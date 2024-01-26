from typing import Callable, Self, TypeVar, Generic, ParamSpec
from functools import wraps

T = TypeVar("T")
U = TypeVar("U")
E = TypeVar("E", bound="Exception")
F = TypeVar("F", bound="Exception")
Params = ParamSpec("Params")


class EagerSuffix(Generic[Params, U]):
    """
    Decorator class used to change a function to an suffix function
    whose first argument is passed in via the `|` operator.
    See below for usage examples.
    ```python
    @Suffix
    def add_one(x: int) -> int:
        return x + 1
    add_two = Suffix(lambda x: x + 1)
    assert 3 == 0 | add_one | add_two
    assert 3 == add_one(2)
    ```
    """

    def __init__(self, func: Callable[Params, U]):
        @wraps(func)
        def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> U:
            return func(*args, **kwargs)

        self.wrapped = wrapper

    def __ror__(self, *args: Params.args, **kwargs: Params.kwargs) -> U:
        return self.wrapped(*args, **kwargs)

    def __call__(self, *args: Params.args, **kwargs: Params.kwargs) -> U:
        return self.wrapped(*args, **kwargs)


class DelayedSuffix(Generic[Params, U]):
    """
    Changes a function to a delayed suffix whose first argument pipes in from the left
    via a `|` and the other arguments are added by calling the function. Piping in from the
    left automatically calls `run` on the function. Otherwise, you can call `run` to execute
    the function after populating its arguments.
    #### Example
    ```python
    @DelayedSuffix
    def add(x: int, y: int) -> int:
        return x + y

    assert 3 == 1 | add(y=2)
    assert 3 == add(1, 2).run()
    ```
    """

    def __init__(self, func: Callable[Params, U]):
        @wraps(func)
        def wrapper(*args: Params.args, **kwargs: Params.kwargs) -> U:
            return func(*args, **kwargs)

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
