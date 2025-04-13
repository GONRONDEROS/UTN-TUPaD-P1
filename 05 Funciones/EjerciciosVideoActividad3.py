# Definicion de funciones
def leer_entero_valido(mensaje, min = float('-Inf'), max = float('Inf')):
    n = int(input(f'{mensaje}'))
    while n < min or n > max:
        n = int(input(f'ERROR. {mensaje}'))
    return n

def informar_si_numero_es_perfecto(numero):
    if es_perfecto(numero):
        print(f'El numero {numero} es perfecto')
    else:
        print(f'El nmero {numero} MO es perfecto')
        
def es_perfecto(numero):
    aSumar = 0
    while numero > 1:
        for i in range(1, numero):
            if numero % i == 0:
                aSumar = aSumar + i
            return aSumar
    if aSumar == numero:
        return True
    else: 
        return False


# Programa Principal
num = leer_entero_valido('Ingrese un numero natural', 1)
informar_si_numero_es_perfecto(num)
