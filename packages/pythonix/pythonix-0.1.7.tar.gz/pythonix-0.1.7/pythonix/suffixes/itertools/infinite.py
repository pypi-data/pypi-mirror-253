from pythonix.suffix_types import EagerSuffix, DelayedSuffix
import itertools as i

count = DelayedSuffix(i.count)
cycle = EagerSuffix(i.cycle)
repeat = DelayedSuffix(i.repeat)
