
# funciones 

def area_de_cuadrado(ancho,altura):
        return ancho * altura
print(area_de_cuadrado(2,5))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        print('i: ',i)
        total+=i
        print('total :',total)
    print(total)
print(sum_of_numbers(10)) # 55