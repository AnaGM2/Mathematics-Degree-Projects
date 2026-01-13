# Función que devuelve una copia de la cadena habiendo reemplazado las letras que aparecen
# en el diccionario como clave por su valor correspondiente.

def reemplazar(cadena, diccionario):
    resultado = ""
    for caracter in cadena:
        if caracter in diccionario:
            resultado += diccionario[caracter]
        else:
            resultado += caracter
    return resultado


# Función que devuelve un diccionario con la frecuencia de aparición de cada palabra en un texto.
# from diccionariostuplasyclases import reemplazar

def cuenta_palabras(texto):
    texto = texto.lower()
    reemplazos = {"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u", ".":"", ",":"", ":":"", "-":"", ";":""}
    lista = texto.split()
    lista_arreglada = []
    diccionario = {}

    for elemento in lista:
        lista_arreglada.append(reemplazar(elemento, reemplazos))

    for palabra in lista_arreglada:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario


# Función que devuelve un diccionario con la frecuencia de aparición de cada pareja de palabras
# consecutivas en un texto.
# from diccionariostuplasyclases import reemplazar

def cuenta_bigramas(texto):
    texto = texto.lower()
    reemplazos = {"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u", ".":"", ",":"", ":":"", "-":"", ";":""}
    lista = texto.split()
    lista_arreglada = []
    diccionario = {}
    lista_tuplas = []

    for elemento in lista:
        lista_arreglada.append(reemplazar(elemento, reemplazos))

    for i in range(len(lista_arreglada)-1):
        tupla = (lista_arreglada[i], lista_arreglada[i+1])
        lista_tuplas.append(tupla)

    for palabras in lista_tuplas:
        if palabras in diccionario:
            diccionario[palabras] += 1
        else:
            diccionario[palabras] = 1

    return diccionario


# Función que imprime el menú de opciones del programa de gestión de usuarios.

def imprimir_menu():
    print('1) Añadir usuario')
    print('2) Eliminar usuario')
    print('3) Listar usuario')
    print('4) Acceder')
    print('5) Máxima edad')
    print('6) Salir')
