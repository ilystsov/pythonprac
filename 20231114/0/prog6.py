class C:
    @property
    def field(self):
        return self._val
    @field.setter
    def field(self, value):
        self._val = value