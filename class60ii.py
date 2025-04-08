try:
    print(g)
except (SyntaxError,NameError):
    print("Name error")
else:
    print("No Error")
finally:
    print("this always executes")
    