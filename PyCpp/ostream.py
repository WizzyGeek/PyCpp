
__all__ = (
    "endl",
    "ends",
    "flush"
)

_str = type("_str", (str,), {})

endl = str(_str("\n"))
ends = str(_str("\0"))

class _flush:
    def __repr__(self) -> str:
        return ""

flush = _flush()
