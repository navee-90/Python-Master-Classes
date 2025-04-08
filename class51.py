# os module
# The os module in Python is used to interact with the operating system
# — it lets you work with files, directories, paths, environment variables, and more
# Get Current Working Directory
# print(os.getcwd())  # Example: /Users/yourname/project
# import os
# print(os.getcwd())


# import os
# os.chdir("N:/") # Change the current working directory to N:/
# os.mkdir("temp") # Create a directory

# import os
# os.rmdir("temp") # Remove a directory
import os
os.chdir("N:/temp")
f=open("myfile.txt","w") # w means write
f.write("Hello World!")
f.close()
