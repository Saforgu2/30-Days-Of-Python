dog = dict()

dog['name'] = 'zeus'
dog['color'] = 'brown'
dog['breed'] = 'german'
dog['legs'] = 4
dog['age'] = 13

student = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'gender':'male',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country':'Spain',
    'city':'Albacete',
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print(len(student))

print(student.get('skills'))
print(type(student.get('skills')))

student.get('skills').append('Java')
student.get('skills').append('SQL')
print(student.get('skills'))

print(student.keys())
print(student.values())

print(student.items())

dog.pop('breed')
print(dog)

del dog
