s = input()
a, b = eval(input())
print(eval(s, {'x': a, 'y': b}))
print(eval(s, {'x': b, 'y': a}))