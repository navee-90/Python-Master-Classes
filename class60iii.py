file=open("finally.txt","w")
try:
    file.write("Hello World!")
    print("Writing to file...")
except FileNotFoundError:
    print("File not found!")
except IOError:
    print("Could not write to file.")
else:
    print("File written successfully.")
finally:
    file.close()
    print("File closed.")