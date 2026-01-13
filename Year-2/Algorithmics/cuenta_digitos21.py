# Función recursiva que indica cuántas veces aparece un dígito k en el número n.

def cuenta_digitos(n, k):
    cadena = str(n)
    if len(cadena) == 1:
        if n == k:
            return 1
        else:
            return 0
    else:
        if int(cadena[0]) == k:
            return 1 + cuenta_digitos(int(cadena[1:]), k)
        else:
            return cuenta_digitos(int(cadena[1:]), k)


print(cuenta_digitos(5135565256565335, 5))
