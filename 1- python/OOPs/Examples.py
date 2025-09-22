# Create a class (2-D vector) and use it to create another class representing a 3-D vector.
class Vector2D: 
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def display(self):
        print(f"Vector2D({self.x}, {self.y})")

class Vector3D(Vector2D):
    def __init__(self,x,y,z):
        super().__init__(x,y)  # Call the constructor of the parent class
        self.z = z
    def display(self):
        print(f"Vector3D({self.x}, {self.y}, {self.z})")

# Example usage
v2d = Vector2D(3, 4)
v2d.display()  # Output: Vector2D(3, 4)

v3d = Vector3D(5, 6, 7)
v3d.display()  # Output: Vector3D(5, 6, 7)

class Animal:
    pass
class Pet(Animal):
    def __init__(self, pet):
        self.pet = pet
    def display(self):
        print(f"Animal of Pet is a {self.pet}")
class Dog(Pet):
    def __init__(self, pet, dogBreed):
        super().__init__(pet)
        self.dogBreed = dogBreed
    def display(self):
        print(f"Animal of Pet is a {self.pet} and breed is {self.dogBreed}")

# Example usage
dog = Dog("Dog", "Bulldog")
dog.display()  # Output: Animal of Pet is a Dog and breed is Bulldog

class Employee:  
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @property
    def annual_salary(self):
        return self.salary * 12
    @annual_salary.setter
    def annual_salary(self, annual_salary):
        self.salary = annual_salary / 12
    def display(self):
        print(f"Employee Name: {self.name}, Monthly Salary: {self.salary}, Annual Salary: {self.annual_salary}")

    @property
    def increment_salary(self):
        return self.salary * 1.10  # 10% increment
    @increment_salary.setter
    def increment_salary(self, new_salary):
        self.salary = new_salary    
    def display_incremented_salary(self):
        print(f"Employee Name: {self.name}, Incremented Monthly Salary: {self.increment_salary}") 
  
# Example usage
emp = Employee("John", 3000)
emp.display()  # Output: Employee Name: John, Monthly Salary: 3000, Annual Salary: 36000
emp.increment_salary = 3500  # Set new salary
emp.display_incremented_salary()  # Output: Employee Name: John, Incremented Monthly Salary: 3850.0
