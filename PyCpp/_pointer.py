from inspect import currentframe, getouterframes
from linecache import getline
from typing import Any, Dict, Tuple

try:
    from varname import argname
except (ModuleNotFoundError, ImportError):
    argname = None

from .errors import NullPointerAccess

__all__ = (
    "Pointer",
)

def _getattr(obj, attrs: Tuple[str]):
    for i in attrs:
        obj = getattr(obj, i)
    return obj

def _setattr(obj, attrs: Tuple[str], val = None) -> None:
    setattr(_getattr(obj, attrs[:-1]), attrs[-1], val)

class Pointer:
    """A virtual Pointer

    This virtual Pointer works by maintaining a reference to
    the global and local scopes in a namespace and the name of the
    variable to which it points.

    Its limitataion is that `__init__` constructor can only be used in
    enviroments where linecache is functional, otherwise, meta-information
    such as the variable's name cannot be obtained. In such enviroments
    the pointer must be provided the name argument.
    """
    __slots__ = (
        "p_locals",
        "p_globals",
        "p_varname",
        "p_line",
        "_with_attr",
        "_attrs"
    )

    def __init__(self, val, *, name: str = "") -> None:
        f_info = getouterframes(currentframe())[1]
        self.p_line = (f_info.filename, f_info.lineno)
        self.p_locals: Dict[str, Any] = f_info.frame.f_locals
        self.p_globals: Dict[str, Any] = f_info.frame.f_globals

        if (not name) and argname:
            try:
                self.p_varname = argname(val, vars_only=False) # type: str
            except Exception:
                self.p_varname = name
        else:
            self.p_varname = name

        self._with_attr: bool = False

        if not self.p_varname.isidentifier():
            temp: Tuple[str] = tuple(self.p_varname.split("."))
            if not all(i.isidentifier() for i in temp):
                self._attrs = () # type: tuple[str]
            else:
                self._with_attr = True
                self.p_varname = temp[0]
                self._attrs = temp[1:]

    def __repr__(self) -> str:
        return f"<Pointer to {self.p_varname} of {self.p_line[0]}>" if self else "<Null Pointer>"

    @property
    def namespace(self) -> dict:
        # NOTE:: [A variable might exist in both the local and global scope
        #         We prefer the local scope over the global we choose the global
        #         scope only when the variable is not in the local scope
        #         The boolean expression used here is::
        #
        #           (var_local ⊕ var_global) & var_global
        #
        #         Truth Table:
        #           (1, 1) -> 0, (1, 0) -> 0
        #           (0, 1) -> 1, (0, 0) -> 0
        # ]
        var_local = self.p_varname in self.p_locals
        var_global = self.p_varname in self.p_globals
        return (self.p_locals, self.p_globals)[(var_local ^ var_global) & var_global]

    @property
    def value(self):
        if self.null_ptr:
            l_src = getline(*self.p_line)
            raise NullPointerAccess(
                ("Can't set or access the value of a Null Pointer\n"
                f"At File \"{self.p_line[0]}\", line {self.p_line[1]}\n  "
                "cannot get value for expression: "
                f"    '{self.p_varname}'") +
                (" in line:\n      " * bool(l_src)) +
                l_src)
        ret = self.namespace.get(self.p_varname)
        if self._with_attr:
            ret = _getattr(ret, self._attrs)
        return ret

    @value.setter
    def value(self, val) -> None:
        if self.null_ptr:
            l_src = getline(*self.p_line)
            raise NullPointerAccess(
                ("Can't set or access the value of a Null Pointer\n"
                f"At File \"{self.p_line[0]}\", line {self.p_line[1]}\n  "
                "cannot set value for expression:\n"
                f"    '{self.p_varname}'") +
                (" in line:\n      " * bool(l_src)) +
                l_src)
        if self._with_attr:
            return _setattr(self.namespace.get(self.p_varname), self._attrs, val)
        self.namespace[self.p_varname] = val

    @property
    def null_ptr(self) -> bool:
        return not self

    def __bool__(self):
        return bool(self.namespace and self.p_varname.isidentifier())

    @classmethod
    def from_ref(cls, name: str, l_namesp: dict, g_namesp: dict, line: Tuple[str, int] = ("None", 0)):
        self = cls.__new__(cls) # Dont wanna call __init__
        self.p_line = line
        self.p_locals = l_namesp
        self.p_globals = g_namesp
        self.p_varname = name
        self._with_attr = False

        if not self.p_varname.isidentifier():
            temp: Tuple[str] = tuple(self.p_varname.split("."))
            if not all(i.isidentifier() for i in temp):
                self._attrs = ()
            else:
                self._with_attr = True
                self.p_varname = temp[0]
                self._attrs = temp[1:]

        return self
