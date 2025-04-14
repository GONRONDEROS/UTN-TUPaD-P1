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

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#Definicion de Funciones
def segundos_a_horas(segundos):
    horas = float(segundos/60)/60
    print(f'{segundos} segundos son un total de {horas} horas')

#Programa Principal
segundos = int(input('Por favor ingrese la cantidad de segundos: '))
segundos_a_horas(segundos)

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

#Definicion de Funciones
def tabla_multiplicar(numero):
    mult = 0
    for i in range(1,11):
        mult = i * numero
        print(f'2 x {i} = {mult}')

#Programa Principal
num = int(input('Por favor ingrese un numero: '))
tabla_multiplicar(num)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
# Mostrar los resultados de forma clara.

#Definicion de Funciones
def operaciones_basicas(a, b):
    op_basic = ()
    if b != 0:
        op_basic = (suma_basica(a,b), resta_basica(a,b), multiplicacion_basica(a,b), division_basica(a,b))
        print(op_basic)
    else:
        print('El segundo numero no puede ser igual a 0. Por favor ingrese otro numero: ')
        
def suma_basica(a,b):
    return a + b
    
def resta_basica(a,b):
    return a - b

def multiplicacion_basica(a,b):
    return a * b

def division_basica(a,b):
    return a/b

#Programa Principal
a = float(input('Por favor ingrese el primer numero: '))
b = float(input('Por favor ingrese el segundo numero: '))
operaciones_basicas(a,b)

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

#Definicion de Funciones
def calcular_imc(peso, altura):
    imc = (peso / (altura**2))
    print(f'Su IMC es de {imc}')

#Programa Principal
peso = float(input('Por favor ingrese el peso en kg: '))
altura = float(input('Por favor ingrese altura en m: '))
calcular_imc(peso, altura)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

#Definicion de Funciones
def celsius_a_fahrenheit(c):
    f = (c * (9/5)) + 32
    print(f'{c} grados Celsius son {f}')

#Programa Principal
celsius = float(input('Por favor ingrese la temperatura en grados Celsius: '))
celsius_a_fahrenheit(celsius)

# 10. Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

#Definicion de Funciones
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f'El promedio de los numeros ingresados es {promedio}')

#Programa Principal
a = float(input('Por favor ingrese el primer numero: '))
b = float(input('Por favor ingrese el primer numero: '))
c = float(input('Por favor ingrese el primer numero: '))
calcular_promedio(a, b, c)
