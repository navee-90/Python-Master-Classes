# Abstraction
# Abstraction means hiding the internal details and showing only the essential features to the user.
# In OOP, abstraction helps us work with interfaces, not implementation.
from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def milleage(self):
        pass

    @abstractmethod
    def milleage1(self):
        pass
class Tesler(Car):
    def milleage(self):
        print("This milleage is 50Kmph")

    def milleage1(self):
        print("This milleage is 20Kmph")
M1=Tesler()
M1.milleage() #abstract method
M1.milleage1()
class Suzuki(Tesler):
    def milleage(self):
        print("This milleage is 10Kmph")
P1=Suzuki()
P1.milleage() #abstract method

# inheritance means accepting the properties from parent class to child class.
# abstract method: the forcing of the child class to implement the abstract method of the parent class.
# polymorhism:same method name with different implementation.
# encapsulation : protecting the variable insite the class.