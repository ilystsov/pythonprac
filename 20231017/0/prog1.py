import timeit
print(timeit.Timer('"-".join(str(n) for n in range(100))').autorange()) 