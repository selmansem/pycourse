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

# To create a tuple, the varaible must have multiple values
# otherwise, the variable will be interpreted according to the data type of the only specified value.

x = (1, 2, 3, 1, '6')
print(x)
print(type(x))

# In case it's specified just one value is not considered a tuple
y = (4)
print(y)
print(type(y))

# To force that the value be considered as tupel must add a comma after
z = (5,)
print(z)
print(type(z))

# To count the values inside the tuple
print(len(x))

# To count how many times a specific value appears
print(x.count(1))

# To get a value by index
print(x[2])

# Now I'm gonna get two values from the tuple x, one of them will be formatted as int. And I will add them.
# 1: Taking values
value_1 = x[2] #3
value_2 = x[4] #6

# Formatting the second value as integer
value_2 = int(value_2)

# Adding them
total = value_1 + value_2

# Print total
print(f'The total of the sum of {value_1} plus {value_2} is {total}', end='\n')

# Finally to delete a variable use del before the variable name
var_to_delete = 'Hello there'
print(var_to_delete)

del var_to_delete
print(var_to_delete) # Will give an error because the variable is deleted

# Example of use purposes
# Inside a dictionary
{
    "Madrid": (-3.7025600, 40.4165000), # Long and lat of Madrid
    "Sevilla": (-5.9731700, 37.3828300),  # Long and lat of Sevilla
    "Granada": (-3.6066700, 37.1881700),  # Long and lat of Granada
    "Barcelona": (2.1589900, 41.3887900)  # Long and lat of Barcelona
}


# Remember: Tuples can't be modified