from itertools import islice, tee
def slide(seq, n):
    i = 0
    working_seq, const_seq = tee(seq)
    while True:
        window = islice(working_seq, i, n + i)
        if (el := next(window, None)) == None:
            break
        else:
            yield el
        yield from window
        i += 1
        working_seq, const_seq = tee(const_seq)

import sys
exec(sys.stdin.read())
    