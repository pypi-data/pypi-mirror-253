from pythonix.suffix_types import EagerSuffix, DelayedSuffix
import itertools as i
from typing import (
    SupportsFloat,
    SupportsComplex,
    SupportsInt,
    SupportsIndex,
    TypeAlias,
    Iterable,
    TypeVar,
)

Number: TypeAlias = SupportsFloat | SupportsComplex | SupportsInt | SupportsIndex
T = TypeVar("T")


@DelayedSuffix
def count(start: Number, step: Number = 1) -> Number:
    return i.count(start, step)


@EagerSuffix
def cycle(iterable: Iterable[T]) -> T:
    return i.cycle(iterable)


@DelayedSuffix
def repeat(obj: T, times: int | None = None) -> T:
    return i.repeat(obj, times)
