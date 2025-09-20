# conditionals in python
a = 33
b = 200
if (b > a):
  print("b is greater than a") # Output: b is greater than a

# if...else statement
a = 33
b = 33
if (b > a):
  print("b is greater than a")
else:
  print("b is not greater than a") # Output: b is not greater than a

# elif statement
a = 200
b = 33
c = 500
if (b > a):
  print("b is greater than a")
elif (a == b):
    print("a and b are equal")
else:
  print("a is greater than b") # Output: a is greater than b

# nested if statement
x = 41
if (x > 10):
  print("Above ten,")
  if (x > 20):
    print("and also above 20!")
  else:
    print("but not above 20.") # Output: Above ten, and also above 20!

# short hand if statement 
if (a > b): print("a is greater than b") # Output: a is greater than b

# short hand if...else statement
a = 2
b = 330
print("A") if (a > b) else print("B") # Output: B

# and keyword
a = 200
b = 33
c = 500
if (a > b) and (c > a):
  print("Both conditions are True") # Output: Both conditions are True

# or keyword
a = 200
b = 33
c = 500
if (a > b) or (a > c):
  print("At least one of the conditions is True") # Output: At least one of the conditions is True

# nested if...else statement
x = 41
if (x > 10):
  print("Above ten,")
  if (x > 20):
    print("and also above 20!")
  else:
    print("but not above 20.") # Output: Above ten, and also above 20!


# pass statement
a = 33
b = 200
if (b > a):
  pass # pass is used as a placeholder for future code

# Example of using pass in a function
def myfunction():
  pass # pass is used as a placeholder for future code
myfunction()  
# Output: No output, function does nothing


