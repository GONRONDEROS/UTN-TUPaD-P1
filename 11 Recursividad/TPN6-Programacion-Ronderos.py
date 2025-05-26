## ACTIVIDADES ##

#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num -1)

print(f'Resultado de Prueba de Factorial de 4: {factorial(4)}')

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

def fibo(pos):
    if pos <= 0:
        return 0
    elif pos == 1:
        return 1
    return fibo(pos-1)+fibo(pos-2)

print(f'Resultado de Prueba de Fibonacci de 3: {fibo(3)}')

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛**𝑚 = (𝑛) ∗ (𝑛)**(m-1). Prueba esta función en un
#algoritmo general.

def potencia(base,pot):
    if base == 0 and (pot == 0 and pot < 0):
        return 'Indefinido'
    if pot == 0: # Caso Base
        return 1
    return base * potencia(base,pot-1)

print(f'Resultado de Prueba de Potencia de base 2 potencia 3: {potencia(2,3)}')

#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(base_decimal):
    if base_decimal == 0: # Caso Base
        return ''
    resto = base_decimal % 2
    return decimal_a_binario(base_decimal // 2) + str(resto)
    
print(f'Resultado de Decimal A Binario con decimal = 10: {decimal_a_binario(10)}')

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.
#Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().

def tildes(palabra_a_revisar):
    array_de_palabra = list(palabra_a_revisar)
    tildes = ['á','é','í','ó','ú','Á','É','Í','Ó','Ú']
    for i in range(len(tildes)):
        for j in range(len(array_de_palabra)):
            if array_de_palabra[j] == tildes[i]:
                print('Caracter Invalido')
    for letra in array_de_palabra:
        if letra == ' ':
            print('No se admiten espacios')             
    return False
    
def es_palindromo(palabra):
    if tildes(palabra) == False:
        array_de_palabra = list(palabra)
        if len(array_de_palabra) <= 1: # Si el array tiene un elemento o menos, es palindromo por def
            return True
        if array_de_palabra[0] != array_de_palabra[-1]:
            return False
        return es_palindromo(array_de_palabra[1:-1]) # ya habiendo chequeado el primer elemento, comenzamos desde el segundo (indice = 1) y eliminamos al mismo tiempo el ultimo (:-1)

print(es_palindromo('oso'))
print(es_palindromo('osé'))
print(es_palindromo('auto'))
print(es_palindromo('reconocer'))

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.
#Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.
#Ejemplos:
#suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
#suma_digitos(9) → 9
#suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n == 0:
        return 0
    resto = n % 10
    cociente = n // 10
    return resto + suma_digitos(cociente)

print(suma_digitos(9))

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide.
#Ejemplos:
#contar_bloques(1) → 1 (1)
#contar_bloques(2) → 3 (2 + 1)
#contar_bloques(4) → 10 (4 + 3 + 2 + 1)


#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.
#Ejemplos:
#contar_digito(12233421, 2) → 3
#contar_digito(5555, 5) → 4 
#contar_digito(123456, 7) → 0 