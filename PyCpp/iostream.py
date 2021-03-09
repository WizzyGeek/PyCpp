from sys import stderr, stdout, stdin
from inspect import getouterframes, currentframe
from typing import Dict, Union, Tuple

from ._pointer import Pointer
from .ostream import endl, flush
from .vector import PY_39

if PY_39:
    from .vector import c_GenericAlias


__all__ = (
    "cout",
    "wcout",
    "clog",
    "wclog",
    "cerr",
    "wcerr",
    "cin",
    "wcin",
    "istream",
    "basic_istream",
    "ostream",
    "basic_ostream",
    "iostream",
    "basic_iostream"
)


class basic_ostream:
    def __init__(self, stream = None) -> None:
        if not stream.writable():
            raise ValueError("Stream must be writeable")
        self.stream = stream

    def __lshift__(self, content):
        print(
            content,
            end="",
            file=self.stream,
            flush=((content is flush) or (content is endl))
        )
        return self

    def flush(self):
        # https://www.cplusplus.com/reference/ostream/basic_ostream/flush/
        self.stream.flush()
        return self

    def __repr__(self):
        return f"<{self.__class__.__name__} of {self.stream.name}>"

    if PY_39:
        __class_getitem__ = c_GenericAlias


class ostream_unbuf(basic_ostream):
    def __lshift__(self, content):
        print(content, end="", file=self.stream, flush=True)
        return self


def _parse_vars(pystmt: str):
    if pystmt.isspace() or not pystmt:
        return []
    if ">>" in pystmt:
        k = pystmt.split(">>")[1:]
        vars = []
        for j in k:
            j = j.strip().lstrip("(").rstrip(")")
            if "." in j:
                k = tuple(j.split("."))
                if all(i.isidentifier() for i in k):
                    vars.append(j)
            else:
                vars.append(j)
        return vars


class basic_istream:
    def __init__(self, stream) -> None:
        self._cache: Dict[str, Dict[int, Dict[str, Union[Tuple[Pointer, int]]]]] = {}
        if not stream.readable():
            raise ValueError("stream must be readable")
        self.stream = stream

    def __rshift__(self, _):
        f_info = getouterframes(currentframe())[1]
        filename = f_info.filename
        lineno = f_info.lineno
        cache = self._cache

        if filename not in cache:
            cache[filename] = {}
        if lineno not in cache[filename]:
            f_locals = f_info.frame.f_locals
            f_globals = f_info.frame.f_globals

            stmts = f_info.code_context[0].strip().split("#")[0].split(";")

            ptrs = []
            for i in stmts:
                # We got called in a line so I presume all
                # rshifts are for basic_istream and parse them
                for j in _parse_vars(i):
                    ptrs.append(Pointer.from_ref(j, f_locals, f_globals, (filename, lineno)))

            ptr_cache = cache[filename][lineno] = {
                "ptrs": tuple(ptrs),
                "index": 0
            }
        else:
            ptr_cache = cache[filename][lineno]

        ptr_cache["ptrs"][ptr_cache["index"]].value = self.__stream_get__()
        ptr_cache["index"] = (ptr_cache["index"] + 1) % len(ptr_cache["ptrs"])
        return self

    def __stream_get__(self) -> str:
        return self.stream.readline()[:-1]

    def __repr__(self):
        return f"<{self.__class__.__name__} of {self.stream.name}>"

    if PY_39:
        __class_getitem__ = c_GenericAlias

class basic_iostream(basic_istream, basic_ostream):
    def __init__(self, stream) -> None:
        super(basic_istream, self).__init__(stream)
        super(basic_ostream, self).__init__(stream)

# Type Aliases in Py3.9
if PY_39:
    istream = basic_istream[str]
    ostream = basic_ostream[str]
    iostream = basic_iostream[str]
else:
    istream = basic_istream
    ostream = basic_ostream
    iostream = basic_iostream

# NOTE
# In python we only have bytes, str
# hence wc* and c* are actually the same
# We define them twice so that the identity
# is different

cout = basic_ostream(stdout)
wcout = basic_ostream(stdout)

clog = basic_ostream(stderr)
wclog = basic_ostream(stderr)

cerr = ostream_unbuf(stderr)
wcerr = ostream_unbuf(stderr)

cin = basic_istream(stdin)
wcin = basic_istream(stdin)
