# Parents
class A1:
    def __init__(self, x):
        self.x = x # Class fields need not be previously declared, as they are in Java.
a1 = A1(2)
print(a1.x)
class A2: # Child of A
    def __init__(self, y):
       self.y = y
a2 = A2(4)
print(a2.y)

# Child 1
class B(A1, A2):
    def __init__(self, x, y):
        A1.__init__(self, x)
        A2.__init__(self, y)
b = B(3, 5)
print(b.x, ",", b.y)

# Using super to instantiate...
# Child 2
class C(A1, A2):
    def __init__(self, x, y):
        super().__init__(x)
        super().__init__(y)
c = C(7, 8)
try:
    print(c.x, ",", c.y)
except:
    print("Attribute 'y' not found for object of class C.")
    print(c.x)
    # This demonstrates that if super is called multiple times,
    # it merely instantiates the 1st parent class,
    # giving access to only that class' attributes and methods.