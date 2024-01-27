from typing import Callable, Self, TypeVar, Generic, ParamSpec
from functools import update_wrapper

T = TypeVar("T")
U = TypeVar("U")
E = TypeVar("E", bound="Exception")
F = TypeVar("F", bound="Exception")
Params = ParamSpec("Params")


class EagerSuffix(Generic[Params, U]):
    """
    Eager suffix function that can receive its argument normally
    or via the `|` operator.
    """

    def __init__(self, func: Callable[Params, U]):
        def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> U:
            return func(*args, **kwargs)

        update_wrapper(self, func)
        if func.__doc__ is not None:
            self.__doc__ += func.__doc__
        self.wrapped = wrapper

    def __ror__(self, *args: Params.args, **kwargs: Params.kwargs) -> U:
        return self.wrapped(*args, **kwargs)

    def __call__(self, *args: Params.args, **kwargs: Params.kwargs) -> U:
        return self.wrapped(*args, **kwargs)


class DelayedSuffix(Generic[Params, U]):
    def __init__(self, func: Callable[Params, U]):
        def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> U:
            return func(*args, **kwargs)

        update_wrapper(self, func)
        if func.__doc__ is not None:
            self.__doc__ += func.__doc__
        self.wrapped = wrapper
        self._args = tuple()  # type: ignore
        self._kwargs = dict()  # type: ignore

    def __ror__(self, other: T) -> U:
        if len(self._args) <= 1:
            self._args = tuple([other])
        else:
            self._args = tuple([other] + list(self._args)[1:])
        return self.run()

    def __call__(self, *args: Params.args, **kwargs: Params.kwargs) -> Self:
        self._args = args
        self._kwargs = kwargs
        return self

    def run(self) -> U:
        return self.wrapped(*self._args, **self._kwargs)
