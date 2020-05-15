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


cities = {
    "Madrid": (-3.7025600, 40.4165000),  # Long and lat of Madrid
    "Sevilla": (-5.9731700, 37.3828300),  # Long and lat of Sevilla
    "Granada": (-3.6066700, 37.1881700),  # Long and lat of Granada
    "Barcelona": (2.1589900, 41.3887900)  # Long and lat of Barcelona
}

print(cities.get("Madrid"))