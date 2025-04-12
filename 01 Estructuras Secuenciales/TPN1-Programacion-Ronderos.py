#Actividades
#Ej 1
print('Ejercicio 1')
print('hola Mundo!')

#Ej 2
nombre = input(f'Cual es su nombre? ')
print(f'Hola {nombre}!')

#Ej 3
nombre, apellido, edad, residencia = input(f'Cual es su nombre? '), input(f'Cual es su apellido? '), int(input(f'Cual es su edad? ')), input(f'Cual es su residencia? ')
print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}!')

#Ej 4
radio = float(input('Por favor ingrese el radio del circulo: '))
pi = 3.14
area = float(pi * radio * radio)
perimetro = float(2 * pi * radio)
print(f'El Area del circulo es {area} y el perimetro de la misma es {perimetro}')

#Ej 5
segundos = int(input('Ingrese una cantidad de segundos: '))
horas = segundos / 3600
print(f'{segundos} segundos equivalen a {horas:.2f} horas')
    
#Ej 6
num = int(input('Ingrese un numero: '))
n0 = num * 0
n1 = num
n2 = num * 2
n3 = num * 3
n4 = num * 4
n5 = num * 5
n6 = num * 6
n7 = num * 7
n8 = num * 8
n9 = num * 9
n10 = num * 10
print(f'Tabla de multiplicar del {num}: \n{n0}\n{n1}\n{n2}\n{n3}\n{n4}\n{n5}\n{n6}\n{n7}\n{n8}\n{n9}\n{n10}')

#Ej 7
num1 = float(int(input('Ingrese numero 1: ')))
num2 = float(int(input('Ingrese numero 2: ')))
sum = float(int(num1 + num2))
resta = float(int(num2 - num1))
multi = float(int(num1 * num2))
div = float(int(num1 / num2))
if (num1 != 0 and num2 != 0): 
    print(f'Suma = {sum}\nResta = {resta}\nMultiplicacion = {multi}\nDivision = {div} ')
else:
    print('Los numeros ingresados no pueden ser 0')


#Ej 8
altura = (float(input('Ingrese su altura en cm: '))/100)
peso = float(input('Ingrese su altura en kgs: '))
imc = (peso)/(altura ** 2)
print(f'Su IMC es de: {imc}')


#Ej 9
cel = float(input('Ingrese temperatura en grados celcius: '))
far = float(((9/5)*cel)+32)
print(f'El equivalente en grados Farenheit es: {far}')


#Ej 10
num1, num2, num3 = float(input('Ingrese numero 1: ')), float(input('Ingrese numero 2: ')), float(input('Ingrese numero 3: '))
prom = float((num1+num2+num3)/3)
print(f'El promedio de los numeros es: {prom}')
