from math import inf
def div_ab(a, b):
    return a/b

while True:
    a, b = map(int, input().split())
    try:
        print(div_ab(a, b))
    except ZeroDivisionError:
        print(inf)