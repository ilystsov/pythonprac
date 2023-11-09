from math import sqrt

class InvalidInput(Exception):
    def __str__(self):
        return 'Invalid input'
    pass


class BadTriangle(Exception):
    def __str__(self):
        return 'Not a triangle'
    pass


def triangleSquare(s):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(s)
    except Exception:
        raise InvalidInput
    if not all((isinstance(coord, (int, float)) for coord in (x1,x2,x3,y1,y2,y3))):
        raise BadTriangle
    a = sqrt((x2 - x3)**2 + (y2 - y3)**2)
    b = sqrt((x1 - x3)**2 + (y1 - y3)**2)
    c = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    side1, side2, side3 = sorted([a, b, c])
    if not ((side1 > 0 and side2 > 0 and side3 > 0) and (side3 < side1 + side2)):
        raise BadTriangle
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

while True:
    s = input()
    try:
        area = triangleSquare(s)
    except InvalidInput as e:
        print(e)
    except BadTriangle as e:
        print(e)
    else:
        print(f'{area:.2f}')
        break 

import sys
exec(sys.stdin.read())
