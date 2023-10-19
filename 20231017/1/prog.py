s = input().lower()
pairs = set()
for i in range(1, len(s)):
    if s[i].isalpha() and s[i - 1].isalpha():
        pairs.add(s[i - 1:i + 1])
print(len(pairs))
