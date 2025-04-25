#ACTIVIDADES
#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

numeros_multiplos_de_4 = list(range(4,101,4))
print(numeros_multiplos_de_4)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

lista_de_5_elementos = [['Estudiantes de La Plata', 'Campeon del Mundo'], 'Veron', 11, 'Bilardo', 'Leon']
penultimo_elemento = lista_de_5_elementos[-2]
print(penultimo_elemento)

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo:
# lista_vacia = []

lista_vacia = []
lista_vacia.append('Estudioooo')
lista_vacia.append('Gooool!!!')
lista_vacia.append('Libertadores')
print(lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
# animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]
animales[1]='loro'
animales[3]='oso'
print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# El programa realiza los siguientes pasos:
# Definición de la lista: Crea una lista llamada numeros con los valores [8, 15, 3, 22, 7].
# Encontrar el valor máximo: La función max(numeros) encuentra el valor máximo de la lista, que en este caso es 22.
# Eliminar el valor máximo: La función numeros.remove(max(numeros)) elimina el primer elemento de la lista que coincide con el valor máximo, que en este caso es 22.

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

