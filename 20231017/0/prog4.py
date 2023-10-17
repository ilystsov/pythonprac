import collections

d = collections.defaultdict(int)
for i in input().split():
    d[i] += 1
print(d.items())
