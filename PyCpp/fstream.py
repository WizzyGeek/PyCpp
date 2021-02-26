from os import PathLike
from typing import Union

from .ostream import flush, endl
from .iostream import basic_ostream

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

class ifstream:
    def __init__(self, fileName:str) -> None:
        self.file = fileName

def getline(ifstream):
    return open(ifstream.file).readlines()
