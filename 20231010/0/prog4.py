from math import sin
def scale(a, b, A, B, x):
    return (x - a)* (B - A) / (b - a) + A

a, b = -20, 20

n = 30
for i in range(n):
    x = scale(a, n-1, -5, 5, i)
    y = (sin(x))
    y = int(scale(-1, 1, 0, 20, y))
    print(" "*y, '*')
