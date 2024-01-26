import operator as op
from pythonix.suffix_types import EagerSuffix, DelayedSuffix
from pythonix.result.decorators import safe
from pythonix.result.containers import Result
from typing import Any, TypeVar, SupportsAbs, SupportsIndex

T_co = TypeVar("T_co", covariant=True)


@EagerSuffix
def index(val: T_co) -> int:
    return op.index(val)


@EagerSuffix
def inv(val: T_co) -> T_co:
    return op.inv(val)


@EagerSuffix
def invert(val: T_co) -> T_co:
    return op.invert(val)


@EagerSuffix
def neg(val: T_co) -> T_co:
    '''
    Same as `-a`
    '''
    return op.neg(val)


@EagerSuffix
def pos(val: T_co) -> T_co:
    '''
    Same as `+a`
    '''
    return op.pos(val)


@EagerSuffix
def abs_(val: SupportsAbs[T_co]) -> T_co:
    '''
    Same as `abs(a)`
    '''
    return op.abs(val)


@EagerSuffix
def index(val: SupportsIndex) -> int:
    '''
    Same as `a.__index__()`
    '''
    return op.index(val)


@DelayedSuffix
def add(left_val: Any, val: Any) -> Any:
    '''
    Same as `a` + `b`.
    '''
    return op.add(left_val, val)


@DelayedSuffix
def and_(left_val: Any, val: Any) -> bool:
    return op.and_(left_val, val)


@DelayedSuffix
def floordiv(left_val: Any, val: Any) -> Result[Any, ZeroDivisionError]:
    return safe(op.floordiv, ZeroDivisionError)(left_val, val)


@DelayedSuffix
def lshift(left_val: Any, val: Any) -> Any:
    return op.lshift(left_val, val)


@DelayedSuffix
def rshift(left_val: Any, val: Any) -> Any:
    return op.rshift(left_val, val)


@DelayedSuffix
def mod(left_val: Any, val: Any) -> Any:
    return op.mod(left_val, val)


@DelayedSuffix
def mul(left_val: Any, val: Any) -> Any:
    return op.mul(left_val, val)


@DelayedSuffix
def ixor(left_val: Any, val: Any) -> Any:
    return op.ixor(left_val, val)


@DelayedSuffix
def itruediv(left_val: Any, val: Any) -> Any:
    return safe(itruediv, ZeroDivisionError)(left_val, val)


@DelayedSuffix
def isub(left_val: Any, val: Any) -> Any:
    return op.isub(left_val, val)


@DelayedSuffix
def irshift(left_val: Any, val: Any) -> Any:
    return op.irshift(left_val, val)


@DelayedSuffix
def ipow(left_val: Any, val: Any) -> Any:
    return op.ipow(left_val, val)


@DelayedSuffix
def ior(left_val: Any, val: Any) -> Any:
    return op.ior(left_val, val)


@DelayedSuffix
def imatmul(left_val: Any, val: Any) -> Any:
    return op.imatmul(left_val, val)


@DelayedSuffix
def imul(left_val: Any, val: Any) -> Any:
    return op.imul(left_val, val)


@DelayedSuffix
def imod(left_val: Any, val: Any) -> Any:
    return op.imod(left_val, val)


@DelayedSuffix
def ilshift(left_val: Any, val: Any) -> Any:
    return op.ilshift(left_val, val)


@DelayedSuffix
def ifloordiv(left_val: Any, val: Any) -> Any:
    return safe(op.ifloordiv, ZeroDivisionError)(left_val, val)


@DelayedSuffix
def iand(left_val: Any, val: Any) -> Any:
    return op.iand(left_val, val)


@DelayedSuffix
def iadd(left_val: Any, val: Any) -> Any:
    return op.iadd(left_val, val)


@DelayedSuffix
def xor(left_val: Any, val: Any) -> Any:
    return op.xor(left_val, val)


@DelayedSuffix
def mod(left_val: Any, val: Any) -> Any:
    return op.mod(left_val, val)


@DelayedSuffix
def truediv(left_val: Any, val: Any) -> Result[Any, ZeroDivisionError]:
    return safe(op.truediv, ZeroDivisionError)(left_val, val)


@DelayedSuffix
def sub(left_val: Any, val: Any) -> Any:
    return op.sub(left_val, val)


@DelayedSuffix
def pow_(left_val: Any, val: Any) -> Any:
    return op.pow_(left_val, val)


@DelayedSuffix
def or_(left_val: Any, val: Any) -> Any:
    return op.or_(left_val, val)


@DelayedSuffix
def matmul(left_val: Any, val: Any) -> Any:
    return op.matmul(left_val, val)
