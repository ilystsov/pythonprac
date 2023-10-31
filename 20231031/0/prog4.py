class Rectangle:
    rectcnt = 0
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.__class__.rectcnt += 1
        name = f'rect_{self.__class__.rectcnt}'
        setattr(self, name, self.__class__.rectcnt)
    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1})\nobjects number: {self.__class__.rectcnt}"
    def __abs__(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)
    def __lt__(self, obj):
        return abs(self) < abs(obj)
    def __eq__(self, obj):
        return abs(self) == abs(obj) 
    def __mul__(self, number):
        return self.__class__(self.x1 * number, self.y1 * number, self.x2 * number, self.y2 * number)
    __rmul__ = __mul__
    def __getitem__(self, idx):
        return [(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1)][idx]
    def __bool__(self):
        return abs(self) != 0
    def __del__(self):
        print('Deleting', self)
        self.__class__.rectcnt -= 1