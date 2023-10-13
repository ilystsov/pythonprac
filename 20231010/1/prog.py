from fractions import Fraction
def check(s, w, *data):
    deg_a = int(data[0])
    coefs_a = []
    coefs_b = []
    for i in range(1, 1 + deg_a + 1):
        coefs_a.append(Fraction(data[i]))  
    deg_b = int(data[i + 1])
    i += 2
    for j in range(deg_b + 1):
        coefs_b.append(Fraction(data[i + j]))
    res_a = 0
    res_b = 0
    for i in range(deg_a + 1):
        res_a += coefs_a[i] * s**(deg_a - i)

    for i in range(deg_b + 1):
        res_b += coefs_b[i] * s**(deg_b - i)

    return res_a == w * res_b

data = input().split(',')
s = Fraction(data[0])
w = Fraction(data[1])
print(check(s, w, *data[2:]))