class C:
    @property
    def age(self):
        if self._val == 42:
            print('secret value!')
            return -1
        return self._val

    @age.setter
    def age(self, value):
        if value > 128:
            raise ValueError('too old!')
        self._val = value