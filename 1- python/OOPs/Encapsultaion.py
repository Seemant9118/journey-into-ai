# Encapsulation

# property : The property() function in Python is used to create and manage attributes in a class.
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14 * (self._radius ** 2)
    
c = Circle(5)

print(c.radius)  # 5 (getter called)
print(c.area)    # 78.5 (computed using getter of area)

c.radius = 10    # setter called, validates & updates _radius

print(c.radius)  # 10 (getter again)
print(c.area)    # 314.0 (computed dynamically)

# Why use property instead of direct attributes?
# Encapsulation: You can hide implementation details (e.g., store _radius, but expose radius).
# Validation: You can enforce rules (like radius ≥ 0).
# Flexibility: You can later change how the attribute is computed (lazy evaluation, caching, etc.) without changing external code.
# ✅ Example: Imagine tomorrow you switch to using math.pi instead of 3.14 for area → external code (c.area) stays the same!

