matrix = []
while s := input():
    matrix.append(eval(s))

for i in matrix:
    print(*i)

print()
l = len(matrix[0])
for i in range(l):
    for j in range(i + 1, l):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for i in matrix:
    print(*i)