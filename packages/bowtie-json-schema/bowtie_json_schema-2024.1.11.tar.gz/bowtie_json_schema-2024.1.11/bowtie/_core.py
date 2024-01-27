from __future__ import annotations

from collections import deque
from contextlib import asynccontextmanager, suppress
from typing import TYPE_CHECKING, Any, Protocol
import asyncio
import json

from attrs import asdict, field, frozen, mutable
from url import URL
import aiodocker.containers
import aiodocker.docker
import aiodocker.exceptions
import aiodocker.stream

from bowtie import _commands, exceptions

if TYPE_CHECKING:
    from collections.abc import (
        AsyncIterator,
        Awaitable,
        Callable,
        Iterable,
        Set,
    )

    from bowtie._report import Reporter


@frozen
class GotStderr(Exception):
    stderr: bytes


@frozen
class StartupFailed(Exception):
    name: str
    stderr: str = ""
    data: Any = None

    def __str__(self) -> str:
        if self.stderr:
            return f"{self.name}'s stderr contained: {self.stderr}"
        return self.name


@frozen
class NoSuchImage(Exception):
    name: str
    data: Any = None


class StreamClosed(Exception):
    pass


class _InvalidResponse:
    def __repr__(self) -> str:
        return "<InvalidResponse>"


INVALID = _InvalidResponse()


@mutable
class Stream:
    """
    Wrapper to make aiodocker's Stream more pleasant to use.
    """

    _stream: aiodocker.stream.Stream = field(alias="stream")
    _container: aiodocker.containers.DockerContainer = field(alias="container")
    _read_timeout_sec: float | None = field(alias="read_timeout_sec")
    _buffer: deque[bytes] = field(factory=deque, alias="buffer")
    _last: bytes = b""

    @classmethod
    def attached_to(
        cls,
        container: aiodocker.containers.DockerContainer,
        **kwargs: Any,
    ) -> Stream:
        stream = container.attach(stdin=True, stdout=True, stderr=True)
        return cls(stream=stream, container=container, **kwargs)

    def _read_with_timeout(self) -> Awaitable[aiodocker.stream.Message | None]:
        read = self._stream.read_out()
        return asyncio.wait_for(read, timeout=self._read_timeout_sec)

    def send(self, message: dict[str, Any]) -> Awaitable[None]:
        as_bytes = f"{json.dumps(message)}\n".encode()
        return self._stream.write_in(as_bytes)

    async def receive(self) -> bytes:
        if self._buffer:
            return self._buffer.popleft()

        while True:
            message = await self._read_with_timeout()
            if message is not None:
                break
            info: dict[str, Any] = await self._container.show()  # type: ignore[reportUnknownMemberType]
            if info["State"]["FinishedAt"]:
                raise StreamClosed(self)

        if message.stream == 2:  # type: ignore[reportUnknownMemberType]  # noqa: PLR2004
            data: list[bytes] = []

            while message.stream == 2:  # type: ignore[reportUnknownMemberType]  # noqa: PLR2004
                data.append(message.data)  # type: ignore[reportUnknownMemberType]
                message = await self._read_with_timeout()
                if message is None:
                    raise GotStderr(b"".join(data))

        line: bytes
        rest: list[bytes]
        while True:
            line, *rest = message.data.split(b"\n")  # type: ignore[reportUnknownMemberType]
            if rest:
                line, self._last = self._last + line, rest.pop()  # type: ignore[reportUnknownVariableType]
                self._buffer.extend(rest)
                return line  # type: ignore[reportUnknownVariableType]

            message = None
            while message is None:
                message = await self._read_with_timeout()
            self._last += line  # type: ignore[reportUnknownMemberType]


@frozen
class DialectRunner:
    _name: str = field(alias="name")
    _dialect: URL = field(alias="dialect")
    _send: Callable[[_commands.Command[Any]], Awaitable[Any]] = field(
        alias="send",
    )
    _start_response: _commands.StartedDialect = field(alias="start_response")

    @classmethod
    async def start(
        cls,
        send: Callable[[_commands.Command[Any]], Awaitable[Any]],
        dialect: URL,
        name: str,
    ) -> DialectRunner:
        request = _commands.Dialect(dialect=str(dialect))
        return cls(
            name=name,
            send=send,
            dialect=dialect,
            start_response=await send(request),  # type: ignore[reportGeneralTypeIssues]  # uh?? no idea what's going on here.
        )

    def warn_if_unacknowledged(self, reporter: Reporter):
        if self._start_response != _commands.StartedDialect.OK:
            reporter.unacknowledged_dialect(
                implementation=self._name,
                dialect=self._dialect,
                response=self._start_response,
            )

    async def run_validation(
        self,
        command: _commands.Run,
        tests: Iterable[_commands.Test],
    ) -> _commands.SeqResult:
        try:
            response = await self._send(command)  # type: ignore[reportGeneralTypeIssues]  # uh?? no idea what's going on here.
            if response is None:
                result = _commands.Empty()
            elif response is INVALID:
                result = _commands.CaseErrored.uncaught()
            else:
                # FIXME: seq here should just get validated against the run one
                _, result = response
        except GotStderr as error:
            stderr = error.stderr.decode("utf-8")
            result = _commands.CaseErrored.uncaught(stderr=stderr)

        expected: list[bool] | list[None] = [test.valid for test in tests]  # type: ignore[reportAssignmentType]
        return _commands.SeqResult(
            seq=command.seq,
            implementation=self._name,
            expected=expected,
            result=result,
        )


class _MakeValidator(Protocol):
    def __call__(self, dialect: URL | None = None) -> Callable[..., None]:
        ...


@frozen(order=True)
class ImplementationInfo:
    # FIXME: Combine with / separate out more from `Implementation`

    _image: _commands.ImplementationId = field(alias="image")

    name: str
    language: str
    homepage: URL
    issues: URL
    source: URL
    dialects: Set[URL]

    @classmethod
    def from_dict(
        cls,
        homepage: str,
        issues: str,
        source: str,
        dialects: list[str],
        **kwargs: Any,
    ):
        return cls(
            homepage=URL.parse(homepage),
            issues=URL.parse(issues),
            source=URL.parse(source),
            dialects=frozenset(URL.parse(dialect) for dialect in dialects),
            **kwargs,
        )

    @property
    def id(self) -> _commands.ImplementationId:
        return self._image

    def serializable(self):
        as_dict = {k.lstrip("_"): v for k, v in asdict(self).items()}
        as_dict.update(
            homepage=str(as_dict["homepage"]),
            issues=str(as_dict["issues"]),
            source=str(as_dict["source"]),
            dialects=[str(d) for d in as_dict["dialects"]],
        )
        return as_dict


@mutable
class Implementation:
    """
    A running implementation under test.
    """

    name: str

    _make_validator: _MakeValidator = field(alias="make_validator")
    _maybe_validate: Callable[..., None] = field(alias="maybe_validate")
    _reporter: Reporter = field(alias="reporter")

    _docker: aiodocker.docker.Docker = field(repr=False, alias="docker")
    _restarts: int = field(default=20, repr=False, alias="restarts")
    _container: aiodocker.containers.DockerContainer = field(
        default=None,
        repr=False,
        alias="container",
    )
    _stream: Stream = field(default=None, repr=False, alias="stream")
    _read_timeout_sec: float | None = field(
        default=2.0,
        converter=lambda value: value or None,  # type: ignore[reportUnknownArgumentType]
        repr=False,
    )

    metadata: dict[str, Any] | None = None

    # FIXME: Still some refactoring into DialectRunner needed.
    _dialect: URL = None  # type: ignore[reportGeneralTypeIssues]

    @classmethod
    @asynccontextmanager
    async def start(
        cls,
        image_name: str,
        make_validator: _MakeValidator,
        **kwargs: Any,
    ) -> AsyncIterator[Implementation]:
        from bowtie._cli import DRAFT2020

        self = cls(
            name=image_name,
            make_validator=make_validator,
            maybe_validate=make_validator(dialect=DRAFT2020),
            **kwargs,
        )

        try:
            await self._start_container()
        except GotStderr as error:
            err = StartupFailed(name=image_name, stderr=error.stderr.decode())
            raise err from None
        except StreamClosed:
            raise StartupFailed(name=image_name) from None
        except aiodocker.exceptions.DockerError as err:
            # This craziness can go wrong in various ways, none of them
            # machine parseable.

            status, data, *_ = err.args
            if data.get("cause") == "image not known":
                raise NoSuchImage(name=image_name, data=data) from err

            message = ghcr = data.get("message", "")

            if status == 500:  # noqa: PLR2004
                try:
                    # GitHub Registry saying an image doesn't exist as reported
                    # within GitHub Actions' version of Podman...
                    # This is some crazy string like:
                    #   Get "https://ghcr.io/v2/bowtie-json-schema/image-name/tags/list": denied  # noqa: E501
                    # with seemingly no other indication elsewhere and
                    # obviously no real good way to detect this specific case
                    no_image = message.endswith('/tags/list": denied')
                except Exception:  # noqa: BLE001, S110
                    pass
                else:
                    if no_image:
                        raise NoSuchImage(name=image_name, data=data)

                try:
                    # GitHub Registry saying an image doesn't exist as reported
                    # locally via podman on macOS...

                    # message will be ... a JSON string !?! ...
                    error = json.loads(ghcr).get("message", "")
                except Exception:  # noqa: BLE001, S110
                    pass  # nonJSON / missing key
                else:
                    if "403 (forbidden)" in error.casefold():
                        raise NoSuchImage(name=image_name, data=data)

            raise StartupFailed(name=image_name, data=data) from err

        yield self
        await self._stop()

    async def _start_container(self):
        self._container = await self._docker.containers.run(  # type: ignore[reportUnknownMemberType]
            config=dict(
                Image=self.name,
                OpenStdin=True,
                HostConfig=dict(NetworkMode="none"),
            ),
        )
        self._stream = Stream.attached_to(
            self._container,
            read_timeout_sec=self._read_timeout_sec,
        )
        started = await self._send(_commands.START_V1)  # type: ignore[reportGeneralTypeIssues]  # uh?? no idea what's going on here.
        if started is INVALID:
            raise StartupFailed(name=self.name)
        self.metadata = started.implementation

    def info(self) -> ImplementationInfo:
        # FIXME: Do this higher up
        if self.metadata is None:
            raise StartupFailed(name=self.name)

        dialects = frozenset(URL.parse(d) for d in self.metadata["dialects"])
        required = ["name", "language", "homepage", "issues", "source"]
        return ImplementationInfo(
            image=self.name,
            dialects=dialects,
            **{k: self.metadata[k] for k in required},
        )

    def start_speaking(self, dialect: URL) -> Awaitable[DialectRunner]:
        self._dialect = dialect
        self._maybe_validate = self._make_validator(dialect)
        return DialectRunner.start(
            name=self.name,
            send=self._send,
            dialect=dialect,
        )

    async def _stop(self):
        request = _commands.STOP.to_request(validate=self._maybe_validate)  # type: ignore[reportUnknownMemberType]  # uh?? no idea what's going on here.
        with suppress(AttributeError):
            await self._stream.send(request)  # type: ignore[reportUnknownArgumentType]
        with suppress(aiodocker.exceptions.DockerError):
            await self._container.delete(force=True)  # type: ignore[reportUnknownMemberType]

    async def _send_no_response(self, cmd: _commands.Command[Any]):
        request = cmd.to_request(validate=self._maybe_validate)

        try:
            await self._stream.send(request)
        except AttributeError:
            # FIXME: aiodocker doesn't appear to properly report stream closure
            self._restarts -= 1
            await self._container.delete(force=True)  # type: ignore[reportUnknownMemberType]
            await self._start_container()
            await self.start_speaking(dialect=self._dialect)
            await self._stream.send(request)

    async def _send(self, cmd: _commands.Command[Any], retry: int = 3) -> Any:
        await self._send_no_response(cmd)
        for _ in range(retry):
            try:
                response = await self._stream.receive()
            except asyncio.exceptions.TimeoutError:
                continue

            try:
                return cmd.from_response(
                    response=response,
                    validate=self._maybe_validate,
                )
            except exceptions._ProtocolError as error:  # type: ignore[reportPrivateUsage]
                self._reporter.invalid_response(
                    error=error,
                    implementation=self,
                    response=response,
                    cmd=cmd,
                )
                break
        return INVALID
