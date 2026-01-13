# Función que devuelve la intersección de las filas de una matriz.

def interseccion_filas(M):
    interseccion = []
    for elem in M[0]:
        nfila = 1
        pertenece = True
        while nfila < len(M):
            if elem not in M[nfila] or elem in interseccion:
                pertenece = False
                break
            nfila += 1
        if pertenece:
            interseccion.append(elem)
    return interseccion


A = [
[0, 1, 2, 4, 4, 5, 6, 7, 9],
[0, 4, 9],
[2, 4, 5, 6, 7, 8, 9],
[0, 1, 2, 4, 5, 6, 8, 9]
]

print(interseccion_filas(A))
