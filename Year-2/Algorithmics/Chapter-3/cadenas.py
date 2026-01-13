# Función que reemplaza dos caracteres en una cadena.

def reemplazar(cad, a, b):
    resultado = ""

    if len(a)>1 or len(b)>1:
        raise ValueError

    else:
        for caracter in cad:
            if caracter == a:
                resultado = resultado + b
            else:
                resultado = resultado + caracter

    return resultado



# Función que devuelve una cadena cifrada.

def cifrar(cadena, avance):
    cifrada = ""
    for caracter in cadena:
        codigo = ord(caracter) + avance
        cifrada += chr(codigo)
    return cifrada



# Función que descifra una cadena cifrada.

def descifrar(cifrada, avance):
    cadena = ""
    for caracter in cifrada:
        codigo = ord(caracter) - avance
        cadena += chr(codigo)
    return cadena



# Función que devuelve una cadena en mayúsculas.

def mayuscula(cadena):
    resultado = ""
    for caracter in cadena:
        if caracter == ' ':
            codigo = ord(caracter)
        else:
            codigo = ord(caracter) - 32
        resultado += chr(codigo)
    return resultado



# Función que devuelve una cadena cifrada con contraseña.

def cifrar_avanzado(cadena, contraseña):
    cifrada = ""
    posicion = 0

    for caracter in cadena:
        avance = ord(contraseña[posicion % len(contraseña)])
        posicion += 1

        codigo = ord(caracter) + avance
        cifrada += chr(codigo)
    return cifrada



# Función que descifra una cadena cifrada con contraseña.

def descifrar_avanzado(cifrada, contraseña):
    cadena = ""
    posicion = 0

    for caracter in cifrada:
        avance = ord(contraseña[posicion % len(contraseña)])
        posicion += 1

        codigo = ord(caracter) - avance
        cadena += chr(codigo)
    return cadena



# Función que reemplaza todas las apariciones de una subcadena por otra dada.

def reemplazar_subcadena(cadenalarga, busqueda, reemplazo):
    resultado = ""
    skip = 0
    for i in range(len(cadenalarga)):
        if skip > 0:
            skip -= 1
            continue
        if len(cadenalarga[i:]) < len(busqueda):
            resultado += cadenalarga[i:]
            break
        if cadenalarga[i:i + len(busqueda)] == busqueda:
            resultado += reemplazo
            skip = len(busqueda) - 1
        else:
            resultado += cadenalarga[i]
    return resultado



# Función que indica si dos cadenas tienen los mismos caracteres
# (sin tener en cuenta el orden ni las veces que se repiten).

def mismos_caracteres(cadena1, cadena2):
    valor = True
    for caracter in cadena1:
        if caracter != ' ':
            if caracter not in cadena2:
                valor = False
    for caracter in cadena2:
        if caracter != ' ':
            if caracter not in cadena1:
                valor = False
    return valor



# Función que indica si una cadena tiene alguna y incorrecta.

def y_incorrecta(cadena):
    cadena = cadena.lower()
    incorrecta = False
    consonantes = "bcdfghjklmnñpqrstvwxyz"

    if cadena.startswith("y") and cadena[1] in consonantes:
        incorrecta = True

    for posicion in range(len(cadena)):
        if cadena[posicion] == " " and cadena.find("y", posicion) == posicion+1 and cadena[posicion+2] in consonantes:
            incorrecta = True
            break
    return incorrecta



# Función que elimina los acentos de una cadena.

def sin_acentos(cadena):
    acentos = 'ÁÉÍÓÚáéíóú'
    letras = 'AEIOUaeiou'
    for caracter in cadena:
        if caracter in acentos:
            cadena = cadena.replace(caracter, letras[acentos.find(caracter)])
    return cadena



# Función que elimina los signos de puntuación de una cadena.

def sin_puntuacion(cadena):
    for caracter in cadena:
        if not caracter.isalnum() and caracter != ' ':
            cadena = cadena.replace(caracter, "")
    return cadena



# Función que devuelve una lista con las palabras de una cadena.

# from cadenas import sin_puntuacion
def extrae_palabras(cadena):
    cadena = sin_puntuacion(cadena)
    lista = cadena.split(" ")
    return lista



# Función que devuelve el entero correspondiente a una cadena escrita en binario.

def binario_a_entero(cad):
    resultado = 0
    for i in range(len(cad)):
        if cad[-(i+1)] == '1':
            num = 2 ** i
            resultado += num
    return resultado



# Función que devuelve el prefijo común más largo entre dos cadenas.

def prefijo_comun(cadena1, cadena2):
    prefijo = ""
    longitud_candidato = 1
    while longitud_candidato <= min(len(cadena1), len(cadena2)):
        if cadena1[:longitud_candidato] == cadena2[:longitud_candidato]:
            prefijo = cadena1[:longitud_candidato]
        else:
            break
        longitud_candidato += 1
    return prefijo



# Función que devuelve la letra del DNI.

def letra_dni(dni):
    dni = int(dni)
    indice_letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return indice_letras[dni % 23]



# Función que devuelve el número de dígitos que contiene una cadena.

def numero_digitos_en_cadena(cadena):
    numeros = "0123456789"
    contador = 0
    for caracter in cadena:
        if caracter in numeros:
            contador += 1
    return contador
