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



# SETS are an unordered non indexed set of values
# Can't be accessed by an index
# Are specified between {} and separated by comma

colors = {'Red', 'Green', 'Blue'}

print(colors)
print(type(colors))

# Add more values
colors.add('Purple')
print(colors)

# Remove values
colors.remove('Green')
print(colors)

# Check if a value exist in set
# Refurn a boolean answer
print('Red' in colors)