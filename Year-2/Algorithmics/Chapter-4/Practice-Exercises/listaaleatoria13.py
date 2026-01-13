from random import randint

# Función que devuelve una lista aleatoria de enteros del tamaño indicado.


def crear_lista_aleatoria(size, ini, fin):
    lista = []
    for elemento in range(size):
        numero = randint(ini, fin)
        lista.append(numero)
    return lista


print(crear_lista_aleatoria(9, 3, 7))
