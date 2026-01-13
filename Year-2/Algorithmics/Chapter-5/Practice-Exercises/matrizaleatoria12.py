from random import random


# Función que genera una matriz aleatoria.

def matriz_aleatoria(nfilas, ncol, maxvalor):
    M = []
    for f in range(nfilas):
        fila = []
        for c in range(ncol):
            fila.append(round(random() * maxvalor, 4))
        M.append(fila)
    return M


print("La matriz generada es: " + str(matriz_aleatoria(3, 4, 100)))
