# polymorphism
# Polymorphism means "many forms" — in Python (and OOP), it refers to the ability to use the same method name or operator, 
# but it behaves differently based on the object or data type.
# Polymorphism = same method name, different behavior
# Method Overloading = same method name, different parameters

# method overloading
# Python does not support traditional method overloading (like in Java or C++), but you can mimic it using:
class MyClass:
    def greet(self,name=None,title=None):
        if name and title:
            return f"Hello {title},{name}"
        elif name:
            return f" Hello {name}"
        else:
            return "Hello"
C1=MyClass()
# txt=C1.greet("Naveen")
# txt=C1.greet()
txt=C1.greet("Naveen","Mr")
print(txt)

# method overriding
# When child class overrides a method from parent class.

# class shape:
#     def area(self):
#         print("Hello")
# class square(shape):
#     def area(self):
#         print("Good Morning!")
# M1=square()
# M1.area() #child preference