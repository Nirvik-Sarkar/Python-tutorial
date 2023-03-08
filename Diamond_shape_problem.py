"""The "diamond problem" (sometimes referred to as the "Deadly Diamond of Death"[6]) is an 
ambiguity that arises when two classes B and C inherit from A, and class D inherits from both B 
and C. If there is a method in A that B and C have overridden, and D does not override it, then 
which version of the method does D inherit: that of B, or that of C?"""
#Code of Diamond shape problem
class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
    def met(self):
        print("This is a method from class C")

class D(C, B):
    def met(self):
        print("This is a method from class D")


a = A()
b = B()
c = C()
d = D()

d.met()


