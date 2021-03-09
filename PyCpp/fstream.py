from os import PathLike
from typing import Union

from .iostream import basic_ostream, basic_istream
from .vector import PY_39

__all__ = (
    "ofstream",
    "basic_ofstream",
    "ifstream",
    "basic_ifstream",
    "getline"
)


class basic_ofstream(basic_ostream):
    def __init__(self, file: Union[str, PathLike]) -> None:
        self.stream = open(file, "w+")

    def close(self) -> None:
        self.stream.close()

    def is_open(self) -> bool:
        return not self.stream.closed


class basic_ifstream(basic_istream):
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

if PY_39:
    ofstream = basic_ofstream[str]
    ifstrem = basic_ifstream[str]
else:
    ofstream = basic_ofstream
    ifstream = basic_ifstream
