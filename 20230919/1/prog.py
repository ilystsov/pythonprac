a = int(input())
print('A', '+' if a % 25 == 0 and a % 2 == 0 else '-', end=' ')
print('B', '+' if a % 25 == 0 and a % 2 == 1 else '-', end=' ')
print('C', '+' if a % 8 == 0 else '-')
