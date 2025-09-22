# Inheritance in Python
# Inheritance is a way of creating a new class from an existing class

# Base class
class Animal:
    def speak(self):
        return "Animal speaks"

# Derived class
class Dog(Animal):
    def bark(self):
        return "Dog barks"
    
# Another derived class
class Cat(Animal):
    def meow(self):
        return "Cat meows"

# Creating objects of derived classes
dog = Dog()
cat = Cat()
print(dog.speak())  # Inherited method
print(dog.bark())   # Dog's own method
print(cat.speak())  # Inherited method
print(cat.meow())   # Cat's own method

# Type of Inheritance
# 1. Single Inheritance occurs when child class inherits only a single parent class.
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def bark(self):
        return "Dog barks"

# 2. Multi-level Inheritance occurs when a child class inherits from a parent class, which in turn inherits from another parent class.
class Puppy(Dog):
    def weep(self):
        return "Puppy weeps"

# 3. Multiple Inheritance occurs when the child class inherits from more than one parent classes.
class Employee:
    def emp_id(self):
        return "Employee ID"

class Person:
    def person_id(self):
        return "Person ID"

class Programmer(Employee, Person):
    def prog_id(self):
        return "Programmer ID"

# 4. Hierarchical Inheritance occurs when multiple classes inherit from a single parent class.
class Dog(Animal):
    def bark(self):
        return "Dog barks"

class Cat(Animal):
    def meow(self):
        return "Cat meows"

class Lion(Animal):
    def roar(self):
        return "Lion roars"
    
# super() METHOD
# The super() function is used to give access to methods and properties of a parent or sibling class.
class Parent:
    def show(self):
        return "Parent class method"

class Child(Parent):
    def show1(self):
        parent_method = super().show()  # Calling parent class method
        return f"{parent_method} and Child class method"

child = Child()
print(child.show1())

# class method :  A class method is a method which is bound to the class and not the object of the class.
class Parent:
    classAttr = 10
    @classmethod
    def class_method(cls):
        return f"This is a class attribute is {cls.classAttr}"

a = Parent()
a.classAttr = 20 
print(a.class_method())

