# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

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



# To request the user for data, use the input method
## Example: Now we gonna request a number to the user and save it in a variable
age = input("Insert your age: ")
print(age)

# But now the variable is saves as string
print(type(age))

# To convert a string into int, use int function
new_age = int(age)
print(f'Converted {new_age} string into integer and saved into a new variable called new_age')
print(type(new_age))

# Now with the converted string you can operate with the value as an integer
print(new_age + 2)

## Tip 1: You can print a value in the middle of a string by formatting it
## Before declaring the string you must add f, thats mean format
## And inside the string you must add the variable name in braces
