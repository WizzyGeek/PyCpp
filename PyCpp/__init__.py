from .iostream import *

class std: pass

excluded_globals = {"std", "excluded_globals"}

# populate std namespace
for _i, _j in globals():
    if not (_i.startswith("_") or _i in excluded_globals):
        setattr(std, _i, _j)