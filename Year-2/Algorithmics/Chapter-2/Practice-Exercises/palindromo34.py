# Función que comprueba si una cadena es un palíndromo.

def palindromo(cadena):

    es_palin = True

    for i in range(0, len(cadena)//2):
        if cadena[i] != cadena[-i-1]:
            es_palin = False

    return es_palin
