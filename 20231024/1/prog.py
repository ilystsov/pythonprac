def fib(m, n):
    pprev = 0
    prev = 1
    cur = 1
    for i in range(m):
        cur = prev + pprev
        pprev = prev
        prev = cur

    for i in range(n):
        yield cur 
        cur = prev + pprev
        pprev = prev
        prev = cur

import sys
exec(sys.stdin.read())