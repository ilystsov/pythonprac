def decorate(fun):
    def newfun(*args):
        if all(type(i) == int for i in args):
            return fun(*args)
        else:
            raise TypeError
    return newfun
@decorate
def fun(a, b, c):
    return sum((a, b, c))
print(fun(1, 2, 3))
print(fun(1, 2, 'a'))
