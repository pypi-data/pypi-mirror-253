from typing import Callable, TypeVar, ParamSpec
from pythonix.result.errors import IsNoneError
from functools import wraps
from pythonix.result.containers import Result

U = TypeVar("U")
E = TypeVar("E", bound="Exception")
Params = ParamSpec("Params")


def safe(
    f: Callable[Params, U], err_type: type[E] = Exception  # type: ignore
) -> Callable[Params, Result[U, E]]:
    @wraps(f)
    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> Result[U, E]:
        try:
            return Result.Ok(f(*args, **kwargs))
        except err_type as e:
            return Result.Err(e)

    return wrapper


def some(f: Callable[Params, U]) -> Callable[Params, Result[U, IsNoneError]]:
    @wraps(f)
    def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> Result[U, IsNoneError]:
        try:
            return Result.Some(f(*args, **kwargs))
        except Exception as err:
            return Result.Nil()

    return wrapper
