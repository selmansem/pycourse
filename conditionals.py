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



# IT IS MANDATORY TO RESPECT THE TABULATION BEFORE THE CONDITIONAL OPERATIONS

age_to_compare = input('Insert a random age: ')
user_age = input('Insert user age: ')

# Arithmetic operators

# + Perform Addition between the operands 12 + 3 = 15
# - Perform Subtraction between operands 12 - 3 = 9
# * Perform Multiplication between the operands 12 * 3 = 36
# / Perform division between the operands 12 / 3 = 4
# % Make a module between operands 16 % 3 = 1
# ** Performs the power of operands 12 ** 3 = 1728
# // Perform division with integer result 18 // 5 = 3
print(12 + 3) # = 15
print(12 - 3) # = 9
print(12 * 3) # = 36
print(12 / 3) # = 4
print(16 % 3) # = 1
print(12 ** 3) # = 1728
print(18 // 5) # = 3

# Relational operators
# Conditionals to compare if, elif (same as else if in other languages) and else
if user_age > age_to_compare:
    print(f'The user is over {age_to_compare}')
elif user_age < age_to_compare:
    print(f'The user is under {age_to_compare}')
elif user_age == age_to_compare:
    print(f'The user is {user_age}')
else:
    print('There\'s someting wrong')

# Logic operators and, or, not.
if user_age > age_to_compare and user_age < age_to_compare:
    print(f'You\'re selecting an age range between {user_age} and {age_to_compare}')
elif not(user_age == age_to_compare):
    print(f'The user is not {age_to_compare}')


# Python does NOT have switch or case statement (ADDED IN PYTHON 3.10 AS MATCH CASE)
# You have to use dictionary mapping
month_number = input('Give me the month number and I\'ll tell you the name: ')

months = {
    1:'January',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'
}

month_number = int(month_number)

if month_number < 1 or month_number > 12:
    print(f'On the planet earth there is no month {month_number}')
else:
    print(months.get(int(month_number)))

# Match case
quit_flag = False
match quit_flag:
    case True:
        print("Quitting")
        exit()
    case False:
        print("System is on") 