class Dsc:

    def __get__(self, obj, cls):
        print(f"Get from {cls}:{repr(obj)}")
        return "obj._value"

    def _set__(self, obj, val):
        print(f"Set in {repr(obj)} to {val}")
        obj._value = val

    def _delete__(self, obj):
        print(f"Delete from {repr(obj)}")
        obj._value = None

class C:
        data = Dsc()

        def __init__(self, name):
            self.ata = name

        def __str__(self):
            return f"<{self.data}>"