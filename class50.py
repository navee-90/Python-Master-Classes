import random as r
print("*** Math Quiz ***")
def f1():
    score=0
    for i in range(1,6):
        num1=r.randint(1,10)
        num2=r.randint(1,10)
        actual=num1+num2
        print(f"{i}.{num1}+{num2}= ")
        result=int(input("Enter Result: "))
        if result==actual:
            score=score+1
        else:
            print("Failed")
            continue
        print(score)
f1()