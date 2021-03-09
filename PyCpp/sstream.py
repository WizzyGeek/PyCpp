from io import StringIO

from .iostream import basic_iostream
from .fstream import basic_ifstream
from .vector import PY_39

__all__ = (
    "stringstream",
    "basic_stringstream"
)


class basic_stringstream(basic_iostream):
    def __init__(self, string: str):
        self.stream = StringIO(string)
        self._buffer = []

    __stream_get__ = basic_ifstream.__stream_get__

    def str(self):
        return self.stream.getvalue()

if PY_39:
    stringstream = basic_stringstream[str]
else:
    stringstream = basic_stringstream