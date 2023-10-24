import random
import itertools
def ffn(n, seq):
    yield from itertools.filterfalse(lambda x: x % n, seq)


print(list(ffn(5, (random.randrange(50) for i in range(100)))))