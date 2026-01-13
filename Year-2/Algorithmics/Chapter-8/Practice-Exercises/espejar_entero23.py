# Función recursiva que devuelve un número natural con los dígitos en sentido contrario.

def espejar_entero(n):
    cadena = str(n)
    if len(cadena) == 1:
        return n
    else:
        return int(cadena[-1]) * 10 ** (len(cadena)-1) + espejar_entero(n // 10)


print(espejar_entero(2089))
