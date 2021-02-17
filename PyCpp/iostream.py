import forbiddenfruit as ff

__all__ = (
    "endl",
    "cout",
    "cin"
)

endl = "\n"

def str_lshift(self, other):
    return self + other

ff.curse(str, "__lshift__", str_lshift)

class OutStream:
    def __lshift__(self, content):
        print(content, end = "")
        return content

class InStream:
    def __rshift__(self, content):
        return input(content)

cout = OutStream()
cin = InStream()