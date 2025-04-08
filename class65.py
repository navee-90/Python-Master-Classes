# Encapsulation
# Encapsulation is one of the key principles of Object-Oriented Programming (OOP).
# It means hiding the internal state and requiring all interaction through methods — like putting data in a “capsule” 

class Employee:
    def __init__(self,name):
        self.name=name
    def setName(self,n):
        self.name=n
    def getName(self):
        return self.name
M1=Employee("Naveen")
M1.name="Swathi"
print(M1.name)
M1.setName("Bunny")
print(M1.getName())
