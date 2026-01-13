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


# Programa de prueba.

cadena = "Esto es una prueba"
avance = 2
cifrada = cifrar(cadena, avance)
print("La cadena cifrada es: ", cifrada)
descifrada = descifrar(cifrada, avance)
print("La cadena descifrada es: ", descifrada)
