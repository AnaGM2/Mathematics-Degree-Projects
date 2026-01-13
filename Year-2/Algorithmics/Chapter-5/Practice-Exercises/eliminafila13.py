from matrices import matriz_aleatoria


# Función que elimina la fila i-ésima de una matriz dada por parámetro.

def elimina_fila(M, i):
    del M[i]
    return M


# Función que devuelve una copia de la matriz dada por parámetro sin la fila i-ésima.

def elimina_fila_copia(M, i):
    Msinfila = []
    for nfila in range(len(M)):
        if nfila != i:
            Msinfila.append(M[nfila])
    return Msinfila


print(elimina_fila(matriz_aleatoria(3, 4, 100), 2))
print(elimina_fila_copia(matriz_aleatoria(3, 4, 100), 2))
