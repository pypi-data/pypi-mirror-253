from __future__ import annotations

from typing import Any, Tuple, Type, Union, get_args, get_origin

AnyType = Type[Any] | Tuple[Type[Any], ...]


def is_optional(type_: Type[Any]):
    return type(None) in get_args(type_)


def remove_optional(type_: Type[Any]):
    if get_origin(type_) != Union:
        return type_

    if not is_optional(type_):
        return type_

    args = get_args(type_)

    if len(args) == 2:
        none_index = args.index(type(None))
        return args[1 - none_index]

    # deep copy
    return_type = Union[int, None]  # could be anything
    return_type.__dict__ = type_.__dict__.copy()

    setattr(return_type, "__args__", tuple(arg for arg in args if arg != type(None)))

    return return_type


def convert_tuple_to_union(type_: AnyType) -> Type[Any]:
    if isinstance(type_, tuple):
        tmp_type_ = Union[int, float]  # could be anything
        setattr(tmp_type_, "__args__", type_)
        type_ = tmp_type_

    return type_
