from __future__ import annotations
from typing import Callable, TypeVar, Generic, cast, ParamSpec
from pythonix.result.errors import IsNoneError, ExpectError, UnwrapError
from functools import wraps

T = TypeVar("T")
U = TypeVar("U")
E = TypeVar("E", bound="Exception")
F = TypeVar("F", bound="Exception")
Params = ParamSpec("Params")


class Result(Generic[T, E]):
    _val: T
    _err: E
    _ok: bool

    def __init__(self):
        ...

    @classmethod
    def Ok(cls, val: T) -> Result[T, E]:
        if isinstance(val, Exception):
            raise TypeError(
                f"Expected value to not be of type or subtype of Exception. Found {type(val)}."
            )
        cls._ok = True
        cls._val = val
        return cast(Result[T, E], cls())

    @classmethod
    def Err(cls, err: E) -> Result[T, E]:
        if not isinstance(err, Exception):
            raise TypeError(
                f"Expected err value to be of type or subtype of Exception. Found {type(err)}."
            )
        cls._ok = False
        cls._err = err
        return cast(Result[T, E], cls())

    @classmethod
    def Some(cls, val: T) -> Result[T, IsNoneError]:
        if val is None:
            return Result.Nil()
        cls._val = val
        cls._ok = True
        return cast(Result[T, IsNoneError], cls())

    @classmethod
    def Nil(cls) -> Result[T, IsNoneError]:
        cls._ok = False
        cls._err = IsNoneError("Found a None when expecting Some")
        return cast(Result[T, IsNoneError], cls())

    def is_ok(self) -> bool:
        """
        Validates that a ResultKind object is in an Ok state
        """
        return self._ok

    def is_err(self) -> bool:
        return not self._ok

    def is_ok_and(self, predicate: Callable[[T], bool]) -> bool:
        return self.is_ok() and predicate(self._val)

    def is_err_and(self, predicate: Callable[[E], bool]) -> bool:
        return not self.is_err() and predicate(self._err)

    def unwrap(self) -> T:
        """
        If Ok then returns wrapped value, else panics with wrapped err
        """
        if self.is_err():
            raise self._err
        return self._val

    def unwrap_or(self, or_val: T) -> T:
        if self.is_err():
            return or_val
        return self._val

    def unwrap_or_else(self, or_else_func: Callable[[], T]) -> T:
        if self.is_err():
            return or_else_func()
        return self._val

    def unwrap_err(self) -> E:
        if self.is_ok():
            raise UnwrapError()
        return self._err

    def expect(self, err_msg: str) -> T:
        if self.is_err():
            raise ExpectError(err_msg)
        return self._val

    def expect_err(self, err_msg: str) -> E:
        if self.is_ok():
            raise ExpectError(err_msg)
        return self._err

    def ok(self) -> Result[T, IsNoneError]:
        if self.is_err():
            return self.Nil()
        return self.Some(self._val)

    def err(self) -> Result[E, IsNoneError]:
        if self.is_ok():
            return Result.Nil()
        return Result.Some(self._err)

    def mapme(self, op: Callable[[T], U]) -> Result[U, E]:
        if self.is_err():
            return Result.Err(self._err)
        return Result.Ok(op(self._val))

    def mapme_or(self, default: U, op: Callable[[T], U]) -> Result[U, E]:
        if self.is_err():
            return Result.Ok(default)
        return Result.Ok(op(self._val))

    def mapme_or_else(
        self, default: Callable[[E], U], op: Callable[[T], U]
    ) -> Result[U, E]:
        if self.is_err():
            return Result.Ok(default(self._err))
        return Result.Ok(op(self._val))

    def mapme_err(self, op: Callable[[E], F]) -> Result[T, F]:
        if self.is_ok():
            return Result.Ok(self._val)
        return Result.Err(op(self._err))

    def and_res(self, comp_res: Result[U, E]) -> Result[U, E]:
        if self.is_err():
            return Result.Err(self._err)
        return comp_res

    def and_then(self, op: Callable[[T], Result[U, E]]) -> Result[U, E]:
        if self.is_err():
            return Result.Err(self._err)
        return op(self._val)

    def or_res(self, comp_res: Result[T, F]) -> Result[T, F]:
        if self.is_ok():
            return Result.Ok(self._val)
        return comp_res

    def or_else(self, op: Callable[[E], Result[T, F]]) -> Result[T, F]:
        if self.is_ok():
            return Result.Ok(self._val)
        return op(self._err)
