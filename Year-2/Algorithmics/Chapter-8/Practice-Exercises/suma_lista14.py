# Función que suma los elementos de una lista de forma recursiva.

def suma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + suma_lista(lista[1:])


print(suma_lista([4, 6, 8, 9, 24, 32, 34]))
