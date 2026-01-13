from random import random

# Función que devuelve una cadena cifrada con contraseña.

def cifrar_avanzado(cadena, contrasena):
    cifrada = ""
    posicion = 0

    for caracter in cadena:
        avance = ord(contrasena[posicion % len(contrasena)])
        posicion += 1

        codigo = ord(caracter) + avance
        cifrada += chr(codigo)
    return cifrada



# Función que descifra una cadena cifrada con contraseña.

def descifrar_avanzado(cifrada, contrasena):
    cadena = ""
    posicion = 0

    for caracter in cifrada:
        avance = ord(contrasena[posicion % len(contrasena)])
        posicion += 1

        codigo = ord(caracter) - avance
        cadena += chr(codigo)
    return cadena



# Función que indica si los elementos de una cadena son un número entero.

def es_numero(cadena):
    numero = True
    for caracter in cadena:
        if caracter not in "0123456789":
            numero = False
            break
    return numero



# Función que convierte una cadena con números separados por coma y espacio en una lista.

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



# Función que genera una matriz aleatoria.

# from random import random
def matriz_aleatoria(nfilas, ncol):
    M = []
    for f in range(nfilas):
        fila = []
        for c in range(ncol):
            fila.append(round(random(), 4))
        M.append(fila)
    return M



# Función que multiplica dos matrices.

def multiplicacion_matrices(M1, M2):
    M = []
    for nfila1 in range(len(M1)):
        fila = []
        for ncolumna2 in range(len(M2[0])):
            elem = 0
            for ncolumna1 in range(len(M1[0])):  # También se podría tomar range(len(M2)).
                elem += M1[nfila1][ncolumna1] * M2[ncolumna1][ncolumna2]
            fila.append(elem)
        M.append(fila)
    return M



# Función que transforma una cadena con formato de matriz en matriz.

# from archivosyargumentos import es_numero
def convertir_a_matriz(cadena):
    M = []
    fila = []
    acumulador = ""
    for ncaracter in range(len(cadena)):
        if es_numero(cadena[ncaracter]) or cadena[ncaracter] == ".":
            acumulador += cadena[ncaracter]
        elif cadena[ncaracter] == "," and cadena[ncaracter - 1] != "]":
            fila.append(float(acumulador))
            acumulador = ""
        elif cadena[ncaracter] == "]" and ncaracter != len(cadena) - 1:
            fila.append(float(acumulador))
            acumulador = ""
            M.append(fila)
            fila = []
    return M
