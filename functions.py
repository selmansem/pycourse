# import only system from os
from os import system, name

# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# now call function we defined above
clear()

#######################################################################
## The function above is to clean the console each time run the code ##
#######################################################################



# The parameters can be obtained from user input, specified in the code as variables or directly in the function call
numberOne = 10
numberTwo = 20

# To use functions in python you have to define them before with their parameters
# In this case the function prints the result, but can return in it to be used
def my_function_add(numberOne, numberTwo):
    print(numberOne + numberTwo)

# Calling the function
my_function_add(numberOne, numberTwo)

# Function return value
def my_function_multiply(n1, n2):
    return n1 * n2

print(my_function_multiply(3, 2))

# In python, you can create anonymous functions called lambda.
# This function automaticaly returns the result.
# lambda syntax:
# <function_name> = lambda <parameters>: <operations>
substract_lamb_func = lambda n1, n2: n1 - n2
print(substract_lamb_func(3, 1))