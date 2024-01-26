from pythonix.suffix_types import EagerSuffix, DelayedSuffix
import itertools as i
import functools as f
from typing import TypeVar, Iterable, Callable, Tuple

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


accumulate = DelayedSuffix(i.accumulate)
batched = DelayedSuffix(i.batched)
chain = DelayedSuffix(i.chain)
compress = DelayedSuffix(i.compress)
groupby = DelayedSuffix(i.groupby)
islice = DelayedSuffix(i.islice)
pairwise = EagerSuffix(i.pairwise)
tee = DelayedSuffix(i.tee)
zip_longest = DelayedSuffix(i.zip_longest)
sum_it = EagerSuffix(sum)
slice_it = DelayedSuffix(slice)
into_iter = EagerSuffix(iter)
into_aiter = EagerSuffix(aiter)
all_are_true = EagerSuffix(all)
any_are_true = EagerSuffix(any)
zip_it = DelayedSuffix(zip)
reverse_it = EagerSuffix(reversed)
next_item = EagerSuffix(next)
anext_item = EagerSuffix(anext)
enumerate_it = DelayedSuffix(enumerate)
sort_it = DelayedSuffix(sorted)
