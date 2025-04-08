# Module
# A module is simply a Python file (.py) that contains definitions like functions, variables, and classes that you can reuse in other Python programs.
# syntax
# import module_name
# from module_name import function_name
# from module_name import function_name as alias
# from module_name import *  # imports everything from the module

# scripting
# A script is a Python file that is meant to be executed directly to perform a specific task (e.g., automation, data analysis, etc.).

# import addition 
from addition import*
# import subtract as minus
from subtract import *
from multiply import mul
from division import*
def calculator(n1,n2):
    a=addition(n1,n2)
    b=subtraction(n1,n2)
    c=mul(n1,n2)
    d=division(n1,n2)
    print(f"Addition:{a}-Subtaction:{b}- Multiplication:{c}-Division:{d}")
    # print(f"Addition:{a}-\nSubtaction:{b}-\nMultiplication:{c}-\nDivision:{d}")
calculator(20,2)