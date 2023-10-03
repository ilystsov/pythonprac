def F(f, g):
    def h(x):
        return f(x) + g(x)
    return h

def f1(x):
    return x * 3

def f2(x):
    return x / 3

h = F(f1, f2)
print(h(10))