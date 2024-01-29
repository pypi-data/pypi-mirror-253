from __future__ import annotations

from collections.abc import (
    Callable,
    Mapping,
    MutableMapping,
    MutableSequence,
    MutableSet,
    Sequence,
    Set,
)
from typing import (
    Any,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
    get_args,
    get_origin,
    overload,
)

AnyType = Type[Any] | Tuple[Type[Any], ...]

T = TypeVar("T")
KT = TypeVar("KT")
VT = TypeVar("VT")

from rcheck.exceptions import (
    BaseException,
    BoolException,
    BytesException,
    FloatException,
    IntException,
    MappingException,
    MutableMappingException,
    MutableSequenceException,
    MutableSequenceOfException,
    MutableSetException,
    MutableSetOfException,
    OptBoolException,
    OptBytesException,
    OptFloatException,
    OptIntException,
    OptStrException,
    SequenceException,
    SequenceOfException,
    SetException,
    SetOfException,
    StrException,
)
from rcheck.type_utils import convert_tuple_to_union, is_optional, remove_optional


class Check:
    """Main type checking class

    Examples
    --------

    Check the type of each input and raise an exception if incorrect.
    >>> from rcheck import r
    >>>
    >>> def sign_up(name: str, age: int):
    >>>     name = r.check_str("user's name", name)
    >>>     age = r.check_int("user's age", age)
    >>>     print(name, age)
    >>>
    >>> sign_up("rcheck", 10)
    ...

    Generic type checking
    >>> from typing import Union, Sequence
    >>> from rcheck import r
    >>>
    >>> my_list = [1, "two", [3.0, None]]
    >>> my_list = r.check_sequence("complicated generic list", my_list, of=Union[int, str, Sequence[Optional[float]]])
    >>> my_list

    Since there are issues setting default parameters in functions to be classes such as lists or dicts,
    rheck will return the correct default.
    >>> from typing import Any, Optional, Sequence
    >>> from rcheck import r
    >>>
    >>> def my_func(values: Optional[Sequence[Any]] = None):
    >>>     values = r.check_opt_sequence("optional values", values)
    >>>     return values
    >>>
    >>> my_func()
    []

    """

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, *, suppress_and_record: bool) -> None:
        ...

    def __init__(self, *, suppress_and_record: bool = False) -> None:
        self._suppress_and_record = suppress_and_record
        self._suppress_and_record_original = suppress_and_record

        if suppress_and_record:
            self._enable_suppress_and_record()

    def _enable_suppress_and_record(self):
        self._suppress_and_record = True
        self._records: List[BaseException] = []

    def _disable_suppress_and_record(self):
        del self._records
        self._suppress_and_record = False

    def _error(self, exception: BaseException) -> Any:
        if self._suppress_and_record:
            self._records.append(exception)
            return exception

        raise exception

    def _generic_isinstance(self, value: Any, type_: AnyType) -> Tuple[bool, Any]:
        # print("generic isinstaance", value, type_)
        # print(value, type_)
        type_ = convert_tuple_to_union(type_)

        if type_ == Any:
            return True, {}

        is_opt = is_optional(type_)
        type_ = remove_optional(type_)

        origin = get_origin(type_)
        args = get_args(type_)

        # or could call the check_opt_* version of checks?
        if is_opt and value is None:
            return True, {}

        checker = Check(suppress_and_record=False)

        if origin == Union:
            # print("IN UNION", args)
            for union_type in args:
                is_type, desc = self._generic_isinstance(value, union_type)
                if is_type:
                    return True, {}

            return False, {}
        elif origin == MutableSequence:
            try:
                checker.check_mutable_sequence("fake-seq-name", value, of=args[0])
                return True, {}
            except BaseException:
                return False, {}
        elif origin == Sequence:
            # print("seq", args)
            try:
                checker.check_sequence("fake-seq-name", value, of=args[0])
                return True, {}
            except BaseException:
                # print("ret false")
                return False, {}
        elif origin == MutableMapping:
            k_args, v_args = args
            try:
                checker.check_mutable_mapping(
                    "fake-seq-name", value, keys_of=k_args, values_of=v_args
                )
                return True, {}
            except BaseException:
                return False, {}
        elif origin == Mapping:
            k_args, v_args = args
            # print("mapping", k_args, v_args)
            try:
                checker.check_mapping(
                    "fake-seq-name", value, keys_of=k_args, values_of=v_args
                )
                return True, {}
            except BaseException:
                return False, {}
        elif origin == MutableSet:
            try:
                checker.check_mutable_set("fake-seq-name", value, of=args[0])
                return True, {}
            except BaseException:
                return False, {}
        elif origin == Set:
            try:
                checker.check_set("fake-seq-name", value, of=args[0])
                return True, {}
            except BaseException:
                return False, {}
        elif isinstance(value, type_):
            return True, {}

        return False, {}

    def check_str(
        self,
        name: str,
        value: Any,
        *,
        description: Optional[str] = None,
    ) -> str:
        """Check whether a value is a string

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a string
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        StrException
            If the value is not a string

        Returns
        -------
        check_str : str
            Input value as a string

        Examples
        --------
        Successful check
        >>> value = "hello"
        >>> value = r.check_str("my string", value)
        >>> value
        "hello"

        Unsuccessful check
        >>> value = 1
        >>> value = r.check_str("my string?", value)
        StrException: Error in param: name got value 1 is not of type str.
        """
        if isinstance(value, str):
            return value

        return self._error(StrException(name, value, description))

    @overload
    def check_opt_str(
        self,
        name: str,
        value: Any,
        *,
        description: Optional[str] = None,
    ) -> str | None:
        ...

    @overload
    def check_opt_str(
        self,
        name: str,
        value: Any,
        *,
        default: str,
        description: Optional[str] = None,
    ) -> str:
        ...

    def check_opt_str(
        self,
        name: str,
        value: Any,
        *,
        default: Optional[str] = None,
        description: Optional[str] = None,
    ) -> str | None:
        """Check whether a value is a string or None

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a string or None
        default: Optional[str]
            Default string value to use in case value is None
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        OptStrException
            If the value is not a string or None

        Returns
        -------
        check_str : str | None
            Input value as a string, otherwise the default value

        Examples
        --------
        Successful check
        >>> value = "hello"
        >>> value = r.check_opt_str("my string", value)
        >>> value
        "hello"

        Successful check
        >>> value = r.check_opt_str("my string", None, default="default value")
        >>> value
        "default value"

        Unsuccessful check
        >>> value = 1
        >>> value = r.check_opt_str("my string?", value)
        OptStrException: Error in param: name got value 1 is not of type str.
        """
        match value:
            case None:
                return default
            case str(_):
                return value
            case _:
                return self._error(OptStrException(name, value, description))

    def check_bytes(
        self,
        name: str,
        value: Any,
        *,
        description: Optional[str] = None,
    ) -> bytes:
        """Check whether a value is bytes

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being bytes
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        BytesException
            If the value is not bytes

        Returns
        -------
        check_bytes : bytes
            Input value as bytes

        Examples
        --------
        Successful check
        >>> value = b"hello"
        >>> value = r.check_bytes("my bytes", value)
        >>> value
        b"hello"

        Unsuccessful check
        >>> value = 1
        >>> value = r.check_bytes("my bytes?", value)
        BytesException: Error in param: name got value 1 is not of type bytes.
        """
        if isinstance(value, bytes):
            return value

        return self._error(BytesException(name, value, description))

    @overload
    def check_opt_bytes(
        self,
        name: str,
        value: Any,
        *,
        description: Optional[str] = None,
    ) -> bytes | None:
        ...

    @overload
    def check_opt_bytes(
        self,
        name: str,
        value: Any,
        *,
        default: bytes,
        description: Optional[str] = None,
    ) -> bytes:
        ...

    def check_opt_bytes(
        self,
        name: str,
        value: Any,
        *,
        default: Optional[bytes] = None,
        description: Optional[str] = None,
    ) -> bytes | None:
        """Check whether a value is bytes or None

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being bytes or None
        default: Optional[bytes]
            Default bytes value to use in case value is None
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        OptBytesException
            If the value is not bytes or None

        Returns
        -------
        check_opt_bytes : bytes | None
            Input value as bytes, otherwise the default value

        Examples
        --------
        Successful check
        >>> value = b"hello"
        >>> value = r.check_opt_bytes("my bytes", value)
        >>> value
        b"hello"

        Successful check
        >>> value = r.check_opt_bytes("my bytes", None, default=b"default value")
        >>> value
        b"default value"

        Unsuccessful check
        >>> value = 1
        >>> value = r.check_opt_bytes("my bytes?", value)
        OptBytesException: Error in param: name got value 1 is not of type bytes.
        """
        match value:
            case None:
                return default
            case bytes(_):
                return value
            case _:
                return self._error(OptBytesException(name, value, description))

    def check_bool(
        self,
        name: str,
        value: Any,
        *,
        description: Optional[str] = None,
    ) -> bool:
        """Check whether a value is a bool

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a bool
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        BoolException
            If the value is not a bool

        Returns
        -------
        check_bool : bool
            Input value as a bool

        Examples
        --------
        Successful check
        >>> r.check_bool("my bool", True)
        True

        Unsuccessful check
        >>> value = 1
        >>> value = r.check_bool("my bool?", value)
        BoolException: Error in param: name got value 1 is not of type bool.
        """
        if isinstance(value, bool):
            return value

        return self._error(BoolException(name, value, description))

    @overload
    def check_opt_bool(
        self,
        name: str,
        value: Any,
        *,
        description: Optional[str] = None,
    ) -> bool | None:
        ...

    @overload
    def check_opt_bool(
        self,
        name: str,
        value: Any,
        *,
        default: bool,
        description: Optional[str] = None,
    ) -> bool:
        ...

    def check_opt_bool(
        self,
        name: str,
        value: Any,
        *,
        default: Optional[bool] = None,
        description: Optional[str] = None,
    ) -> bool | None:
        """Check whether a value is a bool or None

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a bool or None
        default: Optional[bool]
            Default bool value to use in case value is None
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        OptBoolException
            If the value is not a bool or None

        Returns
        -------
        check_opt_bool : bool | None
            Input value as bool, otherwise the default value

        Examples
        --------
        Successful check
        >>> value = r.check_opt_bool("my bool", True)
        >>> value
        True

        Successful check
        >>> value = r.check_opt_bool("my bool", None, default=True)
        >>> value
        True

        Unsuccessful check
        >>> value = 1
        >>> value = r.check_opt_bool("my bool?", value)
        OptBoolException: Error in param: name got value 1 is not of type bool.
        """
        match value:
            case None:
                return default
            case bool(_):
                return value
            case _:
                return self._error(OptBoolException(name, value, description))

    def check_int(
        self,
        name: str,
        value: Any,
        *,
        description: Optional[str] = None,
    ) -> int:
        """Check whether a value is an int

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being an int
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        IntException
            If the value is not an int

        Returns
        -------
        check_int : int
            Input value as an int

        Examples
        --------
        Successful check
        >>> value = 1
        >>> value = r.check_int("my int", value)
        >>> value
        1

        Unsuccessful check
        >>> value = "hello"
        >>> value = r.check_int("my int?", value)
        IntException: Error in param: name got value "hello" is not of type int.
        """
        if isinstance(value, int):
            return value

        return self._error(IntException(name, value, description))

    @overload
    def check_opt_int(
        self,
        name: str,
        value: Any,
        *,
        description: Optional[str] = None,
    ) -> int | None:
        ...

    @overload
    def check_opt_int(
        self,
        name: str,
        value: Any,
        *,
        default: int,
        description: Optional[str] = None,
    ) -> int:
        ...

    def check_opt_int(
        self,
        name: str,
        value: Any,
        *,
        default: Optional[int] = None,
        description: Optional[str] = None,
    ) -> int | None:
        """Check whether a value is an int or None

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being an int
        default: Optional[int]
            Default int value to use in case value is None
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        OptIntException
            If the value is not an int or None

        Returns
        -------
        check_opt_int : int | None
            Input value as an int, otherwise the default value

        Examples
        --------
        Successful check
        >>> value = 1
        >>> value = r.check_opt_int("my int", value)
        >>> value
        1

        Successful check
        >>> value = r.check_opt_int("my int", None, default=1)
        >>> value
        1

        Unsuccessful check
        >>> value = "hello"
        >>> value = r.check_opt_int("my int?", value)
        OptIntException: Error in param: name got value "hello" is not of type int.
        """
        match value:
            case None:
                return default
            case int(_):
                return value
            case _:
                return self._error(OptIntException(name, value, description))

    def check_float(
        self,
        name: str,
        value: Any,
        *,
        description: Optional[str] = None,
    ) -> float:
        """Check whether a value is a float

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a float
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        FloatException
            If the value is not a float

        Returns
        -------
        check_float : float
            Input value as a float

        Examples
        --------
        Successful check
        >>> value = 1.0
        >>> value = r.check_float("my float", value)
        >>> value
        1.0

        Unsuccessful check
        >>> value = "hello"
        >>> value = r.check_float("my float?", value)
        FloatException: Error in param: name got value "hello" is not of type float.
        """
        if isinstance(value, float):
            return value

        return self._error(FloatException(name, value, description))

    @overload
    def check_opt_float(
        self,
        name: str,
        value: Any,
        *,
        description: Optional[str] = None,
    ) -> float | None:
        ...

    @overload
    def check_opt_float(
        self,
        name: str,
        value: Any,
        *,
        default: float,
        description: Optional[str] = None,
    ) -> float:
        ...

    def check_opt_float(
        self,
        name: str,
        value: Any,
        *,
        default: Optional[float] = None,
        description: Optional[str] = None,
    ) -> float | None:
        """Check whether a value is a float or None

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a float
        default: Optional[float]
            Default float value to use in case value is None
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        OptFloatException
            If the value is not a float or None

        Returns
        -------
        check_float : float | None
            Input value as a float, otherwise the default value

        Examples
        --------
        Successful check
        >>> value = 1.0
        >>> value = r.check_float("my float", value)
        >>> value
        1.0

        Successful check
        >>> value = r.check_float("my float", None, default=1.0)
        >>> value
        1.0

        Unsuccessful check
        >>> value = "hello"
        >>> value = r.check_float("my float?", value)
        OptFloatException: Error in param: name got value "hello" is not of type float.
        """
        match value:
            case None:
                return default
            case float(_):
                return value
            case _:
                return self._error(OptFloatException(name, value, description))

    def check_sequence(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = Any,
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> Sequence[T]:
        """Check whether a value is a Sequence and optionally type check elements of the sequence

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a Sequence
        of : Type[T]
            Type of the elements of the Sequence to check
        custom_of_checker : Optional[Callable[[Any], bool]]
            Custom type checking function for sequence elements
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        SequenceException
            If the value is not a sequence
        SequenceOfException
            If the elements in the value are not of type T

        Returns
        -------
        check_sequence : Sequence[T]
            Input value as a sequence

        Examples
        --------
        Successful check
        >>> value = r.check_sequence("my sequence", [])
        >>> value
        []

        Successful check
        >>> from typing import Optional
        >>> value = r.check_sequence("my sequence", [None, 1], of=Optional[int])
        >>> value
        [None, 1]

        Unsuccessful check
        >>> value = r.check_sequence("my sequence?", {})
        SequenceException: Error in param: name got value {} is not of type Sequence.

        Unsuccessful check
        >>> value = r.check_sequence("my sequence of strings?", [2.0], of=str)
        SequenceOfException: Error in param: name got value [2.0] is not of type str.
        """

        # todo: would this (the mutable version) allow for List specific checks as well?
        return cast(
            Sequence[T],
            self._check_generic_sequence(
                name,
                value,
                of,
                None,
                custom_of_checker,
                description,
                Sequence,
                SequenceException,
                SequenceOfException,
            ),
        )

    @overload
    def check_opt_sequence(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = Any,
        default_sequence: Callable[[], Sequence[T]] = lambda: [],
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> Sequence[T]:
        ...

    @overload
    def check_opt_sequence(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = Any,
        default_sequence: Callable[[], Sequence[T] | None] = lambda: None,
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> Sequence[T] | None:
        ...

    def check_opt_sequence(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = Any,
        default_sequence: Callable[[], Sequence[T] | None] = lambda: [],
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> Sequence[T] | None:
        """Check whether a value is a Sequence or None and optionally type check elements of the sequence

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a Sequence
        of : Type[T]
            Type of the elements of the Sequence to check
        default_sequence : Callable[[], Sequence[T] | None]
            If value is None, this function will return the result of the default_sequence function call
        custom_of_checker : Optional[Callable[[Any], bool]]
            Custom type checking function for sequence elements
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        SequenceException
            If the value is not a sequence
        SequenceOfException
            If the elements in the value are not of type T

        Returns
        -------
        check_opt_sequence : Sequence[T] | None
            Input value as a sequence, otherwise the default value

        Examples
        --------
        Successful check
        >>> value = r.check_opt_sequence("my sequence", [])
        >>> value
        []

        Successful check
        >>> value = None
        >>> value = r.check_opt_sequence("my sequence", None)
        >>> value
        []

        Successful check
        >>> from typing import Optional
        >>> value = r.check_opt_sequence("my sequence", [None, 1], of=Optional[int])
        >>> value
        [None, 1]

        Unsuccessful check
        >>> value = r.check_opt_sequence("my sequence?", {})
        SequenceException: Error in param: name got value {} is not of type Sequence.

        Unsuccessful check
        >>> value = r.check_opt_sequence("my sequence of strings?", [2.0], of=str)
        SequenceOfException: Error in param: name got value [2.0] is not of type str.
        """
        if value is None:
            return default_sequence()

        # todo: call _check_generic_sequence
        value = self.check_sequence(
            name,
            value,
            of=of,
            custom_of_checker=custom_of_checker,
            description=description,
        )

        return value

    @overload
    def check_mutable_sequence(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = Any,
        default_element: Optional[Callable[[], T]] = None,
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> MutableSequence[T]:
        ...

    @overload
    def check_mutable_sequence(
        self,
        name: str,
        value: Any,
        *,
        default_element: Callable[[], Any],
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> MutableSequence[Any]:
        ...

    def check_mutable_sequence(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = Any,
        default_element: Optional[Callable[[], T]] = None,
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> MutableSequence[T]:
        """Check whether a value is a MutableSequence and optionally type check elements of the sequence.
        Optionally, replace None elements of the sequence with a default value.

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a MutableSequence
        of : Type[T]
            Type of the elements of the MutableSequence to check
        default_element : Optional[Callable[[], T]]
            If the `of` type is of type `Optional` and this argument is supplied,
            fill in `None` values of the MutableSequence with the result of this function call
        custom_of_checker : Optional[Callable[[Any], bool]]
            Custom type checking function for MutableSequence elements
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        MutableSequenceException
            If the value is not a MutableSequence
        MutableSequenceOfException
            If the elements in the value are not of type T

        Returns
        -------
        check_sequence : MutableSequence[T]
            Input value as a MutableSequence

        Examples
        --------
        Successful check
        >>> value = r.check_mutable_sequence("my mut sequence", [])
        >>> value
        []

        Successful check
        >>> from typing import Optional
        >>> value = r.check_mutable_sequence("my mut sequence", [None, 1], of=Optional[int])
        >>> value
        [None, 1]

        Unsuccessful check
        >>> value = r.check_mutable_sequence("my mut sequence?", {})
        MutableSequenceException: Error in param: name got value {} is not of type Sequence.

        Unsuccessful check
        >>> value = r.check_mutable_sequence("my mut sequence of strings?", [2.0], of=str)
        MutableSequenceOfException: Error in param: name got value [2.0] is not of type str.
        """
        return cast(
            MutableSequence[T],
            self._check_generic_sequence(
                name,
                value,
                of,
                default_element,
                custom_of_checker,
                description,
                MutableSequence,
                MutableSequenceException,
                MutableSequenceOfException,
            ),
        )

    def _check_generic_sequence(
        self,
        name: str,
        value: Any,
        of: Type[T],
        default_element: Callable[[], T] | None,
        custom_of_checker: Callable[[Any], bool] | None,
        description: str | None,
        type_: Type[Sequence[T]],
        exception: Type[BaseException],
        exception_of: Type[BaseException],
    ) -> Any:
        if not isinstance(value, type_):
            return self._error(exception(name, value, description))

        if of is Any:
            return value

        for i, element in enumerate(value):
            if custom_of_checker is not None:
                if custom_of_checker(element):
                    continue

                # todo: pass in element value, type
                return self._error(exception_of(name, value, description))

            is_instance_of, instance_of_desc = self._generic_isinstance(element, of)
            if not is_instance_of:
                return self._error(exception_of(name, value, description))

            if default_element is not None and is_optional(of) and element is None:
                value[i] = default_element()

        return value

    @overload
    def check_opt_mutable_sequence(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = ...,
        default_mutable_sequence: Callable[[], MutableSequence[T]] = lambda: [],
        default_element: Optional[Callable[[], T]] = None,
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> MutableSequence[T]:
        ...

    @overload
    def check_opt_mutable_sequence(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = ...,
        default_mutable_sequence: Callable[
            [], MutableSequence[T] | None
        ] = lambda: None,
        default_element: Optional[Callable[[], T]] = None,
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> MutableSequence[T] | None:
        ...

    def check_opt_mutable_sequence(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = Any,
        default_mutable_sequence: Callable[[], MutableSequence[T] | None] = lambda: [],
        default_element: Optional[Callable[[], T]] = None,
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> MutableSequence[T] | None:
        """Check whether a value is a MutableSequence or None and optionally type check elements of the sequence.
        Optionally, replace None elements of the sequence with a default value.

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a MutableSequence
        of : Type[T]
            Type of the elements of the MutableSequence to check
        default_mutable_sequence : Callable[[], MutableSequence[T] | None]
            If value is None, this function will return the result of the default_sequence function call
        default_element : Optional[Callable[[], T]]
            If the `of` type is of type `Optional` and this argument is supplied,
            fill in `None` values of the MutableSequence with the result of this function call
        custom_of_checker : Optional[Callable[[Any], bool]]
            Custom type checking function for MutableSequence elements
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        MutableSequenceException
            If the value is not a MutableSequence
        MutableSequenceOfException
            If the elements in the value are not of type T

        Returns
        -------
        check_sequence : MutableSequence[T] | None
            Input value as a MutableSequence, otherwise the default value

        Examples
        --------
        Successful check
        >>> value = r.check_opt_mutable_sequence("my mut sequence", [])
        >>> value
        []

        Successful check
        >>> value = r.check_opt_mutable_sequence("my mut sequence", None)
        >>> value
        []

        Successful check
        >>> from typing import Optional
        >>> value = r.check_opt_mutable_sequence("my mut sequence", [None, 1], of=Optional[int])
        >>> value
        [None, 1]

        Unsuccessful check
        >>> value = r.check_opt_mutable_sequence("my mut sequence?", {})
        MutableSequenceException: Error in param: name got value {} is not of type Sequence.

        Unsuccessful check
        >>> value = r.check_opt_mutable_sequence("my mut sequence of strings?", [2.0], of=str)
        MutableSequenceOfException: Error in param: name got value [2.0] is not of type str.
        """
        if value is None:
            return default_mutable_sequence()

        # todo: call _check_generic_sequence
        value = self.check_mutable_sequence(
            name,
            value,
            of=of,
            default_element=default_element,
            custom_of_checker=custom_of_checker,
            description=description,
        )

        return value

    def check_set(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = Any,
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> Set[T]:
        """Check whether a value is a Set and optionally type check elements of the Set

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a Set
        of : Type[T]
            Type of the elements of the set to check
        custom_of_checker : Optional[Callable[[Any], bool]]
            Custom type checking function for Set elements
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        SetException
            If the value is not a Set
        SetOfException
            If the elements in the value are not of type T

        Returns
        -------
        check_set : Set[T]
            Input value as a set

        Examples
        --------
        Successful check
        >>> value = r.check_set("my set", set())
        >>> value
        set()

        Successful check
        >>> from typing import Optional
        >>> value = r.check_set("my set", {None, 1}, of=Optional[int])
        >>> value
        {None, 1}

        Unsuccessful check
        >>> value = r.check_set("my set?", {})
        SetException: Error in param: name got value {} is not of type Set.

        Unsuccessful check
        >>> value = r.check_set("my set of strings?", {2.0}, of=str)
        SetOfException: Error in param: name got value {2.0} is not of type str.
        """
        if not isinstance(value, Set):
            return self._error(SetException(name, value, description))

        value = cast(Set[Any], value)

        if of is Any:
            return value

        for i, element in enumerate(value):
            if custom_of_checker is not None:
                if custom_of_checker(element):
                    continue

                # todo: pass in element value, type
                return self._error(SetOfException(name, value, description))

            is_instance_of, instance_of_desc = self._generic_isinstance(element, of)
            if not is_instance_of:
                return self._error(SetOfException(name, value, description))

        return value

    @overload
    def check_opt_set(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = ...,
        default_set: Callable[[], Set[T]] = lambda: set(),
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> Set[T]:
        ...

    @overload
    def check_opt_set(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = ...,
        default_set: Callable[[], Set[T] | None] = lambda: None,
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> Set[T] | None:
        ...

    def check_opt_set(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = Any,
        default_set: Callable[[], Set[T] | None] = lambda: set(),
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> Set[T] | None:
        """Check whether a value is a Set or None and optionally type check elements of the Set

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a Set
        of : Type[T]
            Type of the elements of the set to check
        default_set : Callable[[], Set[T] | None]
            Default value to return if value is None
        custom_of_checker : Optional[Callable[[Any], bool]]
            Custom type checking function for Set elements
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        SetException
            If the value is not a Set
        SetOfException
            If the elements in the value are not of type T

        Returns
        -------
        check_opt_set : Set[T] | None
            Input value as a set, otherwise the default value

        Examples
        --------
        Successful check
        >>> value = r.check_opt_set("my set", set())
        >>> value
        set()

        >>> value = r.check_opt_set("my set", None)
        >>> value
        set()

        Successful check
        >>> from typing import Optional
        >>> value = r.check_opt_set("my set", {None, 1}, of=Optional[int])
        >>> value
        {None, 1}

        Unsuccessful check
        >>> value = r.check_opt_set("my set?", {})
        SetException: Error in param: name got value {} is not of type Set.

        Unsuccessful check
        >>> value = r.check_opt_set("my set of strings?", {2.0}, of=str)
        SetOfException: Error in param: name got value {2.0} is not of type str.
        """
        if value is None:
            return default_set()

        value = self.check_set(
            name,
            value,
            of=of,
            custom_of_checker=custom_of_checker,
            description=description,
        )

        return value

    def check_mutable_set(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = Any,
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> MutableSet[T]:
        """Check whether a value is a MutableSet and optionally type check elements of the MutableSet

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a MutableSet
        of : Type[T]
            Type of the elements of the set to check
        custom_of_checker : Optional[Callable[[Any], bool]]
            Custom type checking function for mutable set elements
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        MutableSetException
            If the value is not a MutableSet
        MutableSetOfException
            If the elements in the value are not of type T

        Returns
        -------
        check_mutable_set : Optional[Set[T]]
            Input value as a set

        Examples
        --------
        Successful check
        >>> value = r.check_mutable_set("my set", set())
        >>> value
        set()

        Successful check
        >>> from typing import Optional
        >>> value = r.check_mutable_set("my set", {None, 1}, of=Optional[int])
        >>> value
        {None, 1}

        Unsuccessful check
        >>> value = r.check_mutable_set("my set?", {})
        MutableSetException: Error in param: name got value {} is not of type Set.

        Unsuccessful check
        >>> value = r.check_mutable_set("my set of strings?", {2.0}, of=str)
        MutableSetOfException: Error in param: name got value {2.0} is not of type str.
        """
        if not isinstance(value, MutableSet):
            return self._error(MutableSetException(name, value, description))

        value = self.check_set(
            name,
            value,
            of=of,
            custom_of_checker=custom_of_checker,
            description=description,
        )

        return value

    @overload
    def check_opt_mutable_set(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = ...,
        default_mutable_set: Callable[[], MutableSet[T]] = lambda: set(),
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> MutableSet[T]:
        ...

    @overload
    def check_opt_mutable_set(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = ...,
        default_mutable_set: Callable[[], MutableSet[T] | None] = lambda: None,
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> MutableSet[T] | None:
        ...

    def check_opt_mutable_set(
        self,
        name: str,
        value: Any,
        *,
        of: Type[T] = Any,
        default_mutable_set: Callable[[], MutableSet[T] | None] = lambda: set(),
        custom_of_checker: Optional[Callable[[Any], bool]] = None,
        description: Optional[str] = None,
    ) -> MutableSet[T] | None:
        """Check whether a value is a MutableSet or None and optionally type check elements of the MutableSet

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a MutableSet
        of : Type[T]
            Type of the elements of the set to check
        default_mutable_set : Callable[[], MutableSet[T] | None]
            Default value to use in case the passed in value is None
        custom_of_checker : Optional[Callable[[Any], bool]]
            Custom type checking function for mutable set elements
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        MutableSetException
            If the value is not a MutableSet
        MutableSetOfException
            If the elements in the value are not of type T

        Returns
        -------
        check_opt_mutable_set : Set[T] | None
            Input value as a set, otherwise the default value

        Examples
        --------
        Successful check
        >>> value = r.check_opt_mutable_set("my set", set())
        >>> value
        set()

        Successful check
        >>> value = r.check_opt_mutable_set("my set", None)
        >>> value
        set()

        Successful check
        >>> from typing import Optional
        >>> value = r.check_opt_mutable_set("my set", {None, 1}, of=Optional[int])
        >>> value
        {None, 1}

        Unsuccessful check
        >>> value = r.check_opt_mutable_set("my set?", {})
        MutableSetException: Error in param: name got value {} is not of type Set.

        Unsuccessful check
        >>> value = r.check_opt_mutable_set("my set of strings?", {2.0}, of=str)
        MutableSetOfException: Error in param: name got value {2.0} is not of type str.
        """
        if value is None:
            return default_mutable_set()

        value = self.check_mutable_set(
            name,
            value,
            of=of,
            custom_of_checker=custom_of_checker,
            description=description,
        )

        return value

    def check_mapping(
        self,
        name: str,
        value: Any,
        *,
        keys_of: Type[KT] = Any,
        values_of: Type[VT] = Any,
        description: Optional[str] = None,
    ) -> Mapping[KT, VT]:
        """Check whether a value is a Mapping and optionally type check keys and values of the mapping

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a Mapping
        keys_of : Type[KT]
            Type of the keys of the mapping to check
        values_of : Type[VT]
            Type of the values of the mapping to check
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        MappingException
            If the value is not a mapping
        MappingOfException
            If the elements in the value are not of type T

        Returns
        -------
        check_mapping : Mapping[KT, VT]
            Input value as a mapping

        Examples
        --------
        Successful check
        >>> value = r.check_mapping("my mapping", {})
        >>> value
        {}

        Successful check
        >>> from typing import Optional
        >>> value = r.check_mapping("my mapping", {"a": 1}, keys_of=str, values_of=int)
        >>> value
        {"a": 1}

        Unsuccessful check
        >>> value = r.check_mapping("my mapping?", [])
        MappingException: Error in param: name got value [] is not of type Mapping.

        Unsuccessful check
        >>> value = r.check_mapping("my mapping of strings?", {1: 2}, keys_of=str)
        MappingOfException: Error in param: name got value {1: 2} is not of type str.
        """
        if not isinstance(value, Mapping):
            return self._error(MappingException(name, value, description))

        # todo: catch errors here:
        if keys_of is not Any:
            self.check_sequence(
                f"keys of {name}", list(cast(Sequence[KT], value.keys())), of=keys_of
            )

        # todo: catch errors here:
        if values_of is not Any:
            self.check_sequence(
                f"values of {name}",
                list(cast(Sequence[VT], value.values())),
                of=values_of,
            )

        # todo: if any errors: raise MappingException() from ...

        return cast(Mapping[KT, VT], value)

    @overload
    def check_opt_mapping(
        self,
        name: str,
        value: Any,
        *,
        default_mapping: Callable[[], Mapping[KT, VT]] = lambda: {},
        keys_of: Type[KT] = ...,
        values_of: Type[VT] = ...,
        description: Optional[str] = None,
    ) -> Mapping[KT, VT]:
        ...

    @overload
    def check_opt_mapping(
        self,
        name: str,
        value: Any,
        *,
        default_mapping: Callable[[], Mapping[KT, VT] | None] = lambda: None,
        keys_of: Type[KT] = ...,
        values_of: Type[VT] = ...,
        description: Optional[str] = None,
    ) -> Mapping[KT, VT] | None:
        ...

    def check_opt_mapping(
        self,
        name: str,
        value: Any,
        *,
        default_mapping: Callable[[], Mapping[KT, VT] | None] = lambda: {},
        keys_of: Type[KT] = Any,
        values_of: Type[VT] = Any,
        description: Optional[str] = None,
    ) -> Mapping[KT, VT] | None:
        """Check whether a value is a Mapping or None and optionally type check keys and values of the mapping

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a Mapping
        default_mapping : Callable[[], Mapping[KT, VT] | None]
            Default value to use in case the mapping is None
        keys_of : Type[KT]
            Type of the keys of the mapping to check
        values_of : Type[VT]
            Type of the values of the mapping to check
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        MappingException
            If the value is not a mapping
        MappingOfException
            If the elements in the value are not of type T

        Returns
        -------
        check_mapping : Mapping[KT, VT] | None
            Input value as a mapping, otherwise the default value

        Examples
        --------
        Successful check
        >>> value = r.check_mapping("my mapping", {})
        >>> value
        {}

        Successful check
        >>> value = r.check_mapping("my mapping", None)
        >>> value
        {}

        Successful check
        >>> from typing import Optional
        >>> value = r.check_mapping("my mapping", {"a": 1}, keys_of=str, values_of=int)
        >>> value
        {"a": 1}

        Unsuccessful check
        >>> value = r.check_mapping("my mapping?", [])
        MappingException: Error in param: name got value [] is not of type Mapping.

        Unsuccessful check
        >>> value = r.check_mapping("my mapping of strings?", {1: 2}, keys_of=str)
        MappingOfException: Error in param: name got value {1: 2} is not of type str.
        """
        if value is None:
            return default_mapping()

        value = self.check_mapping(
            name,
            value,
            keys_of=keys_of,
            values_of=values_of,
            description=description,
        )

        return value

    def check_mutable_mapping(
        self,
        name: str,
        value: Any,
        *,
        keys_of: Type[KT] = Any,
        values_of: Type[VT] = Any,
        description: Optional[str] = None,
    ) -> MutableMapping[KT, VT]:
        """Check whether a value is a MutableMapping and optionally type check keys and values of the mapping

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a MutableMapping
        keys_of : Type[KT]
            Type of the keys of the mapping to check
        values_of : Type[VT]
            Type of the values of the mapping to check
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        MutableMappingException
            If the value is not a MutableMapping
        MutableMappingOfException
            If the elements in the value are not of type T

        Returns
        -------
        check_mutable_mapping : MutableMapping[KT, VT]
            Input value as a mutable mapping

        Examples
        --------
        Successful check
        >>> value = r.check_mutable_mapping("my mut mapping", {})
        >>> value
        {}

        Successful check
        >>> from typing import Optional
        >>> value = r.check_mutable_mapping("my mut mapping", {"a": 1}, keys_of=str, values_of=int)
        >>> value
        {"a": 1}

        Unsuccessful check
        >>> value = r.check_mutable_mapping("my mut mapping?", [])
        MutableMappingException: Error in param: name got value [] is not of type Mapping.

        Unsuccessful check
        >>> value = r.check_mutable_mapping("my mut mapping of strings?", {1: 2}, keys_of=str)
        MutableMappingOfException: Error in param: name got value {1: 2} is not of type str.
        """
        if not isinstance(value, MutableMapping):
            return self._error(MutableMappingException(name, value, description))

        value = self.check_mapping(
            name,
            value,
            keys_of=keys_of,
            values_of=values_of,
            description=description,
        )

        return value

    @overload
    def check_opt_mutable_mapping(
        self,
        name: str,
        value: Any,
        *,
        keys_of: Type[KT] = ...,
        values_of: Type[VT] = ...,
        default_mutable_mapping: Callable[[], MutableMapping[KT, VT]] = lambda: {},
        description: Optional[str] = None,
    ) -> MutableMapping[KT, VT]:
        ...

    @overload
    def check_opt_mutable_mapping(
        self,
        name: str,
        value: Any,
        *,
        keys_of: Type[KT] = ...,
        values_of: Type[VT] = ...,
        default_mutable_mapping: Callable[
            [],
            MutableMapping[KT, VT] | None,
        ] = lambda: None,
        description: Optional[str] = None,
    ) -> MutableMapping[KT, VT] | None:
        ...

    def check_opt_mutable_mapping(
        self,
        name: str,
        value: Any,
        *,
        keys_of: Type[KT] = Any,
        values_of: Type[VT] = Any,
        default_mutable_mapping: Callable[
            [],
            MutableMapping[KT, VT] | None,
        ] = lambda: {},
        description: Optional[str] = None,
    ) -> MutableMapping[KT, VT] | None:
        """Check whether a value is a MutableMapping or None and optionally type check keys and values of the mapping

        Parameters
        ----------
        name : str
            Name of the variable
        value : Any
            Value to test being a MutableMapping
        keys_of : Type[KT]
            Type of the keys of the mapping to check
        values_of : Type[VT]
            Type of the values of the mapping to check
        default_mutable_mapping: Callable[[], MutableMapping[KT, VT] | None]
            Default value to use if value is None
        description : Optional[str]
            Additional comments to add

        Raises
        ------
        MutableMappingException
            If the value is not a MutableMapping
        MutableMappingOfException
            If the elements in the value are not of type T

        Returns
        -------
        check_mutable_mapping : MutableMapping[KT, VT] | None
            Input value as a mutable mapping, otherwise the default value

        Examples
        --------
        Successful check
        >>> value = r.check_mutable_mapping("my mut mapping", {})
        >>> value
        {}

        Successful check
        >>> value = r.check_mutable_mapping("my mut mapping", None)
        >>> value
        {}

        Successful check
        >>> from typing import Optional
        >>> value = r.check_mutable_mapping("my mut mapping", {"a": 1}, keys_of=str, values_of=int)
        >>> value
        {"a": 1}

        Unsuccessful check
        >>> value = r.check_mutable_mapping("my mut mapping?", [])
        MutableMappingException: Error in param: name got value [] is not of type Mapping.

        Unsuccessful check
        >>> value = r.check_mutable_mapping("my mut mapping of strings?", {1: 2}, keys_of=str)
        MutableMappingOfException: Error in param: name got value {1: 2} is not of type str.
        """
        if value is None:
            return default_mutable_mapping()

        value = self.check_opt_mapping(
            name,
            value,
            keys_of=keys_of,
            values_of=values_of,
            description=description,
        )

        return value

    # this isn't really a property, just so it's easier to call
    @property
    def check_all(self):
        """
        Examples
        --------
        Successful check
        >>> with r.check_all:
        >>>     val_a = r.check_int("my int", 1)
        >>>     val_b = r.check_int("my int", 2)
        >>> print(val_a, val_b)
        1, 2

        Unsuccessful check
        >>> with r.check_all:
        >>>     val_a = r.check_int("my int", 1)
        >>>     val_b = r.check_int("my int", 2)
        Two exceptions
        """
        from rcheck.check_all import CheckAll

        self._enable_suppress_and_record()
        return CheckAll(check_instance=self)


# r = Check(suppress_and_record=False)

# # seq = r.check_opt_sequence("my seq", [])

# # my_sq = r.check_sequence("my seq", [None, [1, "hello",]], of=Optional[Sequence[Union[int, str]]])
# # print(my_sq)

# with r.check_all:
#     a = r.check_str("str_a", 1.2, description="My first string")
#     b = r.check_int("str_b", "b", description="My second string")
#     c = r.check_sequence("my sq", 1)

# print(a, b)
