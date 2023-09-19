def digit_sum_6(a):
    digit_sum = 0
    while a > 0:
        digit_sum += a % 10
        a //= 10
    return digit_sum == 6

n = int(input())
i = n
while i <= n + 2:
    j = n
    while j <= n + 2:
        print(i, '*', j, '=', ':=)' if digit_sum_6(i * j) else i * j, end=' ')
        j += 1
    print()
    i += 1