# pycourse
Python Course

## Requirements:
-   Python 3.6 or greater
-   Visual Code Studio

## Note:
### Every example starts with:

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

### How to get third party modules:
Using command <code>*pip*</code>:
```console
pip install <module-name>
```
To obtain the documentation of the module visit [PYPI](https://pypi.org){target="_blank"}.

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
-   **Dictionaries** are an unordered collection of data in a *key*:*value* pair form.
-   **NoneType** is a null value.
### Variables [example](variables.py)
-   Ways to define and call variables.
-   Tips for naming variables and constants.
### Strings [example](strings.py)
-   How to know the methods that you can apply to a value.
-   Various examples of methods for strings.
### Numbers [example](numbers.py)
-   How let user input data.
-   How to convert string to int.
-   How to format a print string.
### Lists [example](lists.py)
-   Define a list.
-   Define a list from range.
-   Get list value by index.
-   Add values to list.
-   Remove values from list.
### Tuples [example](tuples.py)
-   Define a tuple.
-   Printing data from tuple.
-   Implementation example.
### Sets [example](set.py)
-   Define a set.
-   Printing data from set.
-   Add values to set.
-   Delete values from set.
-   Check if value exist in set.
### Dictionaries [example](dictionaries.py)
-   Define a dictionary.
-   Printing data from dictionary.
### Conditionals [example](conditionals.py)
-   Comparison operators.
-   Logic operators.
-   Example *if, elif* and *else*.
-   Note switch statement.
### Loops [example](loops.py)
-   Define *FOR* loop.
-   Example *FOR* loop.
-   Define *WHILE* loop.
-   Example *WHILE* loop.
### Functions [example](functions.py)
-   Define funcions.
-   Explain *lambda* funcions.
### Modules [example](modules.py)
-   Define and explain the three ways to get modules.