# Función que elimina los acentos de una cadena.

def sin_acentos(cadena):
    acentos = 'ÁÉÍÓÚáéíóú'
    letras = 'AEIOUaeiou'
    for caracter in cadena:
        if caracter in acentos:
            cadena = cadena.replace(caracter, letras[acentos.find(caracter)])
    return cadena


print(sin_acentos("hólÁoÁ"))
