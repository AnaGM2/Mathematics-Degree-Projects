# Función que devuelve el número de dígitos impares de un número.

def digitos_impares(n):
    cadena = str(n)
    if len(cadena) == 1:
        if int(cadena) % 2 != 0:
            return 1
        else:
            return 0
    else:
        if int(cadena[0]) % 2 != 0:
            return 1 + digitos_impares(int(cadena[1:]))
        else:
            return digitos_impares(int(cadena[1:]))


print(digitos_impares(1234327))
