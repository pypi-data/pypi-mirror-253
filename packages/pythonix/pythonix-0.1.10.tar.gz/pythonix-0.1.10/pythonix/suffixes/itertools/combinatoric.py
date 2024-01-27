from pythonix.suffix_types import DelayedSuffix
import itertools as i
from typing import Iterable, Any, Tuple, TypeVar

T = TypeVar("T")


@DelayedSuffix
def product(*iterables: Iterable[T], repeat: int = 1) -> Tuple[T, ...]:
    return i.product(*iterables, repeat)


@DelayedSuffix
def permutations(iterable: Iterable[T], r: int | None = None) -> Tuple[T, ...]:
    return i.permutations(iterable, r)


@DelayedSuffix
def combinations(iterable: Iterable[T], r: int) -> Tuple[T, ...]:
    return i.combinations(iterable, r)


@DelayedSuffix
def combinations_with_replacement(iterable: Iterable[T], r: int) -> Tuple[T, ...]:
    return i.combinations_with_replacement(iterable, r)
