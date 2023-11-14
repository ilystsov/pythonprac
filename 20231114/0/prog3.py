def construct_decorator(type):
    def decorate(fun):
        def newfun(*args):
            if all(type(i) == type for i in args):
                return fun(*args)
            else:
                raise TypeError
        return newfun
    return decorate
    
@construct_decorator(int)
def fun(a, b, c):
    return sum((a, b, c))

@construct_decorator(str)
def isin(string, substr):
    return substr in string

print(isin('abc', 'bc'))
print(fun(1, 2, 3))
print(fun(1, 2, 'a'))