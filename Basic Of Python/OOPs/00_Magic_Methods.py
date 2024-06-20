# magic methods are special methods that begin and end with double underscores (__) and have specific predefined functionality. 
# These methods allow you to define how objects behave in certain situations, such as arithmetic operations, comparisons, iteration, and more
# They are also known as dunder methods (short for "double underscore").
# Example : __init()  ,  __str__()  ,  __repr__()  ,  __add__()  ,  __mul__() etc.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return 2

    def __contains__(self, item):
        return item == self.x or item == self.y

# Example usage
v1 = Vector(1, 2)
v2 = Vector(3, 4)

print("Representation:", repr(v1))
print("Representation:", repr(v2))
print("Addition:", v1 + v2)
print("Subtraction:", v2 - v1)
print("Multiplication:", v1 * 3)
print("Equality Comparison:", v1 == v2)
print("Length:", len(v1))
print("Contains:", 2 in v1)
