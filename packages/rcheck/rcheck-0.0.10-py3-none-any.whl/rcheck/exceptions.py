from __future__ import annotations

from collections.abc import (
    Mapping,
    MutableMapping,
    MutableSequence,
    MutableSet,
    Sequence,
    Set,
)
from typing import Any, Optional, Type


class BaseException(Exception):
    type_: Type[Any]

    def __init__(
        self,
        name: str,
        value: Any,
        description: Optional[str] = None,
    ):
        self._name = name
        self._value = value
        self._description = description

    def __str__(self):
        output = f"Error in param: {self._name} got value {self._value} is not of type {self.type_.__name__}."

        if self._description is not None:
            output += "\n\n" + self._description

        return output


class StrException(BaseException):
    type_ = str


class BytesException(BaseException):
    type_ = bytes


class BoolException(BaseException):
    type_ = bool


class FloatException(BaseException):
    type_ = float


class IntException(BaseException):
    type_ = int


class OptStrException(BaseException):
    type_ = str
    is_optional = True


class OptBytesException(BaseException):
    type_ = bytes
    is_optional = True


class OptBoolException(BaseException):
    type_ = bool
    is_optional = True


class OptFloatException(BaseException):
    type_ = float
    is_optional = True


class OptIntException(BaseException):
    type_ = int
    is_optional = True


class SequenceException(BaseException):
    type_ = Sequence


class MutableSequenceException(BaseException):
    type_ = MutableSequence


class SetException(BaseException):
    type_ = Set


class MutableSetException(BaseException):
    type_ = MutableSet


class MappingException(BaseException):
    type_ = Mapping


class MutableMappingException(BaseException):
    type_ = MutableMapping


# TODO: Need to impl the X`of`Exception's


class SequenceOfException(BaseException):
    type_ = Sequence


class SetOfException(BaseException):
    type_ = Set


class MutableSequenceOfException(BaseException):
    type_ = MutableSequence


class MutableSetOfException(BaseException):
    type_ = MutableSet
