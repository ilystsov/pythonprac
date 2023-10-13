from math import *
def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A
w, h, a, b, func = input().split()
w = int(w)
h = int(h)
a = float(a)
b = float(b)
scr = [[' '] * w for i in range(h)]

func_min = float('inf')
func_max = float('-inf')
for i in range(w):
    x = scale(0, w - 1, a, b, i)
    y = (lambda x: eval(func))(x)
    func_min = min(func_min, y)
    func_max = max(func_max, y)

x = scale(0, w - 1, a, b, 0)
y = (lambda x: eval(func))(x)
y = int(scale(func_min, func_max, h - 1, 0, y))
scr[y][0] = '*'
prev_y = y 
for i in range(1, w):
    x = scale(0, w - 1, a, b, i)
    y = (lambda x: eval(func))(x)
    y = int(scale(func_min, func_max, h - 1, 0, y))
    scr[y][i] = '*'
    if abs(prev_y - y) > 1:
        for k in range(min(y, prev_y) + 1, max(y, prev_y)):
            scr[k][i] = '*'
    prev_y = y
if abs(prev_y - y) > 1:
    for k in range(min(y, prev_y) + 1, max(y, prev_y)):
        scr[k][i] = '*'
print("\n".join("".join(s) for s in scr))

