from random import randint
from math import sqrt

# Función que devuelve una lista con números introducidos individualmente hasta escribir fin.

def introducir_lista():
    lista = []
    entrada = input('Introduzca un número: ')
    while entrada != 'fin':
        try:
            numero = int(entrada)
            lista.append(numero)
            entrada = input('Introduzca un número: ')
        except ValueError:
            raise ValueError('Esto no es un múmero entero.')
    return lista



# Función que indica si los elementos de una cadena son un número entero.

def es_numero(cadena):
    numero = True
    for caracter in cadena:
        if caracter not in "0123456789":
            numero = False
            break
    return numero



# Función que convierte una cadena con números separados por coma y espacio a una lista.

# from listas import es_numero
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



# Función que devuelve una lista aleatoria de enteros del tamaño indicado.

# from random import randint
def crear_lista_aleatoria(size, ini, fin):
    lista = []
    for elemento in range(size):
        numero = randint(ini, fin)
        lista.append(numero)
    return lista



# Función que indica si un número es primo.

def esprimo(num):
    es_primo = True
    for div in range(2, num):
        if num % div == 0:
            es_primo = False
            break
    return es_primo



# Función que devuelve una lista con los números primos de la lista introducida menores que n.

# from listas import esprimo
def cuales_primos(lista, n):
    lista_final = []
    for elemento in lista:
        numero = int(elemento)
        if esprimo(numero) and numero < n:
            lista_final.append(numero)
    return lista_final



# Función que calcula el módulo de un vector de dimensión n.

# from math import sqrt
def modulo_lista(vector):
    prod = 0
    for i in range(len(vector)):
        prod += vector[i]**2
    return sqrt(prod)



# Función que devuelve la unión de dos listas sin repetir números.

def union_listas(lista1, lista2):
    lista = []
    for elemento in lista1:
        if elemento not in lista:
            lista.append(elemento)
    for elemento in lista2:
        if elemento not in lista:
            lista.append(elemento)
    return lista



# Función que devuelve la intersección de dos listas.

def intersect_listas(lista1, lista2):
    lista = []
    for elemento in lista1:
        if elemento in lista2:
            lista.append(elemento)
    return lista



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



# Función que indica si una sublista pertenece a una lista y está en el mismo orden.

def es_sublista_ordenada(sublista, lista):
    indiceinicio = -1
    for pos in range(len(lista)):
        if lista[pos] == sublista[0]:
            indiceinicio = pos
    if indiceinicio == -1:
        return False
    if len(sublista) > len(lista[indiceinicio:]):
        return False
    for pos in range(len(sublista)):
        if sublista[pos] != lista[indiceinicio + pos]:
            return False
    return True
