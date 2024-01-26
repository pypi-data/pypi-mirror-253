from pythonix.suffix_types import DelayedSuffix
import itertools as i

product = DelayedSuffix(i.product)
permutations = DelayedSuffix(i.permutations)
combinations = DelayedSuffix(i.combinations)
combinations_with_replacement = DelayedSuffix(i.combinations_with_replacement)
