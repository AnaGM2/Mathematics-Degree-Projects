from listas import esprimo, crear_lista_aleatoria

# Función que devuelve una lista con los números primos de la lista introducida menores que n.


def cuales_primos(lista, n):
    lista_final = []
    for elemento in lista:
        numero = int(elemento)
        if esprimo(numero) and numero < n:
            lista_final.append(numero)
    return lista_final


print(cuales_primos(crear_lista_aleatoria(7, 2, 30), 12))
