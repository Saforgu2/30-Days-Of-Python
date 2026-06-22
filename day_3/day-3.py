# DAY 3

age = 19
height = 173.1
num_complex = (2 + 3j)

print('Age: ', age)
print('Height: ', height)
print('Complex: ', num_complex)

base = input('Enter Triange Base: ')
tri_height = input('Enter Triange Height: ')

print('Triangle area: ', 0.5 * float(base) * float(tri_height))

for i in range(6):
    if((i**2 + 6*(-i) + 9) == 0):
        print("x = ", i)
        break

print('Dragon: ', len('dragon'))
print('Python: ', len('python'))
print(True == False)

py_len = len('python')

print('Float: ', float(py_len))
print('String: ', str(py_len))

# if modulus %2 is 0 then is even if not the prime

print((7 // 2) == int(2.7))

print(40 * 2.1)

for i in range(1, 6):
    message = str(i)
    for j in range(1, 5):
        if j == 1:
            bide = j
        else:
            bide = bide * i
        message += ' ' + str(bide)
    print(message)            
