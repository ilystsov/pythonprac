def objcount(cls):
    class NewCls(cls):
        counter = 0
        def __init__(self, *args, **kwargs):
            self.__class__.counter += 1
            if '__init__' in dir(cls):
                super().__init__(*args, **kwargs)

        def __del__(self):
            self.__class__.counter -= 1
            if '__del__' in dir(cls):
                super().__del__()
    return NewCls


import sys
exec(sys.stdin.read())