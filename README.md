# pycourse
Python Course

Every example starts with:

<pre><code>
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
</code></pre>

## Order to read the examples:
1. [First code line](helloworld.py)
2. [Data types](datatype.py)
3. [Variables](variables.py)
4. [Strings](strings.py)
5. [Numbers](numbers.py)
6. [Lists](lists.py)
7. [Tuples](tuples.py)
8. [Sets](set.py)
9. [Dictionaries](dictionaries.py)
10. [Conditionals](conditionals.py)
11. [Loops](loops.py)
12. [Functions](functions.py)
13. [Modules](modules.py)
