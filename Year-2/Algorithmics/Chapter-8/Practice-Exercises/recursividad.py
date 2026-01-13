# Función que devuelve una copia de la matriz dada por parámetro sin la fila i-ésima.

def elimina_fila_copia(M, i):
    Msinfila = []
    for nfila in range(len(M)):
        if nfila != i:
            Msinfila.append(M[nfila])
    return Msinfila


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


# Función que calcula el determinante de una matriz de forma recursiva.

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


# Función que suma los N primeros números naturales de forma recursiva.

def serie_creciente(N):
    if N == 1:
        return N
    else:
        return N + serie_creciente(N-1)


# Función que calcula el factorial de un número de forma recursiva.

def factorial_recursivo(N):
    if type(N) is float:
        raise ValueError("No se puede calcular el factorial de un número con decimales.")
    elif type(N) is int and N < 0:
        raise ValueError("No se puede calcular el factorial de un entero negativo.")
    elif type(N) is int and N >= 0:
        if N == 0 or N == 1:
            return N
        else:
            return N * factorial_recursivo(N-1)


# Función que imprime la serie decreciente de números naturales del n al 1 de forma recursiva.

def serie_decreciente(n):
    if n == 1:
        print(1)
    else:
        print(n)
        serie_decreciente(n-1)


# Función recursiva que indica cuántas veces aparece un dígito k en el número n.

def cuenta_digitos(n, k):
    cadena = str(n)
    if len(cadena) == 1:
        if n == k:
            return 1
        else:
            return 0
    else:
        if int(cadena[0]) == k:
            return 1 + cuenta_digitos(int(cadena[1:]), k)
        else:
            return cuenta_digitos(int(cadena[1:]), k)


# Función que devuelve el número de dígitos impares de un número.

def digitos_impares(n):
    cadena = str(n)
    if len(cadena) == 1:
        if int(cadena) % 2 != 0:
            return 1
        else:
            return 0
    else:
        if int(cadena[0]) % 2 != 0:
            return 1 + digitos_impares(int(cadena[1:]))
        else:
            return digitos_impares(int(cadena[1:]))


# Función recursiva que devuelve un número natural con los dígitos en sentido contrario.

def espejar_entero(n):
    cadena = str(n)
    if len(cadena) == 1:
        return n
    else:
        return int(cadena[-1]) * 10 ** (len(cadena)-1) + espejar_entero(n // 10)


# Función que calcula una potencia de forma recursiva.

def potencia(x, y):
    if y == 1:
        return x
    else:
        return x * potencia(x, y-1)


# Función recursiva que devuelve una cadena en sentido contrario.

def espejar_cadena(cadena):
    if cadena == "":
        return ""
    else:
        return cadena[-1] + espejar_cadena(cadena[:-1])


# Función que imprime un número en base 2.

def cambio_base_2_con_print(n):
    if n//2 == 0:
        print(n % 2, end="")
    else:
        cambio_base_2_con_print(n//2)
        print(n % 2, end="")


# Función que devuelve un número en base 2.

def cambio_base_2(n):
    if n//2 == 0:
        return str(n % 2)
    else:
        return cambio_base_2(n//2) + str(n % 2)


# Función que devuelve una lista con los dígitos impares de la lista introducida.

def solo_digitos_impares(lista):
    if len(lista) == 0:
        return lista
    if lista[0] % 2 == 1:
        return [lista[0]] + solo_digitos_impares(lista[1:])
    else:
        return solo_digitos_impares(lista[1:])


# Función que devuelve una lista con las palabras de otra lista en minúsculas.

def pasa_minusculas(lista):
    if len(lista) == 0:
        return lista
    else:
        return [lista[0].lower()] + pasa_minusculas(lista[1:])


# Función que imprime una cadena eliminando cada vez un caracter.

def elimina_caracter_recursivo(cadena):
    if cadena == "":
        return
    print(cadena)
    elimina_caracter_recursivo(cadena[:-1])


# Función que imprime una cadena añadiendo cada vez un caracter.

def anyade_caracter_recursivo(cadena):
    if cadena == "":
        return
    anyade_caracter_recursivo(cadena[:-1])
    print(cadena)

