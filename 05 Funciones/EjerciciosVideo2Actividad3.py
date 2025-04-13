import utils
# Definicion de funciones
def imprimir_matriz_de_simbolos(num_de_columnas, num_de_filas, simbolo = 'X'):
    for i in range(num_de_filas):
        utils.imprimir_simbolo(simbolo, num_de_columnas)




# Programa principal

ancho = utils.leer_entero_valido('Ingrese el Ancho: ', 1)
alto = utils.leer_entero_valido('Ingrese el Alto: ', 1)
imprimir_matriz_de_simbolos(ancho, alto, '5')
