class A: pass
class B: pass

class C(A, B): pass
class D(B, A): pass
#invalid
class E(A, C):pass
class E(B, C):pass
class E(D, C):pass
class E(C, D): pass
#AC A CAB
#valid
class E(C, A):pass
class E(B, C):pass

