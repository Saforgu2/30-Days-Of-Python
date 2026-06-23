# DAY 4

message = ['Thirty', 'Days', 'Of', 'Python']
concatenation = ' '.join(message)
print(concatenation)

message = ['Coding', 'For', 'All']
concatenation = ' '.join(message)
print(concatenation)

company = concatenation
print(company)
print(len(company))

print(concatenation.upper())
print(concatenation.lower())

print(concatenation.capitalize())
print(concatenation.title())
print(concatenation.swapcase())

print(concatenation.strip('Coding'))

print(concatenation.index('Coding'))
print(concatenation.find('Coding'))

print(concatenation.replace('Coding', 'Python'))

print(concatenation.split(' '))

print(concatenation[0])

print(len(concatenation) - 1)

print(concatenation[10])

for i in concatenation:
    print(i)

print(concatenation.index('C'))

print(concatenation.index('F'))

print(concatenation.rfind('l'))

new_message = 'You cannot end a sentence with because because because is a conjunction'
print(new_message.index('because'))

print(new_message.rindex('because'))

print(new_message.replace(' because because because ', ' '))

print(concatenation.startswith('Coding'))
print(concatenation.startswith('coding'))

print('I am enjoying this challenge.\nI just wonder what is next.')

print('Name\t Age\tCountry\tCity')
print('Asabeneh\t 250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
message = 'The area of a circle with radius {} is {:.0f} meters square'.format(radius, area)
print(message)

a = 8
b = 6

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
