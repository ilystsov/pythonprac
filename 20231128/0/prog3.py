class sole(type):
    def __new__(metacls, name, parents, namespace):
        if len(parents) > 1:
            raise TypeError("Cannot have more than one parent")
        return super().__new__(metacls, name, parents, namespace)

class C(metaclass=sole):
    pass
class D(C): pass
# class E(C, int): pass