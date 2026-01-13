def ya_resuelto(memo, n):
    return n in memo


def pequeno(n):
    return n <= 1


def trivial(n):
    return n


def descomponer(n):
    return [n-1, n-2]


def combinar(solParciales):
    return solParciales[0] + solParciales[1]


def Fib_DyV(memo, X):
    if ya_resuelto(memo, X):
        return memo[X]
    if pequeno(X):
        memo[X] = trivial(X)
        return memo[X]
    solucionesParciales = []
    for q in descomponer(X):
        solucionesParciales.append(Fib_DyV(memo, q))
    memo[X] = combinar(solucionesParciales)
    return memo[X]


memo = {}
n = int(input("Introduce el valor de n: "))
print(Fib_DyV(memo, n))
