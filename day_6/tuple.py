# DAY 6
# LEVERL 1
empty = tuple()
print(empty)

brothers = ('Peter', 'John', 'Robert')
sisters = ('Emily', 'Nataly')
print(brothers)
print(sisters)

siblings = brothers + sisters
print(siblings)

print(len(siblings))

siblings = list(siblings)
siblings.append('Jose Luis')
siblings.append('Maria')
siblings = tuple(siblings)
family_members = siblings
print(family_members)

# LEVEL 2
siblings = family_members[0:5]
parents = family_members[5:]
print(siblings)
print(parents)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('Meat', 'Milk', 'Cheese', 'Yogurt')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

middle = (len(food_stuff_tp) - 1) // 2
print(len(food_stuff_tp) - 1)
if((len(food_stuff_tp) - 1) % 2 == 0):
    print(food_stuff_tp[middle:middle + 2])
else:
    print(food_stuff_tp[middle:middle + 1])

sliced = food_stuff_lt[0:3] + food_stuff_lt[-3:]
print(sliced)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
