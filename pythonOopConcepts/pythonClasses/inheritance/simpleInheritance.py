# Inheritance using the constructor of the parent class
class A:
    def __init__(self, x):
        self.x = x # Class fields need not be previously declared, as they are in Java.
a = A(2)
print(a.x)
class B(A): # Child of A
    def __init__(self, x):
        A.__init__(self, x)
b = B(4)
print(b.x)

# Inheritance using the super function
# NOTES
# The super function returns a temporary object of the superclass that allows access to all of its methods to its child class.
# Here, we don't need not remember or specify the parent class name to access its attributes and methods.
# This function can be used both in single and multiple inheritances.
class C:
    def __init__(self, x):
        self.x = x # Class fields need not be previously declared, as they are in Java.
c = C(3)
print(c.x)
class D(C): # Child of A
    def __init__(self, x):
        super().__init__(x)
d = D(6)
print(d.x)