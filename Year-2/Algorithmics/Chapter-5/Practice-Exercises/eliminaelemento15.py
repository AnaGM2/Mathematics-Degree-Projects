# Función que elimina todos los elementos con el valor especificado de una matriz dada por parámetro.

def elimina_elemento(M, elem):
    for nfila in range(len(M)):
        while elem in M[nfila]:
            M[nfila].remove(elem)
    return M


# Función que devuelve una copia de la matriz dada por parámetro sin los elementos con el valor especificado.

def elimina_elemento_copia(M, elem):
    Msinelem = []
    for nfila in range(len(M)):
        fila = []
        for ncolumna in range(len(M[nfila])):
            if M[nfila][ncolumna] != elem:
                fila.append(M[nfila][ncolumna])
        Msinelem.append(fila)
    return Msinelem


A = [
[3, 8, 8],
[0, 6, 9],
[3, 1, 6],
[1, 1, 6]
]
print(elimina_elemento(A, 6))

B = [
[3, 8, 8],
[0, 6, 9],
[3, 1, 6],
[1, 1, 6]
]
print(elimina_elemento_copia(B, 6))
