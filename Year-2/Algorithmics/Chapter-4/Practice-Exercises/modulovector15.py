from math import sqrt
from listas import introducir_lista

# Función que calcula el módulo de un vector de dimensión n.


def modulo_lista(vector):
    prod = 0
    for i in range(len(vector)):
        prod += vector[i]**2
    return sqrt(prod)


print(modulo_lista(introducir_lista()))
