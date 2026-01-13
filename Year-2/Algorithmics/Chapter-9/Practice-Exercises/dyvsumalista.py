def pequeno(lista):
    return len(lista) == 1


def trivial(lista):
    return lista[0]


def descomponer(lista):
    mitad = len(lista)//2
    return [lista[:mitad], lista[mitad:]]


def combinar(solParciales):
    return solParciales[0] + solParciales[1]


def Suma_DyV(lista):
    if pequeno(lista):
        return trivial(lista)
    solucionesParciales = []
    for q in descomponer(lista):
        solucionesParciales.append(Suma_DyV(q))
    return combinar(solucionesParciales)


lista = [-1, -2, 4, -9, -3, -2, 0, 9]
print(Suma_DyV(lista))
