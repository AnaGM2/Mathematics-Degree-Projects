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


print(mayuscula('esto es una prueba'))
