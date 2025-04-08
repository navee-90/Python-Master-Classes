# class,object
# self is mandorty in class methods
# object:
# An object is an actual instance of a class — a real thing created based on the blueprint.
# class
# A class is like a blueprint for creating objects. It defines:
# Attributes (data)
# Methods (functions that act on the data)
class MyClass:
    x=5
    def sayHello(self): #self is argument
        print("Hello")
        print(self.x)
p1=MyClass()
# print(p1.x) #5
p1.sayHello()
        