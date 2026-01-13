# Función que devuelve la traspuesta de una matriz.

def traspuesta(M):
    Mtraspuesta = []
    for i in range(len(M[0])):
        Mtraspuesta.append([])
    for nfila in range(len(M)):
        for ncolumna in range(len(M[nfila])):
            Mtraspuesta[ncolumna].append(M[nfila][ncolumna])
    return Mtraspuesta


A =[
[2, 8, 4],
[7, 6, 5],
[1, 0, 9],
]
print(traspuesta(A))
B =[
[3, 8, 8],
[0, 6, 9],
[3, 1, 6],
[1, 1, 6]
]
print(traspuesta(B))
