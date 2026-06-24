empty = list()
items = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8', 'item9', 'item10']

print(len(items))
print(f'{items[0]}     {items[(len(items) - 1) // 2]}     {items[len(items) - 1]}')

mixed = ['Safor', 400, 172, False, 'DB']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)
print(len(it_companies))

print(f'{it_companies[0]}     {it_companies[(len(it_companies) - 1) // 2]}     {it_companies[len(it_companies) - 1]}')

it_companies[0] = 'Twitter'
print(it_companies)

it_companies.append('Facebook')
print(it_companies)

it_companies.insert((len(it_companies) - 1) // 2, 'asml') 
print(it_companies)

it_companies[it_companies.index('asml')] = it_companies[it_companies.index('asml')].upper()
print(it_companies)

joined = '# '.join(it_companies)
print(joined)
print(it_companies)

print('ASML' in it_companies)

lst_sorted = it_companies.copy()
print(lst_sorted)
lst_sorted.sort()
print(lst_sorted)

lst_sorted.reverse()
print(lst_sorted)

print(it_companies[3:])

print(it_companies[-len(it_companies):-3])

middle = (len(it_companies) - 1) // 2
sliced = it_companies[0:middle] + it_companies[middle + 1:]
print(sliced)

it_companies.pop(0)
print(it_companies)

it_companies.pop((len(it_companies) - 1) // 2)
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

# LEVEL 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

print(ages)

ages.sort()
print(ages)

ages.append(ages[len(ages) - 1])
ages.insert(0, ages[0])
print(ages)
