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


# Programa de prueba.

if mismos_caracteres("barco u barca", "corbau"):
    print('verdad')
else:
    print('falso')
