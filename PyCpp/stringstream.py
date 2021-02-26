import forbiddenfruit as ff

__all__ = (
    "stringstream"
)

class stringstream:
    def __init__(self, string:str):
        self.string = string

    def __rshift__(self, other):
        self.string = other.__class__(self.string)
        return self.string