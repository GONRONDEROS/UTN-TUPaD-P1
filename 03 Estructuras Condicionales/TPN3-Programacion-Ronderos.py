# Actividades
    # 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
    # deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input('Por favor, ingrese su edad: '))
if edad > 18:
    print('Es mayor de edad')

    # 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
    # mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
    # mensaje “Desaprobado”.

nota = int(input('Por favor, ingrese su nota: '))
if nota >= 6:
    print('Aprobado')
else:
    print('Desaprobado')

    # 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
    # número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
    # contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
    # operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input('Por favor ingrese un numero par: '))
if num % 2 == 0:
    print('Ha ingresado un numero par')
else:
    print('Por favor, ingrese un numero par')

    # 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
    # siguientes categorías pertenece:
    #   ● Niño/a: menor de 12 años.
    #   ● Adolescente: mayor o igual que 12 años y menor que 18 años.
    #   ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
    #   ● Adulto/a: mayor o igual que 30 años.

edad =int(input('Ingrese su edad: '))
if edad < 12:
    print('Niño/a')
elif 12 <= edad < 18:
    print('Adolescente')
elif 18 <= edad < 30:
    print('Adulto/a joven')
else:
    print('Adulto/a')

    # 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
    # (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
    # pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
    # pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
    # de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
    # como una lista o un string.

contrasena = input('Ingrse una contraseña de entre 8 y 14 caracteres: ')
if 8 <= len(contrasena) <= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')

    # 6)

import random
from statistics import mode, median, mean
numeros_aleatorios = {random.randint(1,100) for i in range(50)}
if (mean(numeros_aleatorios) and mode(numeros_aleatorios) and median(numeros_aleatorios)):
    print('Sin sesgo')
elif ((mean(numeros_aleatorios) > median(numeros_aleatorios)) and (median(numeros_aleatorios) > mode(numeros_aleatorios))):
    print('Sesgo positivo o a la derecha')
else:
    print('Sesgo negativo o a la izquierda')

    # 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
    # termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
    # pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
    # pantalla.

frase = input('Ingrese una frase o palabra: ')
listaDeCaracteres = list(frase)
ultimoCaracter = listaDeCaracteres[-1]
if (ultimoCaracter == 'a' or ultimoCaracter == 'e' or ultimoCaracter == 'i' or ultimoCaracter == 'o' or ultimoCaracter == 'u'):
    print(f'{frase}'+'!')
else:
    print(f'{frase}')

    # 8)

nombre = input('Escriba su nombre: ')
opcion = input('Escriba opcion 1, 2 o 3: ')
if opcion == '1':
    print(nombre.upper())
elif opcion == '3':
    print(nombre.title())
else:
    print(nombre.lower())

# 9)

magnitud = float(input('Ingrese magnitud del terremoto: '))
if magnitud < 3:
    print('Muy Leve (Imperceptible)')
elif 3 <= magnitud < 4:
    print('Leve (ligeramente perceptible)')
elif 4 <= magnitud < 5:
    print('Moderado (sentido por personas, pero generalmente no causa daños)')
elif 5 <= magnitud < 6:
    print('"Fuerte" (puede causar daños en estructuras débiles)')
elif 6 <= magnitud < 7:
    print('"Muy Fuerte" (puede causar daños significativos)')
else:
    print('"Extremo" (puede causar graves daños a gran escala)')

# 10) 

hemis = input('En que hemisferio se encuentra? N = Norte, S = Sur: ')
mes = int(input('En que numero de mes se encuentra?: '))
dia = int(input('Que numero del mes es?: '))
hem = hemis.upper()

if hem == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif hem == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha no válida"
else:
    estacion = "Hemisferio no reconocido"

print("La estación es:", estacion)


