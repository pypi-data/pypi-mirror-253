from types import TracebackType
from typing import Optional, Type

from rcheck.check import Check


class CheckAll:
    def __init__(self, *, check_instance: Check):
        self.check = check_instance

    def __enter__(self) -> Check:
        self.check._enable_suppress_and_record()  # type: ignore
        return self.check

    def __exit__(
        self,
        exc_type: Optional[Type[Exception]],
        exc_value: Optional[Exception],
        exc_tb: Optional[TracebackType],
    ):
        # needs to come before this value is deleted
        records = self.check._records  # type: ignore

        if not self.check._suppress_and_record_original:  # type: ignore
            self.check._disable_suppress_and_record()  # type: ignore

        # non rcheck errors
        if exc_type is not None:
            return

        if len(records) == 0:
            return

        if len(records) == 1:
            raise records[0]

        raise ExceptionGroup("Multiple rcheck validation errors occured", records)


def check_all():
    """Check multiple checks at once in a context

    Usage (need to replace all `r.check_*` with `checker.check_*` or whatever variable name you decide):

    Parameters
    ----------

    Returns
    -------
    check_all : CheckAll
        Instance of a CheckAll class

    Examples
    --------

    Basic Example
    >>> name = "rcheck"
    >>> age = 1
    >>> with check_all() as check:
    >>>     name = check.check_str("name", name)
    >>>     name = check.check_int("age", age)
    >>> print(name, age)
    rcheck 1
    """
    return CheckAll(check_instance=Check(suppress_and_record=True))
