from recursividad import elimina_fila_copia, elimina_columna_copia


# Función que calcula el determinante de una matriz de forma recursiva.

def determinante(M):
    if len(M) == 1:
        det = M[0][0]

    elif len(M) == 2:
        det = M[0][0] * M[1][1] - M[1][0] * M[0][1]

    elif len(M) == 3:
        derecho = M[0][0] * M[1][1] * M[2][2] + M[0][1] * M[1][2] * M[2][0] + M[1][0] * M[2][1] * M[0][2]
        reves = M[0][2] * M[1][1] * M[2][0] + M[0][1] * M[1][0] * M[2][2] + M[1][2] * M[2][1] * M[0][0]
        det = derecho - reves

    else:
        det = 0
        for ncolumna in range(len(M[0])):
            det += M[0][ncolumna] * (-1) ** ncolumna * determinante(elimina_fila_copia(elimina_columna_copia(M, ncolumna), 0))

    return det


A = [[9]]
print(determinante(A))

B = [[3, 2], [-5, 7]]
print(determinante(B))

C = [[9, 4, 1], [5, 2, 7], [3, 8, 6]]
print(determinante(C))

D = [[1, 0, 3, -3, 2], [2, -3, -2, 3, 6], [-1, 2, 1, 2, 7], [3, 2, 5, 0, 1], [9, 2, 4, 0, 7]]
print(determinante(D))
