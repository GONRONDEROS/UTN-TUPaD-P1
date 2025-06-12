'''
# Actividades

#1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
print(precios_frutas)

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

#2
precios_frutas.update({'Banana': 1330, 'Manzana': 1700, 'Melón': 2800})
print(precios_frutas)

#3
lista_frutas = ['Banana', 'Ananá', 'Melón', 'Uva', 'Naranja', 'Manzana', 'Pera'] 
'''
#4

def agenda():
    agenda_telefonica = {}
    n = 2
    for i in range(n):
        nombre = input('Por favor ingrese el nombre del contacto a agendar: ')
        nombre_upper = nombre.upper()
        print('=============================================================')
        print(f'Usted a ingresado {nombre_upper}')
        print('=============================================================')
        telefono = input(f'Por favor ingrese el telefono de contacto de {nombre} a agendar: ')
        print('=============================================================')
        print(f'Usted a ingresado {telefono}')
        print('=============================================================')
        print(f'El contacto {nombre} se ha agendado con el telefono: {telefono}')
        agenda_telefonica.update({nombre_upper: telefono})
        print(f'La memoria permite ingresar {n-len(agenda_telefonica)} contactos adicionales.')
        print('=============================================================')
    consulta(agenda_telefonica)

def consulta(agenda):
    nombre_a_consultar = input('Ingrese el Nombre de pila de la persona a consultar el numero de telefono: ')
    nombre_upper = nombre_a_consultar.upper()
    tel = agenda[nombre_upper]
    print(f'El numero de telefono del contacto {nombre_a_consultar} es: {tel}')
    print('#################################################################')

agenda()

