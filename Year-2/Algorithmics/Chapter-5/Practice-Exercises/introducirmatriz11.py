from matrices import convertir_a_lista


# Función que construye una matriz con las filas introducidas por teclado.

def introduce_matriz():
    matriz = []
    cadfila = input("Introduce la fila: ")
    while cadfila != "":
        fila = convertir_a_lista(cadfila)
        matriz.append(fila)
        cadfila = input("Introduce la fila: ")
    return matriz


print("Has introducido la matriz: " + str(introduce_matriz()))
