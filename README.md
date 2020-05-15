# pycourse
Python Course

## Requirements:
-   Python 3.6 or greater
-   Visual Code Studio

## Note:
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
1. [First code line](#first-code-line-example)
2. [Data types](#data-types-example)
3. [Variables](#variables-example)
4. [Strings](#strings-example)
5. [Numbers](#numbers-example)
6. [Lists](#lists-example)
7. [Tuples](#tuples-example)
8. [Sets](#sets-example)
9. [Dictionaries](#dictionaries-example)
10. [Conditionals](#conditionals-example)
11. [Loops](#loops-example)
12. [Functions](#functions-example)
13. [Modules](#modules-example)

## Abstracts:
### First code line [example](helloworld.py)
A simple code showing how to comment content and how to print the results on the screen.
### Data types [example](datatype.py)
Explain the data types you can use:
-   **Strings** can be enclosed in single or double quotes if they are single line.\
    They can also be enclosed in triple single or double quotes if they are single line.
-   **Type** function to get what type of data is the indicated value.
-   **Concatenate strings** using <kbd>+</kbd> and <kbd>,</kbd>.
-   **Numbers** can be integer or float.
-   **Booleans**, return values True or False.
-   **Sequences:**
    -   **Lists:** Ordered mutable data collections between square brackets <kbd>[</kbd><kbd>]</kbd>.
    -   **Tuples:** Ordered non-mutable data collections between parentheses <kbd>(</kbd><kbd>)</kbd>.
### Variables [example](variables.py)
### Strings [example](strings.py)
### Numbers [example](numbers.py)
### Lists [example](lists.py)
### Tuples [example](tuples.py)
### Sets [example](set.py)
### Dictionaries [example](dictionaries.py)
### Conditionals [example](conditionals.py)
### Loops [example](loops.py)
### Functions [example](functions.py)
### Modules [example](modules.py)