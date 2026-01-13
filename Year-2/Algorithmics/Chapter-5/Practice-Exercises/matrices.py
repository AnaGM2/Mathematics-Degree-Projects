from random import random, randint


# Función que indica si los elementos de una cadena son un número entero.

def es_numero(cadena):
    numero = True
    for caracter in cadena:
        if caracter not in "0123456789":
            numero = False
            break
    return numero


# Función que convierte una cadena con números separados por coma y espacio en una lista.

# from matrices import es_numero
def convertir_a_lista(cadena):
    lista_final = []
    acumulador = ""
    for caracter in cadena:
        if es_numero(caracter):
            acumulador += caracter
        elif caracter == ",":
            lista_final.append(int(acumulador))
            acumulador = ""
        elif caracter != " ":
            raise ValueError("La cadena tiene un formato erróneo.")
    lista_final.append(int(acumulador))
    return lista_final


# Función que devuelve el tamaño de la mayor secuencia de números iguales en una lista.

def elem_consecutivos(lista):
    contador = 1
    longitudes = []
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            contador += 1
        else:
            longitudes.append(contador)
            contador = 1
    longitudes.append(contador)
    ordenada = sorted(longitudes)
    return ordenada[-1]


# Función que construye una matriz con las filas introducidas por teclado.

# from matrices import convertir_a_lista
def introduce_matriz():
    matriz = []
    cadfila = input("Introduce la fila: ")
    while cadfila != "":
        fila = convertir_a_lista(cadfila)
        matriz.append(fila)
        cadfila = input("Introduce la fila: ")
    return matriz


# Función que genera una matriz aleatoria.

# from random import random
def matriz_aleatoria(nfilas, ncol, maxvalor):
    M = []
    for f in range(nfilas):
        fila = []
        for c in range(ncol):
            fila.append(round(random() * maxvalor, 4))
        M.append(fila)
    return M


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


# Función que elimina todos los elementos con el valor especificado de una matriz dada por parámetro.

def elimina_elemento(M, elem):
    for nfila in range(len(M)):
        while elem in M[nfila]:
            M[nfila].remove(elem)
    return M


# Función que devuelve una copia de la matriz dada por parámetro sin los elementos con el valor especificado.

def elimina_elemento_copia(M,elem):
    Msinelem = []
    for nfila in range(len(M)):
        fila = []
        for ncolumna in range(len(M[nfila])):
            if M[nfila][ncolumna] != elem:
                fila.append(M[nfila][ncolumna])
        Msinelem.append(fila)
    return Msinelem


# Función que devuelve la traspuesta de una matriz.

def traspuesta(M):
    Mtraspuesta = []
    for i in range(len(M[0])):
        Mtraspuesta.append([])
    for nfila in range(len(M)):
        for ncolumna in range(len(M[nfila])):
            Mtraspuesta[ncolumna].append(M[nfila][ncolumna])
    return Mtraspuesta


# Función que devuelve la unión de las filas de una matriz sin repetir números.

def union_filas(M):
    union = []
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] not in union:
                union.append(M[i][j])
    return union


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


# Función que calcula el determinante de una matriz.

# from matrices import elimina_fila_copia, elimina_columna_copia
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


# Función que devuelve la adjunta de una matriz.

# from matrices import determinante, traspuesta, elimina_fila_copia, elimina_columna_copia
def adjunta(M):
    Mcof = []
    for i in range(len(M)):
        fila = []
        for j in range(len(M[i])):
            cofactor = (-1) ** (i+j) * determinante(elimina_fila_copia(elimina_columna_copia(M, j), i))
            fila.append(cofactor)
        Mcof.append(fila)
    return traspuesta(Mcof)


# Función que devuelve la inversa de una matriz.

# from matrices import adjunta, determinante
def inversa(M):
    inv = []
    for i in range(len(M)):
        fila = []
        for j in range(len(M[i])):
            fila.append(adjunta(M)[i][j] / determinante(M))
        inv.append(fila)
    return inv


# Función que devuelve la matriz identidad de tamaño n.

def identidad(n):
    I = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        I.append(fila)
    return I


# Función que calcula la resta entre dos matrices.

def resta_matrices(M1, M2):
    M = []
    if len(M1) != len(M2):
        print("No se pueden restar, ya que tienen diferente número de filas.")
    else:
        for i in range(len(M1)):
            fila = []
            if len(M1[i]) != len(M2[i]):
                print("No se pueden restar, ya que tienen diferente número de columnas.")
            else:
                for j in range(len(M1[i])):
                    fila.append(M1[i][j]-M2[i][j])
                M.append(fila)
    return M


# Función que recorre una matriz en forma de espiral.

def espiral(M):
    result = []

    n_filas = len(M)
    n_columnas = len(M[0])

    n_it = n_filas // 2

    for it in range(n_it):
        # ->
        # columna:
        # it 0: 0 -> n_columnas -1
        # it 1: 1 -> n_columnas -2
        # ...
        # it i: i -> n_columnas-i-1
        for col in range(it, n_columnas - it):
            result.append(M[it][col])

        # columna abajo
        # fila:
        # it 0: 1 -> n_filas -1
        # it 1: 2 -> n_filas-2
        # ...
        # it i: i+1 -> n_filas -i -1
        for fila in range(it + 1, n_filas - it):
            result.append(M[fila][n_columnas - it - 1])

        # <-
        for colinversa in range(n_columnas - it - 2, it - 1, -1):
            result.append(M[n_filas - it - 1][colinversa])

        # columna arriba
        for filainversa in range(n_filas - it - 2, it, -1):
            result.append(M[filainversa][it])

    return result


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

# from matrices import elem_consecutivos, traspuesta, vuelta_matriz
def secuencia_mas_larga(M):
    longitud = 1
    diagonal = []

    for n_fila in range(len(M)):
        if elem_consecutivos(M[n_fila]) > longitud:
            longitud = elem_consecutivos(M[n_fila])

    for n_columna in range(len(traspuesta(M))):
        if elem_consecutivos(traspuesta(M)[n_columna]) > longitud:
            longitud = elem_consecutivos(traspuesta(M)[n_columna])

    for n_diagonal in range(len(M) + len(M[0]) - 1):
        for nfila in range(len(M)):
            for ncolumna in range(len(traspuesta(M))):
                if nfila + ncolumna == n_diagonal:
                    diagonal.append(M[nfila][ncolumna])
        if elem_consecutivos(diagonal) > longitud:
            longitud = elem_consecutivos(diagonal)
        diagonal = []

    for n_diagonal_vuelta in range(len(M) + len(M[0]) - 1):
        for nfila_vuelta in range(len(M)):
            for ncolumna_vuelta in range(len(traspuesta(M))):
                if nfila_vuelta + ncolumna_vuelta == n_diagonal_vuelta:
                    diagonal.append(vuelta_matriz(M)[nfila_vuelta][ncolumna_vuelta])
        if elem_consecutivos(diagonal) > longitud:
            longitud = elem_consecutivos(diagonal)
        diagonal = []

    return longitud


# Función que crea una matriz aleatoria con enteros del 0 al 1000.

# from random import randint
def crear_matriz_aleatoria(x, y):
    M = []
    for i in range(x):
        nueva_fila = []
        for j in range(y):
            nueva_fila.append(randint(0, 1000))
        M.append(nueva_fila)
    return M


# Función que calcula la media de los elementos de la cruz central de una matriz 7x5.

def media_cruz_central(M):
    suma = 0
    for i in range(len(M)):
        suma += M[i][2]
    for j in range(len(M[3])):
        suma += M[3][j]
    return suma/(len(M) + len(M[3]))


# Función que resta las diagonales de una matriz.

def resta_diagonales(M):
    diag1 = 0
    diag2 = 0
    for i in range(len(M)):
        diag1 += M[i][i]
        diag2 += M[i][len(M)-1-i]
    return diag1 - diag2


# Función que elimina una fila y una columna de una matriz.

def elimina_fila_columna(M, fila, columna):
    resultado = []
    for i in range(len(M)):
        if i != fila:
            row = []
            for j in range(len(M[i])):
                if j != columna:
                    row.append(M[i][j])
            resultado.append(row)
    return resultado

