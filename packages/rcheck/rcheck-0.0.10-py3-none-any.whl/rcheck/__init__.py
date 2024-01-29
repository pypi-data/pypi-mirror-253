from rcheck.check import Check
from rcheck.check_all import check_all

r = Check(suppress_and_record=False)

__all__ = ("Check", "check_all", "r")
