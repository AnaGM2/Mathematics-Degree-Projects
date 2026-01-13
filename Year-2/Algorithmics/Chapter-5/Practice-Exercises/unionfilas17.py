# Función que devuelve la unión de las filas de una matriz sin repetir números.

def union_filas(M):
    union = []
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] not in union:
                union.append(M[i][j])
    return union


A = [
[0, 1, 2, 5, 6, 7, 9],
[0, 4, 9],
[2, 4, 5, 6, 7, 8, 9],
[0, 1, 2, 5, 6, 8, 9]
]
print(union_filas(A))
