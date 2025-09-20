# # OOPs in python 
# Solving a problem by creating object is one of the most popular approaches in
# programming. This is called object-oriented programming.
# This concept focuses on using reusable code (DRY Principle). 

# class is python
# A class is a blueprint for creating object.
# A class is defined using the keyword 'class'.
# Syntax:
# class ClassName:
#     # class body
#     # attributes
#     # methods
# Example:
class Dog:
    # class attributes
    species = "Canis familiaris"

    # initializer / instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    

# An object is an instance of a class.
# instantiate the Dog class
mikey = Dog("Mikey", 6)
print(mikey.description())  # Output: Mikey is 6 years old
print(mikey.speak("Woof Woof"))  # Output: Mikey says Woof Woof


# A class is a logical entity while an object is a physical entity.
# A class can have attributes and methods.

# Attributes are the data members (variables) of a class.
# types of attributes:
# 1. Class attributes: Attributes that are shared among all instances of a class.
# Example of Class Attribute:
class Employee:
    company = "Google"  # Specific to Each Class

employeeObj = Employee()  # Object Instatiation
employeeObj.company
Employee.company = "YouTube"  # Changing Class Attribute

# 2. Instance attributes: Attributes that are specific to an instance of a class.
# Example of Instance Attribute:
employeeObj.name = "seemant"
employeeObj.salary = "30k"  # Adding instance attribute

# Note: Instance attributes, take preference over class attributes during assignment &
# retrieval.
# When looking up for employeeObj.attributes it checks for the following:
# 1) Is attribute present in object?
# 2) Is attribute present in class?

# Methods are the functions defined inside a class.

# __init__() constructor:
# The __init__() method is a special method that is called when an object is instantiated.
# It is used to initialize the attributes of the class.
# It is similar to a constructor in other programming languages.
# It is called automatically when an object is created.
# It can take arguments to initialize the attributes of the class.
# It is defined using the def keyword.
# Example:
class Person:
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age  # instance attribute
personObj = Person("John", 30)
print(personObj.name)  # Output: John

# self parameter:
# The self parameter is a reference to the current instance(object) of the class.
# It is used to access variables that belongs to the class.
# It must be the first parameter of any function in the class.
# It is similar to 'this' keyword in other programming languages.
# It is not a keyword in python, you can use any other name but it is recommended to use self.
# It is used to differentiate between instance attributes and local variables.
# Example:
class Car:
    def __init__(self, make, model):
        self.make = make  # instance attribute
        self.model = model  # instance attribute

    def display(self):
        return f"{self.make} {self.model}"  # accessing instance attributes using self
carObj = Car("Toyota", "Camry")
print(carObj.display())  # Output: Toyota Camry

carObj2 = Car("Honda", "Civic")
print(carObj2.display())  # Output: Honda Civic

# static method:
# A static method is a method that belongs to the class rather than the instance of the class
# It does not require a reference to the instance (self) or class (cls)
# It is defined using the @staticmethod decorator   
# It can be called using the class name or instance name
# Example:
class Math:
    @staticmethod
    def add(x, y):
        return x + y

obj = Math()
print(obj.add(5, 20))  # Output: 25
print(Math.add(5, 10))  # Output: 15

# Examples of classes in python
print("\n 1. Make a class Programmer store their information who work in microsoft")

class Programmer:
    company = "Microsoft"

    def __init__(self,name, age, designation, salary):
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = salary
    
    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Designation: {self.designation} at {self.company}, Salary: {self.salary}"


programmer1 = Programmer("Alice", 30, "Software Engineer", "100k")
print(programmer1.info())
programmer2 = Programmer("Bob", 35, "Senior Software Engineer", "150k")
print(programmer2.info())
        





