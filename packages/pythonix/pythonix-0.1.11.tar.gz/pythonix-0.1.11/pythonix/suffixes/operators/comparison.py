import operator as op
from pythonix.suffix_types import DelayedSuffix
from typing import Any


@DelayedSuffix
def lt(left_val: Any, val: Any) -> Any:
    return op.lt(left_val, val)


@DelayedSuffix
def le(left_val: Any, val: Any) -> Any:
    return op.le(left_val, val)


@DelayedSuffix
def eq(left_val: Any, val: Any) -> Any:
    return op.eq(left_val, val)


@DelayedSuffix
def ne(left_val: Any, val: Any) -> Any:
    return op.ne(left_val, val)


@DelayedSuffix
def ge(left_val: Any, val: Any) -> Any:
    return op.ge(left_val, val)


@DelayedSuffix
def gt(left_val: Any, val: Any) -> Any:
    return op.gt(left_val, val)
