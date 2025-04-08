# inheritance
# Inheritance is a feature in Object-Oriented Programming where a child class (subclass) can inherit properties and methods from a parent class (superclass).
# Code Reusability: Don't repeat yourself!
# Extensibility: Build more advanced classes on top of basic ones
# Clean structure: Organize related classes logically.
class Mammal:
    def walk(self):
        print("Walking..")
class Dog(Mammal):
    def bark(self):
        print("Barking")
d=Dog() #instance class
d.bark() #invoke 
d.walk() #inheritance
M=Mammal()#instance class
M.walk() #invoke
# inheritance  a child class inherits from a parent class