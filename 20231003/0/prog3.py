def f(n):
    if n == 0:
        return
    f(n - 1)
f(998)