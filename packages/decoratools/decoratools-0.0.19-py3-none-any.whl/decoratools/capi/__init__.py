import ctypes
from collections.abc import Callable, Iterator, Mapping
from dataclasses import dataclass
from enum import IntEnum, IntFlag
from functools import wraps
from inspect import Signature, currentframe, signature
from types import GenericAlias
from typing import (
    Annotated,
    Any,
    ParamSpec,
    TypeVar,
    get_args,
    get_origin,
    get_type_hints,
)


class ARRAY:
    def __class_getitem__(cls, *args):
        return GenericAlias(cls, *args)


@wraps(ctypes.POINTER, updated=())
class POINTER:
    def __new__(cls, *args, **kwargs):
        return ctypes.POINTER(*args, **kwargs)

    def __class_getitem__(cls, *args):
        return GenericAlias(cls, *args)


@wraps(ctypes.CFUNCTYPE, updated=())
class CFUNCTYPE:
    def __new__(cls, *args, **kwargs):
        return ctypes.CFUNCTYPE(*args, **kwargs)

    def __class_getitem__(cls, *args):
        return GenericAlias(cls, *args)


def _ctype(type_hint: Annotated | type[IntEnum | IntFlag] | type["ctypes._CData"]) -> "ctypes._CData":
    if get_origin(type_hint) is ARRAY:
        ctype, length = get_args(type_hint)
        return _ctype(ctype) * length
    if get_origin(type_hint) is POINTER:
        return ctypes.POINTER(_ctype(*get_args(type_hint)))
    if get_origin(type_hint) is CFUNCTYPE:
        return ctypes.CFUNCTYPE(*map(_ctype, get_args(type_hint)))
    if issubclass(type_hint, (IntEnum, IntFlag)):
        return ctypes.c_int
    return type_hint


def _fields(
    cls: type[ctypes.Structure | ctypes.Union],
    globals: dict[str, Any],
    locals: Mapping[str, Any],
) -> Iterator[tuple[str, "ctypes._CData"]]:
    for key, value in get_type_hints(cls, globalns=globals, localns=locals).items():
        yield key, _ctype(value)


_Structure = ctypes.Structure | ctypes.LittleEndianStructure | ctypes.BigEndianStructure
_Union = ctypes.Union | ctypes.LittleEndianUnion | ctypes.BigEndianUnion


def bind(
    cls: type[_Structure | _Union],
    *,
    globals: dict[str, Any] | None = None,
    locals: Mapping[str, Any] | None = None,
) -> None:
    context = currentframe().f_back
    if globals is None:
        globals = context.f_globals
    if locals is None:
        locals = context.f_locals

    cls._anonymous_ = tuple(_anonymous(cls, globals=globals, locals=locals))
    cls._fields_ = list(_fields(cls, globals=globals, locals=locals))


def _anonymous(cls: type[_Structure | _Union], globals: dict[str, Any], locals: Mapping[str, Any]) -> Iterator[str]:
    for key, value in get_type_hints(cls, globalns=globals, localns=locals, include_extras=True).items():
        if "decoratools.capi.anonymous" in get_args(value):
            yield key


def structure(
    cls: type | None = None,
    *,
    autobind: bool = True,
    pack: int | None = None,
    endianness: str = "native",
    **kwargs,
) -> type | Callable[[type], type]:
    _dataclass = dataclass(init=False, frozen=False, slots=False, weakref_slot=False, **kwargs)
    match endianness:
        case "native":
            structure = ctypes.Structure
        case "little":
            structure = ctypes.LittleEndianStructure
        case "big":
            structure = ctypes.BigEndianStructure
        case _:
            raise ValueError(
                f"expected 'endianness' to be one of: 'native', 'little', or 'big', but got '{endianness}'"
            )

    def wrapper(cls: type, context=None) -> type:
        if context is None:
            context = currentframe().f_back

        cls = _dataclass(cls)

        @wraps(cls, updated=())
        class Wrap(cls, structure):
            if autobind:
                _anonymous_ = tuple(_anonymous(cls, globals=context.f_globals, locals=context.f_locals))
                _fields_ = list(_fields(cls, globals=context.f_globals, locals=context.f_locals))
            if pack is not None:
                _pack_ = pack

        return Wrap

    if cls is None:
        return wrapper

    return wrapper(cls, context=currentframe().f_back)


def union(
    cls: type | None = None,
    *,
    autobind: bool = True,
    pack: int | None = None,
    endianness: str = "native",
    **kwargs,
) -> type | Callable[[type], type]:
    _dataclass = dataclass(init=False, frozen=False, slots=False, weakref_slot=False, **kwargs)
    match endianness:
        case "native":
            union = ctypes.Union
        case "little":
            union = ctypes.LittleEndianUnion
        case "big":
            union = ctypes.BigEndianUnion
        case _:
            raise ValueError(
                f"expected 'endianness' to be one of: 'native', 'little', or 'big', but got '{endianness}'"
            )

    def wrapper(cls: type, context=None) -> type:
        if context is None:
            context = currentframe().f_back
        cls = _dataclass(cls)

        @wraps(cls, updated=())
        class Wrap(cls, union):
            if autobind:
                _anonymous_ = tuple(_anonymous(cls, globals=context.f_globals, locals=context.f_locals))
                _fields_ = list(_fields(cls, globals=context.f_globals, locals=context.f_locals))
            if pack is not None:
                _pack_ = pack

        return Wrap

    if cls is None:
        return wrapper

    return wrapper(cls, context=currentframe().f_back)


T = TypeVar("T")
P = ParamSpec("P")


def unwraps(
    cfunc: "ctypes._FuncPtr", *, errcheck: Callable | None = None
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    def decorator(template: Callable[P, T], *, errcheck: Callable | None = errcheck) -> Callable[P, T]:
        context = currentframe().f_back
        prototype = signature(template)

        if unqualified := tuple(
            parameter.name for parameter in prototype.parameters.values() if parameter.annotation is Signature.empty
        ):
            raise ValueError(f"Missing type hint for the following parameters of {template}: {', '.join(unqualified)}")

        if prototype.return_annotation is Signature.empty:
            raise ValueError(f"{template} is missing a return type hint")

        hints = get_type_hints(template, globalns=context.f_globals, localns=context.f_locals, include_extras=True)
        cfunc.restype = _ctype(hints.pop("return"))
        cfunc.argtypes = [_ctype(hint) for hint in hints.values()]
        if errcheck is not None:
            cfunc.errcheck = errcheck

        @wraps(template)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            return cfunc(*args, **kwargs)

        return wrapper

    return decorator
