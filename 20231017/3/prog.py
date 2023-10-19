from collections import Counter
w = int(input())
d = {}
c = Counter()
while s := input():
    new_s = ''
    for i in s:
        if i.isalpha():
            new_s += i
        else:
            new_s += ' '
    new_s = new_s.lower()
    c.update(Counter(i for i in new_s.split() if len(i) == w))
if c:
    occ_number = c.most_common()[0][1]
    ans = [word[0] for word in c.most_common() if word[1] == occ_number]
    print(*sorted(ans))