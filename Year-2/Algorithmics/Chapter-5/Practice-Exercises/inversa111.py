from matrices import adjunta, determinante


# Función que devuelve la inversa de una matriz.

def inversa(M):
    inv = []
    for i in range(len(M)):
        fila = []
        for j in range(len(M[i])):
            fila.append(adjunta(M)[i][j] / determinante(M))
        inv.append(fila)
    return inv


print(inversa([[1, 2, 3], [0, 1, 4], [0, 0, 1]]))
