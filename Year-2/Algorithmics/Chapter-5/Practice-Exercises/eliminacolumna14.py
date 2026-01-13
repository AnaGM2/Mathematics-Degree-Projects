from matrices import matriz_aleatoria


# Función que elimina la columna i-ésima de una matriz dada por parámetro.

def elimina_columna(M, i):
    for nfila in range(len(M)):
        del M[nfila][i]
    return M


# Función que devuelve una copia de la matriz dada por parámetro sin la columna i-ésima.

def elimina_columna_copia(M, i):
    Msincolumna = []
    for nfila in range(len(M)):
        fila = []
        for ncolumna in range(len(M[nfila])):
            if ncolumna != i:
                fila.append(M[nfila][ncolumna])
        Msincolumna.append(fila)
    return Msincolumna


print(elimina_columna(matriz_aleatoria(3, 4, 100), 2))
print(elimina_columna_copia(matriz_aleatoria(3, 4, 100), 2))
