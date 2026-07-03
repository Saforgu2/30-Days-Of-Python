
# DAY 13
# LEVEL 1

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
non_negative = [i for i in numbers if(i > 0)]
print(non_negative)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [number for i in list_of_lists for number in i]
print(flatten)

list_of_tuples = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5,) for i in range(11)]
print(list_of_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
counties_flatten = [[j[0].upper(), j[0][:3].upper(), j[1].upper()] for i in countries for j in i]
print(counties_flatten)

counties_dict = [{'country':j[0].upper(), 'city':j[1].upper()} for i in countries for j in i]
print(counties_dict)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [j[0] + ' ' + j[1] for i in names for j in i]
print(full_names)

slope = lambda x1, y1, x2, y2 : (y2 - y1) / (x2 - x1)
print(slope(0, 0, 2, 1))

y_intercept = lambda a, b : a*0 
