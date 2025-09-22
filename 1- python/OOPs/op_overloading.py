# Operators in Python can be overloaded using dunder methods.
# These methods are called when a given operator is used on the objects.
# Operators in Python can be overloaded using the following methods:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Overloading the - operator
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # Overloading the * operator
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    # Overloading the / operator
    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)

    # String representation of the object
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
p1 = Point(2, 3)
p2 = Point(5, 7)    
print(p1 + p2)  # Point(7, 10)
print(p1 - p2)  # Point(-3, -4)
print(p1 * p2)  # Point(10, 21)
print(p1 / p2)  # Point(0.4, 0.42857142857142855)
print(p1)       # Point(2, 3)
print(p2)       # Point(5, 7)
