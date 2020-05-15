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



demo_list = [1, "Hello", 4.3, True, [1, 2, 3]]
colors = ['red', 'green', 'blue']

# To create a list with a non-variable must specify the list values inside a tuple ()
numbers = list((4, 5, 6))
print(numbers)
print(type(numbers))

# To print a range of numbers use the range method
## Remember the range method last value is not included
## Example 1: If you want to print a range from 1 to 10
one_to_ten = list(range(1, 11))
print(one_to_ten)
## If you write in code 10 instead 11 will return 9
print(list(range(1, 10)))

# To get the list lenght use len()
_1_to_10_len = len(one_to_ten)
print(f'\nThe lenght of one_to_ten variable is {_1_to_10_len}')

# To get a list value by index
print(colors[1])

# The fifth value in demo_list is a list, so it's considered as one value
print(demo_list[4])

# To add one value to list
colors.append('black')
print(colors)

# To add multiple values to list, must set them inside a list[] or tuple[]
colors.extend(('hello', 2, 'you'))
print(colors)
colors.extend(['good', 'bye'])
print(colors)

# To add a value in a specified position, use insert(<position>, <value>)
colors.insert(3, 'white')
print(colors)

# To remove a specific list value use remove()
colors.remove(2)
print(colors)

# To delete list value by index use pop()
colors.pop(2)
print(colors)

# To sort the list alphabetically
colors.sort()
print(colors)

# And reverse sort just set the property reverse=True
colors.sort(reverse=True)
print(colors)

# To remove all list values use clear()
colors.clear()
print(colors)


# Tip 1: \n means jump to next line
# Tip 2: For sort can't use multiple data types