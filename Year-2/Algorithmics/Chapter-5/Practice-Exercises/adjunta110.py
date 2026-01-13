from matrices import determinante, traspuesta, elimina_fila_copia, elimina_columna_copia


# Función que devuelve la adjunta de una matriz.

def adjunta(M):
    Mcof = []
    for i in range(len(M)):
        fila = []
        for j in range(len(M[i])):
            cofactor = (-1) ** (i+j) * determinante(elimina_fila_copia(elimina_columna_copia(M, j), i))
            fila.append(cofactor)
        Mcof.append(fila)
    return traspuesta(Mcof)


print(adjunta([[1, 0, 2], [0, 3, 0], [4, 0, 5]]))
