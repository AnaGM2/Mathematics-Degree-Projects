# Función que devuelve la unión de dos listas sin repetir números.

def union_listas(lista1, lista2):
    lista = []
    for elemento in lista1:
        if elemento not in lista:
            lista.append(elemento)
    for elemento in lista2:
        if elemento not in lista:
            lista.append(elemento)
    return lista


lista1 = [1, 5, 24, 32, 88]
lista2 = [1, 2, 3, 18, 24]
lista = union_listas(lista1, lista2)
print(lista)
