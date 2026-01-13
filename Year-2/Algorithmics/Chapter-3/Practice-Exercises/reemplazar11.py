# Función que reemplaza dos caracteres en una cadena.

def reemplazar(cad, a, b):
    resultado = ""

    if len(a) > 1 or len(b) > 1:
        raise ValueError

    else:
        for caracter in cad:
            if caracter == a:
                resultado = resultado + b
            else:
                resultado = resultado + caracter

    return resultado



try:
    reemplazar("Hola", "o", "a")
except ValueError:
    print('Error')
