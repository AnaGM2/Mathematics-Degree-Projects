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


# Programa de prueba.

if y_incorrecta("La palabra inteligente es correcta y la palabra Ynteligente es incorrecta."):
    print('Incorrecta')
else:
    print('Correcta')
