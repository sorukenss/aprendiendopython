
#diccionarios 

my_dict = dict()

my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict= {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(len(my_other_dict))
print(my_other_dict['first_name'])
print(my_other_dict['skills'])
print(my_other_dict['skills'][0])

print(my_other_dict['age'])
# add nuevo valor a esa propiedad
my_other_dict['age'] = 500

print(my_other_dict['age'])

# crear un nuevo campo dentro del diccionario
my_other_dict['job_title'] = 'teacher'
print(my_other_dict)

#add nuevo valor a una lista dentro del diccionario 

my_other_dict['skills'].append('HTML')
print(my_other_dict['skills'])

del my_other_dict['age']

print(my_other_dict)

print(my_other_dict.values())



