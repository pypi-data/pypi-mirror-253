from pythonix.suffix_types import EagerSuffix, DelayedSuffix

slice_it = DelayedSuffix(slice)
into_iter = EagerSuffix(iter)
into_aiter = EagerSuffix(aiter)
all_are_true = EagerSuffix(all)
any_are_true = EagerSuffix(any)
zip_it = DelayedSuffix(zip)
reverse_it = EagerSuffix(reversed)
next_item = EagerSuffix(next)
anext_item = EagerSuffix(anext)
enumerate_it = DelayedSuffix(enumerate)
sort_it = DelayedSuffix(sorted)
