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



# We can use modules obtained from three ways:
# 1. Modules written by us
# 2. Third party modules from internet
# 3. Modules from the python libraries


# 1. MODULES WRITTEN BY US:
import myModule
myModule.add(2, 3)


# 2. THIRD PARTY MODULES FROM INTERNET: (use pip to install)
# In this case we're using colorama. To provide color to text in console.
# Importing the modules Fore, Back, Style, init from the library colorama
from colorama import Fore, Back, Style, init
# init module send reset sequences to turn off color changes at the end of every print automatically if is True.
init(autoreset=True)
print(Fore.RED + 'some red text')


# 3. MODULES FROM THE PYTHON LIBRARIES:
from datetime import date, timedelta
print(date.today())
print(timedelta(minutes=70)) # Will return time in hours