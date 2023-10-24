from itertools import repeat
def travel(n):
    yield from repeat('по кочкам', n)
    return 'и в яму'

def travelwrap(n):
    end = yield from travel(n)
    yield end

print(*list(travelwrap(6)), sep='\n')