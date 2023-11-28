class Doubleton(type):
    _instance1 = None
    _instance2 = None
    cnt = 0
    def __call__(cls, *args, **kw):
        if cls._instance1 is None:
             cls._instance1 = super().__call__(*args, **kw)

        elif cls._instance2 is None:
             cls._instance2 = super().__call__(*args, **kw)
        cls.cnt += 1
        return cls._instance1 if cls.cnt % 2 else cls._instance2

class C(metaclass=Doubleton): pass
print(*(C() for i in range(7)), sep="\n")