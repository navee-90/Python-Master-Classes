class Calc:
    def __init__(self,x,y): #__init__ is constructor
        self.x=x
        self.y=y
        print("Hello World!")
    def add(self):
        return self.x+self.y
    def sub(self):
       return self.x-self.y
    def mul(self):
        return self.x*self.y
    def div(self):
        return self.x/self.y