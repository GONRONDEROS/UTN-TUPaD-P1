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

