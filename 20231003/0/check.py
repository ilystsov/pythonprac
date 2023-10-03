def a():
    global c 
    c = 123
    print(c)

c = 0
print(a(), c)