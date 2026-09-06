class A:
    pass

class B(A):
    def speak(self):
        print("HI from B")


class C(A):
    def speak(self):
        print("HI from C")

class D(B,C):
    pass

d = D()
print(D.__mro__)
d.speak()