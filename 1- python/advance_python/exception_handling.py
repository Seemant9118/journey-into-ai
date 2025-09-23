# exception handling in python

# There are many built-in exceptions which are raised in python when something goes wrong.
# Exception in python can be handled using a "try" statement. The code that handles the exception is written in the "except" clause.

# try:
# # Code which might throw exception
# except Exception

# Example 1: Handling a ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
# Output: Error: Division by zero is not allowed.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except TypeError:
    print("Error: Invalid type.")
except:
    print("Error: An unexpected error occurred.")

# rasing exceptions
# We can raise custom exceptions using the ‘raise’ keyword in python.
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    else:
        print(f"Your age is {age}.")

try:
    check_age(-5)
except ValueError as ve:
    print(f"ValueError: {ve}")
    
# try with "else" clause
# Sometimes we want to run a piece of code when try was successful.
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print(f"You entered: {num}")
    
# try with "finally" clause
# Python offers a ‘finally’ clause which ensures execution of a piece of code inspective of the exception.
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Execution completed.")
    try:
        file.close()
    except:
        pass

