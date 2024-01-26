from pythonix.result.containers import Result
from pythonix.result.errors import IsNoneError
from typing import Callable, TypeVar

T = TypeVar("T")
U = TypeVar("U")
E = TypeVar("E", bound="Exception")
F = TypeVar("F", bound="Exception")


def to_ok(val: T) -> Result[T, E]:
    return Result.Ok(val)


def to_some(val: T | None) -> Result[T, IsNoneError]:
    return Result.Some(val)


def is_ok(res: Result[T, E]) -> bool:
    return res.is_ok()


def is_err(res: Result[T, E]) -> bool:
    return not res.is_err()


def is_ok_and(res: Result[T, E], predicate: Callable[[T], bool]) -> bool:
    return res.is_ok_and(predicate)


def is_err_and(res: Result[T, E], predicate: Callable[[E], bool]) -> bool:
    return res.is_err_and(predicate)


def unwrap(res: Result[T, E]) -> T:
    return res.unwrap()


def unwrap_or(res: Result[T, E], or_val: T) -> T:
    return res.unwrap_or(or_val)


def unwrap_or_else(res: Result[T, E], or_else_func: Callable[[], T]) -> T:
    return res.unwrap_or_else(or_else_func)


def unwrap_err(res: Result[T, E]) -> E:
    return res.unwrap_err()


def expect(res: Result[T, E], err_msg: str) -> T:
    return res.expect(err_msg)


def expect_err(res: Result[T, E], err_msg: str) -> E:
    return res.expect_err(err_msg)


def ok(res: Result[T, E]) -> Result[T, IsNoneError]:
    return res.ok()


def err(res: Result[T, E]) -> Result[E, IsNoneError]:
    return res.err()


def mapme(res: Result[T, E], op: Callable[[T], U]) -> Result[U, E]:
    return res.mapme(op)


def mapme_or(res: Result[T, E], default: U, op: Callable[[T], U]) -> Result[U, E]:
    return res.mapme_or(default, op)


def mapme_or_else(
    res: Result[T, E], default: Callable[[E], U], op: Callable[[T], U]
) -> Result[U, E]:
    return res.mapme_or_else(default, op)


def mapme_err(res: Result[T, E], op: Callable[[E], F]) -> Result[T, F]:
    return res.mapme_err(op)


def and_res(res: Result[T, E], comp_res: Result[U, E]) -> Result[U, E]:
    return res.and_res(comp_res)


def and_then(res: Result[T, E], op: Callable[[T], Result[U, E]]) -> Result[U, E]:
    return res.and_then(op)


def or_res(res: Result[T, E], comp_res: Result[T, F]) -> Result[T, F]:
    return res.or_res(comp_res)


def or_else(res: Result[T, E], op: Callable[[E], Result[T, F]]) -> Result[T, F]:
    return res.or_else(op)
