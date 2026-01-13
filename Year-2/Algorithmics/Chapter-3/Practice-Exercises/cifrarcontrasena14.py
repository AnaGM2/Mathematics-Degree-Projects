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


# Programa de prueba.

cadena = "esto es una prueba de cifrado"
password = "SECRETO"
cifrada = cifrar_avanzado(cadena, password)
print("La cadena cifrada es: ", cifrada)
descifrada = descifrar_avanzado(cifrada, password)
print("La cadena descifrada es: ", descifrada)
