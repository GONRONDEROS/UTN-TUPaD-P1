# Actividades
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
'''
for i in range(0,101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = str(int(input('Por favor ingrese un numero entero: ')))
cant = len(num)
print(f'El numero tiene {cant} digitos')

num = int(input('Por favor ingrese un numero entero: '))

numAbs = abs(num)
long = 0

if num == 0:
    long = 1
    print(f'El numero tiene {long} digito')
else:
    while numAbs > 0:
        numAbs //= 10
        long += 1
    print(f'El numero tiene {long} digitos')


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

numA = int(input('Por favor ingrese el primer numero entero: '))
numB = int(input('Por favor ingrese el segundo numero entero: '))

if numA == numB:
    print('Los numeros deben ser diferentes')
elif numA > numB:
    sum = 0
    for i in range(numB+1, numA):
        sum = sum + i
    print(sum)
else:
    sum = 0
    for i in range(numA+1, numB):
        sum = sum + i
    print(sum)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

total = 0
num = int(input('Por favor ingrese un numero entero: '))
while num != 0:
    total += num
    num = int(input('Por favor ingrese un numero entero: '))
print(total)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
aleatorio = random.randint(0,9)
num = int(input('Por favor adivine el numero entre 0 y 9: '))
total2 = 1
while num != aleatorio:
    total2 += 1
    num = int(input('No has acertado! Escoge otro numero entre 0 y 9: '))
print(f'Has acertado! Te tomo un total de {total2} intento/s')

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)
'''
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input('Por favor ingrese un numero entero positivo: '))
sum = 0
for i in range(0, num+1):
    sum += i
print(sum)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).



# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).




# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.