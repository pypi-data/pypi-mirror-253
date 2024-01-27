from pythonix.suffix_types import EagerSuffix, DelayedSuffix
import itertools as i
import functools as f
from typing import TypeVar, Iterable, Callable, Tuple, Any, Iterator

T = TypeVar("T")
S = TypeVar("S")
U = TypeVar("U")


@DelayedSuffix
def reduce(
    iterable: Iterable[T], op: Callable[[T, S], U], initial: T | None = None
) -> U:
    return f.reduce(op, iterable, initial)


@DelayedSuffix
def map_it(iterable: Iterable[T], op: Callable[[T, S], U]):
    return map(op, iterable)


@DelayedSuffix
def dropwhile(iterable: Iterable[T], predicate: Callable[[T], bool]):
    return i.dropwhile(predicate, iterable)


@DelayedSuffix
def filter_it(iterable: Iterable[T], predicate: Callable[[T], bool]):
    return filter(predicate, iterable)


@DelayedSuffix
def filterfalse_it(iterable: Iterable[T], predicate: Callable[[T], bool]):
    return i.filterfalse(predicate, iterable)


@DelayedSuffix
def starmap(iterable: Iterable[Tuple[T, ...]], op: Callable[[Tuple[T, ...]], U]):
    return i.starmap(op, iterable)


@DelayedSuffix
def takewhile(iterable: Iterable[T], predicate: Callable[[T], bool]):
    return i.takewhile(predicate, iterable)


@EagerSuffix
def chain_from_iterable(iterable: Iterable[Iterable[T]]):
    return i.chain.from_iterable(iterable)


@DelayedSuffix
def accumulate(
    iterable: Iterable[S],
    func: Callable[[T, S], S] | None = None,
    initial: T | None = None,
):
    return i.accumulate(iterable, func, initial)


@DelayedSuffix
def batched(iterable: Iterable[T], n: int = 2):
    return i.batched(iterable, n)


@DelayedSuffix
def chain(*iterables: Iterable[T]):
    return i.chain(iterables)


@DelayedSuffix
def compress(data: Iterable[T], selectors: Iterable[Any]):
    return i.compress(data, selectors)


@DelayedSuffix
def groupby(iterable: Iterable[T], key: Callable[[T], U] | None = None):
    return i.groupby(iterable, key)


@DelayedSuffix
def islice(
    iterable: Iterable[T],
    start: int | None = 0,
    stop: int | None = None,
    step: int | None = 1,
):
    return i.islice(iterable, start, stop, step)


@DelayedSuffix
def pairwise(iterable: Iterable[T]):
    return i.pairwise(iterable)


@DelayedSuffix
def tee(iterable: Iterable[T], n: int = 2):
    return i.tee(iterable, n)


@DelayedSuffix
def zip_longest(*iterables: Iterable[T], fill_value: T | None = None):
    return i.zip_longest(*iterables, fill_value=fill_value)
