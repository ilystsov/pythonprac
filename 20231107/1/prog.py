import collections

class DivStr(collections.UserString):
    def __init__(self, s=''):
        super().__init__(s)

    def __floordiv__(self, n):
        l = len(self.data) // n
        start = 0
        end = l
        for i in range(n):
            yield self.__class__(self.data[start:end])
            start += l
            end += l

    def __mod__(self, n):
        k = len(self.data) % n
        if k == 0:
            return self.__class__()
        return self.__class__(self.data[-k:])


import sys
exec(sys.stdin.read())
