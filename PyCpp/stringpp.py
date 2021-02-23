import forbiddenfruit as ff

__all__ = (
    "strlen",
    "tolower",
    "toupper"
)

def str_lshift(self, other):
    return self + str(other)

def str_length(self):
    return len(self)

def tolower(other:str) -> str:
    return other.lower()

def toupper(other:str) -> str:
    return other.upper()

def strlen(other:str) -> int:
    return len(other)

ff.curse(str, "__lshift__", str_lshift)
ff.curse(str, "length", str_length)