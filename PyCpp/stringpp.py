import forbiddenfruit as ff

__all__ = (
    "strlen",
    "tolower"
)

def str_lshift(self, other):
    return self + other

def tolower(self:str) -> str:
    return self.lower()

def strlen(self:str) -> int:
    return len(self)

ff.curse(str, "__lshift__", str_lshift)