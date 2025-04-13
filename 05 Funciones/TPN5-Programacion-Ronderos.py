# ACTIVIDADES 

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

#Definicion de Funciones
def imprimir_hola_mundo():
    print('Hola Mundo!')

#Programa Principal
imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

#Definicion de Funciones
def saludar_usuario(nombre):
    print(f'Hola {nombre}!')

#Programa Principal
nombre = input('Por favor ingrese su nombre: ')
saludar_usuario(nombre)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#Definicion de Funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

#Programa Principal
nombre = input('Por favor ingrese su nombre: ')
apellido = input('Por favor ingrese su apellido: ')
edad = input('Por favor ingrese su edad: ')
residencia = input('Por favor ingrese su residencia: ')
informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones:
# calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

#Definicion de Funciones
def calcular_area_circulo(radio):
    area = 3.14 * radio**2
    print(f'El Area de la cirucunsferencia es {area}')
def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    print(f'El Perimetro de la cirucunsferencia es {perimetro}')

#Programa Principal
radio = int(input('Por favor ingrese el radio de la circunsferencia: '))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)





