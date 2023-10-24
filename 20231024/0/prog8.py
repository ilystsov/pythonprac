from itertools import product 
for i in product('abcdefgh', range(1, 9)):
    print(*i)