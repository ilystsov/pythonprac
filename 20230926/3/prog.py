m1 = []
m2 = []
s = eval(input())
n = len(s)
m1.append(s)
for i in range(n - 1):
    m1.append(eval(input()))
for i in range(n):
    m2.append(eval(input()))

ans = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            ans[i][j] += m1[i][k] * m2[k][j]

for i in ans:
    print(*i, sep=',')

