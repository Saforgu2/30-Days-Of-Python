# DAY 9
# LEVEL 1

age = input('Enter your age: ')
age = int(age)
if(age >= 18):
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18-age} more years to learn to drive.')

my_age = 19
your_age = input('Enter your age: ')
your_age = int(your_age)
if(my_age > your_age):
    if((my_age - your_age) == 1):
        diff = 'year'
    else:
        diff = 'years'
    print(f'I am {my_age - your_age} {diff} older than you.')
elif(my_age < your_age):
    if((your_age - my_age) == 1):
        diff = 'year'
    else:
        diff = 'years'
    print(f'You are {your_age - my_age} {diff} older than me.')
else:
    print('We are of the same age.')

a = input('Ente number one: ')
a = int(a)
b = input('Ente number two: ')
b = int(b)
if(a > b):
    print(f'{a} is greater than {b}.')
elif(a < b):
    print(f'{b} is greater than {a}.')
else:
    print('They are equal.')

score = input('Enter your score: ')
score = int(score)
if(score <= 100 and score >= 90):
    print('A')
elif(score <= 89 and score >= 80):
    print('B')
elif(score <= 79 and score >= 70):
    print('C')
elif(score <= 69 and score >= 60):
    print('D')
else:
    print('F')

# LEVEL 3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if('skills' in person):
    print('Middle skill: ', person.get('skills')[(len(person.get('skills')) - 1) // 2])
    print('It contains Python.') if('Python' in person.get('skills')) else print('It does not contain Python.')

if(person.get('is_married')):
    print(f'{person.get('first_name')} {person.get('last_name')} lives in {person.get('country')}. He is married')
