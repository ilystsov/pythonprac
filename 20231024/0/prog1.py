def fgen():
    i = 1
    sum = 0
    while True:
        sum += 1 / i / i
        yield sum
        i += 1
    
gen = fgen()
for i in gen:
    print(i)