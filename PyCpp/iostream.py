import forbiddenfruit as ff

__all__ = (
    "endl",
    "cout",
    "cin"
)

endl = "\n"

class OutStream:
    def __lshift__(self, content):
        print(content, end = "")
        return self

class InStream:
    def __rshift__(self, content):
        return input(content)

cout = OutStream()
cin = InStream()