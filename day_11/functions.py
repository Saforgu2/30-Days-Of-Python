# DAY 11
# LEVEL 1

def add_two_numbers(num1, num2):
    return num1 + num2
print(add_two_numbers(2, 5))

def area_of_circle(r):
    PI = 3.14
    return PI * (r ** 2)
print(area_of_circle(6))

def add_all_nums(*args):
    total = 0
    for num in args:
        if(type(num) == int):
            total += num
        else:
            print('Not a number: ', num)
    return total
print(add_all_nums(1, 5, 6, 'H', 9, 10))

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * (9/5)) + 32
print(convert_celsius_to_fahrenheit(32))

def print_list(element):
    for i in element:
        print(i)
print_list([1, 3, 'Python'])

def reverse_list(lst):
    j = -1
    for i in range((len(lst) // 2)):
        tmp = lst[i]
        lst[i] = lst[j]
        lst[j] = tmp
        j -= 1
    return lst
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]

def capitalize_list_items(items):
    for i in range(len(items)):
        items[i] = items[i].capitalize()
    return items
print(capitalize_list_items(['cat', 'dog']))

# LEVEL 2
def evens_and_odds(number):
    evens = 0
    odds = 0
    for i in range(number + 1):
        if(i % 2 == 0):
            evens += 1
        else:
            odds += 1
    print('Evens: ', evens)
    print('Odds: ', odds)
evens_and_odds(100)

def factorial(number):
    if(number == 0):
        return 1
    total = 1
    for i in range(1, number + 1):
        total *= i
    return total
print(factorial(3))

def greet(name =  'Guest'):
    print('Hello, ', name)
greet()
greet('Safor')

named = {'name':'safor', 'age':19}
def show_args(args):
    for key, v in args.items():
        print(f'Received: {key} : {v}')
show_args(named)

1a = 0
print(1a.isidentifier())
