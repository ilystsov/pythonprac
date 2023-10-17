from collections import Counter
print('\n'.join(f"{k}: {v}" for k, v in Counter(input().split()).most_common()))