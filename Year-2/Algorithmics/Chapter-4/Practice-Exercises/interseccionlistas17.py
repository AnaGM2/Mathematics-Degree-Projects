# Función que devuelve la intersección de dos listas.

def intersect_listas(lista1, lista2):
    lista = []
    for elemento in lista1:
        if elemento in lista2:
            lista.append(elemento)
    return lista


lista1 = [1, 5, 24, 32, 88]
lista2 = [1, 2, 3, 18, 24]
lista = intersect_listas(lista1, lista2)
print(lista)
