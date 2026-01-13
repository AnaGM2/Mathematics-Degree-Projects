# Función que calcula el factorial de un número.

def factorial(num):
    fact = 1
    if num != 0:
        for cifra in range(1, num+1):
            fact *= cifra
    return fact


# Función que calcula el coeficiente binomial de dos números.

def binomial(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))
