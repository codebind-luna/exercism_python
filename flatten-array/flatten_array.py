import collections

def flatten(iterable):
    return list(compute_flatten_list(iterable))

def compute_flatten_list(iterable):
    for el in iterable:
        if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
            for sub in flatten(el):
                yield sub
        elif el is not None:
            yield el
