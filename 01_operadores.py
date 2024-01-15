
#operadores 

print('sumar : 3 + 4 =',3+4)
print('resta : 3 - 4 =',3-4)
print('division : 3 / 4 =',3/4)
print('division modelada, se paroxima a un numero entero : 10 // 3 =',10//3)
print('multiplicacion : 3 * 4 =',3*4)
print('residuo de la division : 2%8 =',2%8)
print('calcular un exponente : 2 ** 3 =',2 ** 3)


# declaracion 
a = 2
b = 3

print('suma de a +b =', a +b )
print('resta de a - b =', a - b )
print('division de a / b =', a / b )
print('division aproximada a un entero de a // b =', a // b )
print('calcular exponenete de a ** b =', a ** b )
print('residuo de la division de a % b =', a % b )
print('multiplicacion de a * b =', a * b )

# string 

# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

# format para pintar 
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)

print(f'I am {first_name} {last_name}. I teach {language}')

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')