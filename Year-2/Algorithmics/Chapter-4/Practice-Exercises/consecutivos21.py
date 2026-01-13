# Función que devuelve el tamaño de la mayor secuencia de números iguales en una lista.

def elem_consecutivos(lista):
    contador = 1
    longitudes = []
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            contador += 1
        else:
            longitudes.append(contador)
            contador = 1
    longitudes.append(contador)
    ordenada = sorted(longitudes)
    return ordenada[-1]


print(elem_consecutivos([0, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 0, 0, 0]))
