from collections import Counter, defaultdict
from timeit import Timer

def count_dict(s):
    s = s.split()
    d = defaultdict(int)
    for i in s:
        d[i] += 1
    return d

def count_counter(s):
    s = s.split()
    return Counter(s)

s = input()
cyc, tim = (Timer(f'count_dict("{s}")', globals=globals())).autorange()
print('dict:', cyc / tim)

cyc, tim = (Timer(f'count_counter("{s}")', globals=globals())).autorange()
print('counter:', cyc / tim)
