from math import *
def Calc(s, t, u):
    s = eval('lambda x:' + s)
    t = eval('lambda x:' + t)
    u = eval('lambda x, y:' + u)
    return lambda x: u(s(x), t(x))
     
s, t, u = eval(input())
x = eval(input())
print((Calc(s, t, u))(x))