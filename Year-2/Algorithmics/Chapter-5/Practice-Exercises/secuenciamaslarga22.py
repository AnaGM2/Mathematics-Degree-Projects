from matrices import elem_consecutivos, traspuesta


# Función que devuelve una matriz dada la vuelta.

def vuelta_matriz(M):
    M_vuelta = []
    for n_fila in range(len(M)):
        fila_vuelta = []
        for n_columna in range(len(M[n_fila])-1, -1, -1):
            fila_vuelta.append(M[n_fila][n_columna])
        M_vuelta.append(fila_vuelta)
    return M_vuelta


# Función que devuelve la longitud de la mayor secuencia de números iguales
# en una matriz (en vertical, horizontal o diagonal).

def secuencia_mas_larga(M):
    longitud = 1

    for n_fila in range(len(M)):
        if elem_consecutivos(M[n_fila]) > longitud:
            longitud = elem_consecutivos(M[n_fila])

    for n_columna in range(len(traspuesta(M))):
        if elem_consecutivos(traspuesta(M)[n_columna]) > longitud:
            longitud = elem_consecutivos(traspuesta(M)[n_columna])

    for n_diagonal in range(len(M) + len(M[0]) - 1):
        diagonal = []
        for nfila in range(len(M)):
            for ncolumna in range(len(traspuesta(M))):
                if nfila + ncolumna == n_diagonal:
                    diagonal.append(M[nfila][ncolumna])
        if elem_consecutivos(diagonal) > longitud:
            longitud = elem_consecutivos(diagonal)

    for n_diagonal_vuelta in range(len(M) + len(M[0]) - 1):
        diagonal = []
        for nfila_vuelta in range(len(M)):
            for ncolumna_vuelta in range(len(traspuesta(M))):
                if nfila_vuelta + ncolumna_vuelta == n_diagonal_vuelta:
                    diagonal.append(vuelta_matriz(M)[nfila_vuelta][ncolumna_vuelta])
        if elem_consecutivos(diagonal) > longitud:
            longitud = elem_consecutivos(diagonal)

    return longitud


A = [
[5, 4, 1, 2, 8, 8, 1],
[6, 4, 1, 3, 7, 5, 2],
[7, 6, 4, 4, 5, 1, 3],
[6, 6, 2, 1, 6, 2, 4],
[5, 1, 2, 2, 1, 2, 1],
[4, 3, 1, 2, 2, 1, 1]
]

print(vuelta_matriz(A))

print(secuencia_mas_larga(A))
