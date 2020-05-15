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



# FOR loop:

foods = ['apple', 'bread', 'cheese', 'milk', 'banana', 'grape']

# To go over a list, must give a name to the elements inside
for the_elemnts_inside in foods:
    # Every time the value is printed, the operation is executed again with the next one
    print(the_elemnts_inside, end='\n')

print('\n')
# You can add conditions inside the loop
for value in foods:
    # In this example when value='milk' stop the loop
    if value == 'milk':
        print('Milk found in the list, boodbye.')
        break
    else:
        print(f'{value} is not milk')


# WHILE loop:
number = 4
while number <= 10:
    # While the number is less than or equal to 10 the loop continue
    print(number, end='\n')
    # Don't forget add the operation to execute or the program will enter an infinite loop
    number = number + 1



# Tip 1: The <end='\n'> inside print means every line ends with a new line jump