import struct
import random
import sys
for fmt, name in [("<f3si", sys.argv[1]), ("!f3si", sys.argv[2])]:
    i = int(random.uniform(0, 100))
    f = (random.uniform(0, 100))
    b = random.randbytes(3)
    with open(sys.argv[1], 'wb') as file:
        for i in range(10):
            s = struct.pack(fmt, f, b, i)
            file.write(s)
