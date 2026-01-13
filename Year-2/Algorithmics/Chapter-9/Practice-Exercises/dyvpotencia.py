def pequeno(x, n):
    return n < 1


def trivial(x, n):
    return 1


def descomponer(n):
    return [n//2]


def combinar(x, n, solParciales):
    sol = solParciales[0] * solParciales[0]
    if n % 2 == 1:
        sol *= x
    return sol


def Pot_DyV(x, n):
    if pequeno(x, n):
        return trivial(x, n)
    solucionesParciales = []
    for q in descomponer(n):
        solucionesParciales.append(Pot_DyV(x, q))
    return combinar(x, n, solucionesParciales)


X = int(input("Introduce la base: "))
n = int(input("Introduce la potencia: "))
print(Pot_DyV(X, n))
