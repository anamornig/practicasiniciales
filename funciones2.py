#1) Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura
def area_rectangulo(base, altura):
    return (base * altura)/2

print(area_rectangulo(15,10))

#2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio

import math
print(math.pi)


def area_circulo(radio):
    return (radio*radio)*math.pi

print(area_circulo(5))

#3) Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

#Si el primer número es mayor que el segundo, debe devolver 1.
#Si el primer número es menor que el segundo, debe devolver -1.
#Si ambos números son iguales, debe devolver un 0.

#Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

def relacion(num1,num2):
    if num1>num2:
        return 1
    elif num1<num2:
        return -1
    else:
        return 0

print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))

#4) Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:
#Comprueba el punto intermedio entre -12 y 24

def intermedio(num1,num2):
    return (num1+num2)/2
print(intermedio(-12,24))

#5) Realizá una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

#Devolver el límite inferior si el número es menor que éste
#Devolver el límite superior si el número es mayor que éste.
#Devolver el número sin cambios si no se supera ningún límite.
#Comprueba el resultado de recortar 15 entre los límites 0 y 10

def recortar(num,limiteinf,limitesup):
    if num <limiteinf:
        return limiteinf
    if num>limitesup:
        return limitesup
    else:
        return num

print(recortar(15,0,10))


#6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:

def separar(lista):
pares=[]
impares=[]
    for num in lista:
        if num%2 ==0:
            pares.append(num)
        else:
            impares.append(num)

    pares.sort()
    impares.sort()
    return pares, impares

lista=[6,4,2,87,342,34,67,23,12,11,64,90,467]
pares, impares= separar(lista)
print(pares)
print(impares)

