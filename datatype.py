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



# Strings
print('Hello world')
print("Hello world")
print('''Hello world''')
print("""Hello world\n""")

# String type
print(type('Hello world'))

# Concatente strings
print("Bye" + "World")

# Numbers
## Integer
print(30)
## Float
print(30.5)

# Booleans
True
False

# List <mutable> & can be empty & must be written between []
[10, 20, 30, 40]
['Hi', 'bonjour']
['Hello', 'hola', 10, True]
[]

# Tuple <inmutable> & can be empty
(10, 20, 40, 100)
()

# Dictionaries <key:value> & value can be empty
{
    "name":"Michel",
    "lastname":"Peterson",
    "nickname":"Micky"
}

# Undifined data
None
