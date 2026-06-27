# DAY 7
# sets
# LEVER 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['ASML', 'Alphabet', 'TSMC'])
print(it_companies)

it_companies.remove('Facebook')
print(it_companies)

# If the item is not in the set it raises an error (remove), however, discard doesnt

# LEVEL 2

print(A.union(B))

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))

del A
del B

# LEVEL 3

ages = set(age)

# STRING: a chain of characters (an arry of characters)
# LIST: Used to store multiple items in a variable, is ordered and indexed ant in can be changed (remove, add, replace)
# TUPLE:  Used to store multiple items in a variable is ordered and indexed, but it cant be changed (remove, add,
#         but can an item cant be replaced)
# SET: Used to store multiple items in a variable is not ordered and is un-indexed, it  but it cant be changed (remove, add,
#         but can an item cant be replaced)

phrase = 'I am a teacher and I love to inspire and teach people'
phrase = phrase.split()
print(phrase)
phrase = set(phrase)
print(len(phrase))
