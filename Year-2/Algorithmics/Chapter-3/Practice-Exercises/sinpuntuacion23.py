# Función que elimina los signos de puntuación de una cadena.

def sin_puntuacion(cadena):
    for caracter in cadena:
        if not caracter.isalnum() and caracter != ' ':
            cadena = cadena.replace(caracter, "")
    return cadena


print(sin_puntuacion("¡ho-la:, adi'os"))
