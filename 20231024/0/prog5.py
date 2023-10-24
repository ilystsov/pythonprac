from itertools import dropwhile, count, accumulate, islice
print(*list(islice(dropwhile(lambda x: x <= 1.6, accumulate(1/i/i for i in count(1))), 10)))