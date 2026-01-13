from cadenas import sin_puntuacion


# Función que devuelve una lista con las palabras de una cadena.

def extrae_palabras(cadena):
    cadena = sin_puntuacion(cadena)
    lista = cadena.split(" ")
    return lista


print(extrae_palabras("Esta es una frase de entrada. ¡Cuidado!: puede haber muchos signos de puntuación."))
