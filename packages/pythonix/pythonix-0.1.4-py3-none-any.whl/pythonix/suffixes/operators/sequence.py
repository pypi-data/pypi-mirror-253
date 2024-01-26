import operator as op
from pythonix.suffix_types import DelayedSuffix
from pythonix.result.decorators import safe
from pythonix.result.containers import Result
from typing import (
    Any,
    TypeVar,
    Sequence,
    Iterable,
    MutableMapping,
    MutableSequence,
    SupportsIndex,
)

T = TypeVar("T")
K = TypeVar("K")


@DelayedSuffix
def concat(left_val: Sequence[T], val: Sequence[T]) -> Sequence[T]:
    return op.concat(left_val, val)


@DelayedSuffix
def iconcat(left_val: Any, val: Any) -> Any:
    return op.iconcat(left_val, val)


@DelayedSuffix
def index_of(left_val: Iterable[T], val: T) -> Result[int, ValueError]:
    return safe(op.indexOf, ValueError)(left_val, val)


@DelayedSuffix
def length_hint(obj: object, default: int = 0) -> int:
    return op.length_hint(obj, default)


@DelayedSuffix
def count_of(left_val: Iterable[object], val: object) -> int:
    return op.countOf(left_val, val)


@DelayedSuffix
def seq_delitem(
    left_val: MutableSequence[T], val: SupportsIndex | slice
) -> Result[MutableSequence[T], LookupError]:
    return safe(op.delitem, LookupError)(left_val, val).and_res(Result.Ok(left_val))


@DelayedSuffix
def mapping_delitem(
    left_val: MutableMapping[K, T], val: K
) -> Result[MutableMapping[K, T], LookupError]:
    return safe(op.delitem, LookupError)(left_val, val).and_res(Result.Ok(left_val))


@DelayedSuffix
def getitem(
    left_val: Sequence[T] | MutableMapping[K, T], val: slice | K
) -> Result[T, LookupError]:
    return safe(op.getitem, LookupError)(left_val, val)


@DelayedSuffix
def seq_setitem(
    left_val: MutableSequence[T], val: SupportsIndex | slice
) -> Result[MutableSequence[T], LookupError]:
    return safe(op.setitem, LookupError)(left_val, val).and_res(Result.Ok(left_val))


@DelayedSuffix
def mapping_setitem(
    left_val: MutableMapping[K, T], val: K
) -> Result[MutableMapping[K, T], LookupError]:
    return safe(op.setitem, LookupError)(left_val, val).and_res(Result.Ok(left_val))
