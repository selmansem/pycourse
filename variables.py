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


# !Rememer python is case sensitive
# and can't start a variable's name with numbers
# 2variablename BAD
# to do it you must use underscore
# _2variablename GOOD

# Save variable with specified name
variablename = "That string"
print(variablename)

# You can set al the variables in one line <like an array>
x, y, z, randomstring = 1, 2, 3, "A random string"
print(x)
print(y)
print(z)
print(randomstring)

# And can print them in th esame line
print(randomstring, x, z, y)

# Conventions
# Tip 1: while you're coding there multiple ways to name a variable. The first one is the most used and common. All them are valid.
book_name = "I robot" # Snake case - using the underscore sign
bookName = "I robot" # Camel case - first character in lowercase
BookName = "I robot"  # Pascal case - first character in uppercase

# Tip 2: The recommended way to set a constant is writing the name uppercase
BOOK_NAME = "I robot"
