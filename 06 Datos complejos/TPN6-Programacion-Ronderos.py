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

#5

frase = input("Ingresá una frase: ")
palabras = frase.split()

unicas = set(palabras)
print("Palabras únicas:", unicas)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Recuento:", recuento)

#6

alumnos = {}

for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingresá la nota {i+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} tiene un promedio de {promedio:.2f}")

#7

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

#8

productos = {
    "manzanas": 20,
    "bananas": 30,
    "naranjas": 13
}

producto = input("Ingresá el nombre del producto: ")

if producto in productos:
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    productos[producto] += agregar
    print(f"Nuevo stock de {producto}: {productos[producto]}")
else:
    nuevo_stock = int(input("Producto nuevo. Ingresá el stock inicial: "))
    productos[producto] = nuevo_stock
    print(f"Producto {producto} agregado con {nuevo_stock} unidades.")

#9 
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (ej: 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividades programadas.")


#10

paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}

invertido = {}

for pais, capital in paises.items():
    invertido[capital] = pais

print("Diccionario original:", paises)
print("Diccionario invertido:", invertido)
