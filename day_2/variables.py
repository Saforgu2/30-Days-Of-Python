# Day 2: 30 Days of python programming

first_name = 'Saforgu'
last_name = 'Saforgu2'
full_name = 'Saforgu Saforgu2'
country = 'Sapin'
city = 'Albacete'
age = 99
year = 2026
is_married = False
is_light_on = True
is_true = False
is_alive, birth_year = True, 2006

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(birth_year))
print(type(is_alive))

print(len(first_name))
print(len(first_name) > len(last_name))

num_one, num_two = 5, 4
num_sum = num_one + num_two
num_sub = num_one - num_two
num_mult = num_one * num_two
num_div = num_one / num_two
num_mod = num_two % num_one
num_pw = num_one ** num_two
num_div_down = num_one // num_two

print(num_sum)
print(num_sub)
print(num_mult)
print(num_div)
print(num_mod)
print(num_pw)
print(num_div_down)

radius = 30
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2 * 3.14 * radius

print('Raidus: ', radius)
print('area_of_circle: ', area_of_circle)
print('circum_of_circle: ', circum_of_circle)

user_radius = input('User radius: ')

user_area = 3.14 * (int(user_radius) ** 2)

print('User area: ', user_area)

help('keywords')
