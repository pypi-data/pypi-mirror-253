from typing import Callable, Self, TypeVar, Generic, ParamSpec
from functools import update_wrapper

T = TypeVar("T")
U = TypeVar("U")
E = TypeVar("E", bound="Exception")
F = TypeVar("F", bound="Exception")
Params = ParamSpec("Params")


class EagerSuffix(Generic[Params, U]):
    def __init__(self, func: Callable[Params, U]):
        doc_addendum: str = (
            "\n"
            "This function is an eager suffix. You can call the function normally "
            "or you can pass its sole argument via the `|` operator."
            "#### Example"
            "```python"
            "assert 1 | add_one == 2"
            "assert add_one(1) == 2"
            "```"
        )
        try:
            if func.__doc__ is not None:
                func.__doc__ = func.__doc__ + doc_addendum
            else:
                func.__doc__ = doc_addendum
        except TypeError as e:
            ...
        except AttributeError as e:
            ...

        update_wrapper(self, func)
        def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> U:
            return func(*args, **kwargs)
        
        self.__doc__ = self.__doc__ + func.__doc__

        self.wrapped = wrapper

    def __ror__(self, *args: Params.args, **kwargs: Params.kwargs) -> U:
        return self.wrapped(*args, **kwargs)

    def __call__(self, *args: Params.args, **kwargs: Params.kwargs) -> U:
        return self.wrapped(*args, **kwargs)


class DelayedSuffix(Generic[Params, U]):
    def __init__(self, func: Callable[Params, U]):
        doc_addendum: str = (
            "\n"
            "This function is a delayed suffix, which means it has some additional rules."
            "1. To run the function you must call the `run()` method after populating its arguments"
            "2. Or, the first argument of the function is populated from the left '|', which calls `run`"
            "If that is the case then you must use keyword arguments"
            "### Example"
            "```python"
            "assert 1 | add(val=5) | mul(val=3) == 15"
            "assert mul(add(1, 5).run(), 3).run() == 15"
            "```"
        )
        try:
            if func.__doc__ is not None:
                func.__doc__ = func.__doc__ + doc_addendum
            else:
                func.__doc__ = doc_addendum
        except TypeError as e:
            ...
        except AttributeError as e:
            ...

        update_wrapper(self, func)
        def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> U:
            return func(*args, **kwargs)

        self.__doc__ = self.__doc__ + func.__doc__

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
