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


myStr = "Hello World"

# There's a function that allows you to know the methods that you can apply to a value.
dir()
## Example <uncomment to test>
# print(dir(myStr))

## Method example 1: will return myStr in uppercase
print(myStr.upper())
## Method example 2: will return myStr in lowercase
print(myStr.lower())
## Method example 3: will return myStr characters into its opposite
print(myStr.swapcase())

# Chained methods: is used for making multiple method calls on the same object, using the object reference just once.
## Method example 4: will return myStr replacing "Hello" with "Bye" and print it uppercase
print(myStr.replace('Hello', 'Bye').upper())