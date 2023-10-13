import math
matrix = []
lid = input()
matrix.append(lid)
gas_quantity = 0
liquid_quantity = 0
while (s := input()) != lid:
    matrix.append(s)
    if s[1] == '.':
        gas_quantity += len(s) - 2
    else:
        liquid_quantity += len(s) - 2
matrix.append(s)    
n = len(matrix[0])
m = len(matrix)
volume = gas_quantity + liquid_quantity
liquid_quantity = (m - 2) * math.ceil(liquid_quantity / (m - 2))
gas_quantity = volume - liquid_quantity
print(m * '#')
for i in range(gas_quantity // (m - 2)):
    print('#' + '.' * (m - 2) + '#')
for i in range(liquid_quantity // (m - 2)):
    print('#' + '~' * (m - 2) + '#')
print(m * '#')
m = max(gas_quantity, liquid_quantity)
fraction_space = len(str(volume)) + len(str(m)) + 1
print(f"{round((gas_quantity / m) * 20) * '.':<20}", f"{f'{gas_quantity}/{volume}':>{fraction_space}}")
print(f"{round((liquid_quantity / m) * 20) * '~':<20}", f"{f'{liquid_quantity}/{volume}':>{fraction_space}}")
