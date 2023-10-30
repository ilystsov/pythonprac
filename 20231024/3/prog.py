from itertools import *
print(*sorted(''.join(el) for el in filter(lambda x: ''.join(x).count('TOR') == 2, product('TOR', repeat=int(input())))), sep=', ')
