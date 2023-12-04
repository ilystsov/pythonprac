def decorate(fun):
    def newfun(*args, **kwargs):
        print(f'{fun.__name__}: {args[1:]}, {kwargs}')
        return fun(*args, **kwargs)
    return newfun

class dump(type):
    @staticmethod
    def __new__(metacls, name, parents, ns, **kwds):
        cls = super().__new__(metacls, name, parents, ns)
        for name, attr in cls.__dict__.items():
            if callable(attr):
                setattr(cls, name, decorate(attr)) 
        return cls


import sys
exec(sys.stdin.read())