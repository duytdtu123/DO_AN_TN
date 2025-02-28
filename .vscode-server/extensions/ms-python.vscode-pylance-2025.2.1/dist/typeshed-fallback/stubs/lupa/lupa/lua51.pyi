from _typeshed import MaybeNone
from collections.abc import Callable, Iterator
from typing import Any, Final, Generic, TypeVar, type_check_only

__all__ = [
    "LUA_VERSION",
    "LUA_MAXINTEGER",
    "LUA_MININTEGER",
    "LuaRuntime",
    "LuaError",
    "LuaSyntaxError",
    "LuaMemoryError",
    "as_itemgetter",
    "as_attrgetter",
    "lua_type",
    "unpacks_lua_table",
    "unpacks_lua_table_method",
]

LUA_MAXINTEGER: Final[int]
LUA_MININTEGER: Final[int]
LUA_VERSION: Final[tuple[int, int]]

# cyfunction object
as_attrgetter: Callable[[object], object]
as_itemgetter: Callable[[object], object]

# cyfunction object
lua_type: Callable[[object], str | MaybeNone]

# cyfunction object as decorator
unpacks_lua_table: Callable[[Callable[..., Any]], Callable[..., Any]]
unpacks_lua_table_method: Callable[[Callable[..., Any]], Callable[..., Any]]

# inner classes

@type_check_only
class _LuaIter:
    def __iter__(self) -> Iterator[object]: ...

@type_check_only
class _LuaTable:
    def keys(self) -> _LuaIter: ...
    def values(self) -> _LuaIter: ...
    def items(self) -> _LuaIter: ...

@type_check_only
class _LuaNoGC: ...

@type_check_only
class _LuaObject: ...

# classes

_bint = TypeVar("_bint", bool, int)

class FastRLock(Generic[_bint]):
    # @classmethod
    # def __init__(cls, /, *args: Any, **kwargs: Any) -> None: ...
    def acquire(self, blocking: _bint = True) -> _bint: ...
    def release(self) -> None: ...
    def __enter__(self) -> _bint: ...
    def __exit__(self, t: object, v: object, tb: object) -> None: ...

class LuaError(Exception): ...
class LuaSyntaxError(LuaError): ...
class LuaMemoryError(LuaError, MemoryError): ...

class LuaRuntime:
    lua_implementation: Final[str]
    lua_version: Final[tuple[int, int]]

    # @classmethod
    # def __cinit__(cls, unpack_return_tuples: bool) -> None: ...
    # def add_pending_unref(self, ref: int) -> None: ...
    # def clean_up_pending_unrefs(self) -> int: ...
    def get_max_memory(self, total: bool = False) -> int | MaybeNone: ...
    def get_memory_used(self, total: bool = False) -> int | MaybeNone: ...
    # def reraise_on_exceptions(self) -> int: ...
    # def store_raised_exception(self, L: object, lua_error_msg: str) -> None: ...  # unannotated
    def eval(self, lua_code: str, *args: Any, name: str | None = None, mode: str | None = None) -> object: ...
    def execute(self, lua_code: str, *args: Any, name: str | None = None, mode: str | None = None) -> object: ...
    def compile(self, lua_code: str, name: str | None = None, mode: str | None = None) -> Callable[..., object]: ...
    def require(self, modulename: str) -> object: ...
    def globals(self) -> _LuaTable: ...
    def table(self, *items: Any, **kwargs: Any) -> _LuaTable: ...
    def table_from(self, *args: Any, recursive: bool = ...) -> _LuaTable: ...
    def nogc(self) -> _LuaNoGC: ...
    def gccollect(self) -> None: ...
    def set_max_memory(self, max_memory: int, total: bool = False) -> None: ...
    def set_overflow_handler(self, overflow_handler: Callable[..., None]) -> None: ...
    # def register_py_object(self, cname: str, pyname: str, obj: object) -> int: ...
    # def init_python_lib(self, register_eval: bool, register_builtins: bool) -> int: ...
