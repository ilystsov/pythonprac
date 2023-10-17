import string
from timeit import Timer
def foo(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = set(string.ascii_lowercase) - vowels
    return len(set(s) & consonants), len(set(s) & vowels)

cyc, tim = (Timer('foo("ghjklasdad")', globals=globals())).autorange()
print(cyc / tim)