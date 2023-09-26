a = list(eval(input()))
for i in range(len(a)):
    for j in range(len(a) - i - 1):
        if (a[j + 1] * a[j + 1]) % 100 < (a[j] * a[j]) % 100:
            a[j + 1], a[j] = a[j], a[j + 1]
print(a)

