from .iostream import *

class std: pass

__version__ = 0.1

excluded_globals = {"std", "excluded_globals", "void"}

void = None

# populate std namespace
for _i, _j in globals().copy().items():
    if not (_i.startswith("_") or _i in excluded_globals):
        setattr(std, _i, _j)