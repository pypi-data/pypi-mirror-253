# SPDX-License-Identifier: MIT

from collections.abc import Generator, Iterable
from importlib.metadata import PackageNotFoundError, version
from io import RawIOBase
from pathlib import Path

from versioning.pep440 import NoVersion, Project

try:
    __version__ = version("<your python package's name>")
except PackageNotFoundError:
    # package is not installed
    with Project(path=Path(__file__).parent) as project:
        try:
            __version__ = str(project.version())
        except NoVersion:
            __version__ = str(project.release(dev=0))


def inbuffered(iterable: Iterable[bytes]) -> Generator[bytes, int, None]:
    size = yield b""
    for data in iterable:
        while data:
            chunk, data = data[:size], data[size:]
            size = yield chunk


class RawIterIO(RawIOBase):
    def __init__(self, data: Iterable[bytes], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data = inbuffered(data)
        next(self._data)

    def readinto(self, b, /) -> int:
        try:
            data = self._data.send(len(b))
        except StopIteration:
            return 0

        b[: len(data)] = data
        return len(data)

    def readable(self) -> bool:
        return True
