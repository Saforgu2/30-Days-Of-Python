# DAY 14
# LEVEL 1

from functools import reduce
from string import ascii_uppercase

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'India', 'North Korea']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map: iterates over a list and returns another list with the changes of the function
# filter: iterates over a list and returns another list that satisfy's the functions criteria
# reduce: iyerates a list and returns a single value.

# higher order function: it takes as a parameter a function, it returns a function or it can be assigned to a varia
#                        ble 
# closures: nested functions, with access to outer scope (variables) and return the inner function
# decorators: A decorator is a design pattern in Python that allows a user to add new functionality to an existing  
#             object without modifying its structure.

# LEVEL 2

def change_to_uppercase(name):
    return name.upper()
countries_uppercase = map(change_to_uppercase, countries)
print(list(countries_uppercase))

def square(number):
    return number ** 2
numbers_square = map(square, numbers)
print(list(numbers_square))

names_uppercase = map(change_to_uppercase, names)
print(list(names_uppercase))

def conatins_land(name):
    if('land' in name):
        return True
    return False
land_countries = filter(conatins_land, countries)
print(list(land_countries))

def six_letters(name):
    if(len(name) == 6):
        return True
    return False
land_countries = filter(six_letters, countries)
print(list(land_countries))

def starts_with_e(name):
    if(name[0] == 'E'):
        return True
    return False
countries_with_e = filter(starts_with_e, countries)
print(list(countries_with_e))

'''country_upper_with_e = countries.map(change_to_uppercase).filter(starts_with_e)
print(list(country_upper_with_e))'''

def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers)
print(total)

def concatenate_countries(country1, country2):
    if(country2 == countries[len(countries) - 1]):
        return country1 + ' and ' + country2 + ' are north European countries.'
    return country1 + ', ' + country2
concatenated = reduce(concatenate_countries, countries)
print(concatenated)

