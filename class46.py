# enter two numbers from user task
num1=int(input("Enter Numer: "))
num2=int(input("Enter Number: "))
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def calculator(n1,n2):
    a=add(n1,n2)
    b=sub(n1,n2)
    c=mul(n1,n2)
    d=div(n1,n2)
    print(f"{a}-{b}-{c}-{d}")
calculator(num1,num2)