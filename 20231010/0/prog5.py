from math import sin
def scale(a, b, A, B, x):
    return (x - a)* (B - A) / (b - a) + A

a, b = -20, 20


scr = [['.'] * 60 for i in range(20)] 

print(len(scr), len(scr[0]))

A, B = 0, 20
for i in range(60):
    x = scale(0, 59, A, B, i)
    y = (sin(x))
    y = int(scale(-1, 1, 19, 0, y))
    print(int(x))
    scr[int(x)][y] = '*'


print('\n'.join([''.join(s) for s in scr]))
