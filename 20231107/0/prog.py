class A:
    v = 1
class B(A):
    v = 2
b = B()
b.v = 3
print('до удаления из b:', b.v)
del b.v
print('после удаления из b:', b.v)
print('до удаления из класса B:', b.v)
del B.v
print('после удаления из класса В:', b.v)
