matrix = []
while s := input():
    matrix.append(eval(s))
l = len(matrix)
if all([len(el) == l for el in matrix]):
    for i in range(l):
        for j in range(i + 1, l):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in matrix:
        print(*i)
else:
    for i in matrix:
        print(*i)