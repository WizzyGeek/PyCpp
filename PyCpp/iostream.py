from sys import stderr, stdout

from .ostream import endl, flush

__all__ = (
    "cout",
    "wcout",
    "clog",
    "wclog",
    "cerr",
    "wcerr",
    "cin",
    "wcin"
)

class basic_ostream:
    def __init__(self, stream = None) -> None:
        self.stream = stream

    def __lshift__(self, content) -> None:
        print(
            content,
            end=None,
            file=self.stream,
            flush=((content is flush) or (content is endl))
        )

class ostream_unbuf(basic_ostream):
    def __lshift__(self, content) -> None:
        print(content, end=None, file=self.stream, flush=True)

class basic_istream:
    def __rshift__(self, content) -> str:
        return input(content)

# NOTE
# In python we only have bytes, str
# hence wc* and c* are actually the same
# We define them twice so that the identity
# is different

# cout, wcout shall be different objects
cout = basic_ostream(stdout)
wcout = basic_ostream(stdout)

clog = basic_ostream(stderr)
wclog = basic_ostream(stderr)

cerr = ostream_unbuf(stderr)
wcerr = ostream_unbuf(stderr)

cin = basic_istream()
wcin = basic_istream()
