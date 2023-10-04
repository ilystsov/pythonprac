def Pareto(*pairs):
    res = []
    for i in range(len(pairs)):
        for j in range (len(pairs)):
            if pairs[i][0] <= pairs[j][0] and pairs[i][1] <= pairs[j][1] and (pairs[i][0] < pairs[j][0] or pairs[i][1] < pairs[j][1]):
                break
        else:
            res.append(pairs[i])
    return tuple(res)
pairs = eval(input() + ',')
print(Pareto(*pairs))
