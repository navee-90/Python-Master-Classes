try:
    # print(g)
    print("Hello World!")
except (NameError, FileNotFoundError):
    print("Variable g is not defined or file not found")
except IOError:
    print("An I/O error occurred")
else:
    print("No Error")
finally:
    print("This block always executes")