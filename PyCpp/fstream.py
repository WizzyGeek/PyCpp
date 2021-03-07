from os import PathLike
from typing import Union

from .iostream import basic_ostream, basic_istream

__all__ = (
    "ofstream",
    "ifstream",
    "getline"
)


class ofstream(basic_ostream):
    def __init__(self, file: Union[str, PathLike]) -> None:
        self.stream = open(file, "w+")

    def close(self) -> None:
        self.stream.close()

    def is_open(self) -> bool:
        return not self.stream.closed

class ifstream(basic_istream):
    def __init__(self, fileName: Union[str, PathLike]) -> None:
        self.stream = open(fileName, "r")
        self._buffer = []

    def __stream_get__(self):
        if not self._buffer:
            self._buffer = super().__stream_get__().split()
        return self._buffer.pop(0)

def getline(ifstream):
    for i in ifstream.stream.readlines():
        yield i[:-1]
