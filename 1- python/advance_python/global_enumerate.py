# global keyword in python
# ‘global’ keyword is used to modify the variable outside of the current scope.

x = 10  # Global variable

def modify_global():
    global x
    x = 20  # Modifying global variable
    print("Inside function, modified global x:", x)
    
modify_global()
print("Outside function, global x:", x)

# enumerate function in python
# enumerate() function adds a counter to an iterable and returns it as an enumerate object.

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
# Output:
# Index: 0, Fruit: apple
# Index: 1, Fruit: banana
# Index: 2, Fruit: cherry

