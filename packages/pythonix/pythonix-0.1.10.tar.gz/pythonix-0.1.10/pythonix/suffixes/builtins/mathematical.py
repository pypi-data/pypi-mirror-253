from pythonix.suffix_types import DelayedSuffix
from pythonix.result.decorators import safe

min_ = DelayedSuffix(min)
max_ = DelayedSuffix(max)
round_ = DelayedSuffix(round)
divmod_ = DelayedSuffix(safe(divmod, ZeroDivisionError))
sum_ = DelayedSuffix(sum)
