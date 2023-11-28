C = type("C", (), {"var": 100500, "__init__": lambda self, x: setattr(self, "var", x)})
print(C.var)
c = C(123)
print(c.var)