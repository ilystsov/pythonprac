import decimal, fractions
def multiplier(x, y, Type):
    return Type(x) * Type(y)

print(multiplier('1.2', '2.0', float))
print(multiplier('3.3', '3.0', decimal.Decimal))
print(multiplier('1/6', '2/3', fractions.Fraction))