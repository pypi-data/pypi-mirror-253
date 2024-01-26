from operator import call as opcall
from pythonix.suffix_types import DelayedSuffix
from pythonix.result.decorators import safe, some
from pythonix.result.containers import Result
from pythonix.result.errors import IsNoneError
from typing import ParamSpec, TypeVar, Any

_P = ParamSpec("_P")
U = TypeVar("U")


@DelayedSuffix
def call(obj: object, *args: _P.args, **kwargs: _P.kwargs) -> U:
    return safe(opcall, TypeError)(obj, **args, **kwargs)


@DelayedSuffix
def get_attr(
    obj: object, name: str, default: Any | None = None
) -> Result[Any, IsNoneError]:
    return some(getattr)(obj, name, default)


@DelayedSuffix
def set_attr(obj: object, name: str, value: Any) -> Result[None, AttributeError]:
    return safe(setattr, AttributeError)(obj, name, value)


@DelayedSuffix
def del_attr(obj: object, name: str) -> Result[None, AttributeError]:
    return safe(delattr, AttributeError)(obj, name)


@DelayedSuffix
def has_attr(obj: object, name: str) -> bool:
    return hasattr(obj, name)
