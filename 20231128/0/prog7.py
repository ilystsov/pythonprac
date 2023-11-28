import inspect
class C:
    a: int 
    def __init__(self, val):
        t = inspect.get_annotations(self.__class__)['a']
        if isinstance(val, t):
            self.a = val
        else:
            raise TypeError

c = C(2)
c = C('w2')

