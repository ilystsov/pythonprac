import itertools
def repeater(seq, n):
    for el in seq:
        yield from itertools.repeat(el, n)