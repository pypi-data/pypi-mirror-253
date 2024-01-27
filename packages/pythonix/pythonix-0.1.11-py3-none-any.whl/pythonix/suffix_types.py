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
        try:
            if func.__doc__ is not None:
                func.__doc__ = self.__doc__ + func.__doc__
        except AttributeError as e:
            ...
        except TypeError as e:
            ...
        update_wrapper(self, func)
        self.wrapped = wrapper

    def __ror__(self, *args: Params.args, **kwargs: Params.kwargs) -> U:
        return self.wrapped(*args, **kwargs)

    def __call__(self, *args: Params.args, **kwargs: Params.kwargs) -> U:
        return self.wrapped(*args, **kwargs)


class DelayedSuffix(Generic[Params, U]):
    '''
    Delayed suffix whose call only populates the function. To execute pass in the first
    argument using the `|` operator or use `run` method.
    '''
    def __init__(self, func: Callable[Params, U]):
        def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> U:
            return func(*args, **kwargs)

        try:
            if func.__doc__ is not None:
                func.__doc__ = self.__doc__ + func.__doc__
        except AttributeError as e:
            ...
        except TypeError as e:
            ...
        update_wrapper(self, func)
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
