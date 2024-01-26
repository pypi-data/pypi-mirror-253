from __future__ import annotations
import operator as op
from pythonix.suffix_types import EagerSuffix, DelayedSuffix
from typing import Any, Tuple, TypeAlias
from types import UnionType

_ClassInfo: TypeAlias = type | UnionType | Tuple[type, ...]


@EagerSuffix
def not_(val: object) -> bool:
    return op.not_(val)


@EagerSuffix
def truth(val: object) -> bool:
    return op.truth(val)


@DelayedSuffix
def is_(left_val: object, val: object) -> bool:
    return op.is_(left_val, val)


@DelayedSuffix
def is_not(left_val: object, val: object) -> bool:
    return op.is_not(left_val, val)


@DelayedSuffix
def is_instance(obj: object, class_info: _ClassInfo) -> bool:
    return isinstance()
