import decimal
def esum(n, one):
    mul = type(one)(1)
    sum = type(one)(1)
    prev = type(one)(1)
    for i in range(1, n):
        mul *= i
        sum += 1 / mul
        if sum == prev:
            break
        prev = sum
    return sum

decimal.getcontext().prec = 100
print(esum(999999999999999999999999, decimal.Decimal('1')))
