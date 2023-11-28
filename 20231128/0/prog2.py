class ctype(type):

    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        print("prepare", name, bases, kwds)
        return super().__prepare__(name, bases, **kwds)

    @staticmethod
    def __new__(metacls, name, parents, ns, **kwds):
        print("new", metacls, name, parents, ns, kwds)
        return super().__new__(metacls, name, parents, ns)

    def __init__(cls, name, parents, ns, **kwds):
        print("init", cls, parents, ns, kwds)
        return super().__init__(name, parents, ns)

    def __call__(cls, *args, **kwargs):
        print("call", cls, args, kwargs)
        return super().__call__(*args, **kwargs)

class C(metaclass=ctype, parameter='QQ'):
    pass