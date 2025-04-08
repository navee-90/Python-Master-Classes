# class Calc:
#     def __init__(self,x,y): #__init__ is constructor
#         self.x=x
#         self.y=y
#         print("Hello World!")
#     def add(self):
#         print(self.x+self.y)
#     def sub(self):
#         print(self.x-self.y)
# M1=Calc(8,5)
# M1.add()
# M1.sub()

# 2nd program
class Calc:
    def __init__(self,x,y): #__init__ is constructor
        self.x=x
        self.y=y
        print("Hello World!")
    def add(self):
        return self.x+self.y
    def sub(self):
       return self.x-self.y
M1=Calc(8,5)
a=M1.add()
b=M1.sub()
print(a)
print(b)