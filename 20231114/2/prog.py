class Num:
    def __get__(self, obj, cls):
        return getattr(obj, 'field', 0)

    def __set__(self, obj, val):
        if hasattr(val, 'real'):
            obj.field = val
        elif hasattr(val, '__len__'):
            obj.field = len(val)


import sys
exec(sys.stdin.read())
