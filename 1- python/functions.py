# functions in Python
def greet(name):
    """Function to greet a person with their name."""
    return f"Hello, {name}!"

print(greet("Alice"))

# types of functions
# 1. Built-in functions
print(len("Hello"))  # Output: 5

# 2. User-defined functions
def add(a, b):
    """Function to add two numbers."""
    return a + b
print(add(5, 3))  # Output: 8

# funcions with default arguments
def greet_person(name, msg="Good morning!"):
    """Function to greet a person with a default message."""
    return f"{msg}, {name}!"
print(greet_person("Bob"))  # Output: Good morning!, Bob!
print(greet_person("Bob", "Hello"))  # Output: Hello, Bob!

# functions with variable-length arguments
def sum_all(*args):
    """Function to sum all numbers passed as arguments."""
    return sum(args)    
print(sum_all(1, 2, 3, 4))  # Output: 10

# functions with keyword arguments
def display_info(**kwargs):
    """Function to display information passed as keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="Alice", age=30)

# lambda functions
square = lambda x: x * x
print(square(5))  # Output: 25

# examples of lambda functions

# A lambda function to add two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Using a lambda with filter() to get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # Output: [2, 4, 6]

# Using a lambda with map() to square each number in a list
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers) # Output: [1, 4, 9, 16, 25, 36]