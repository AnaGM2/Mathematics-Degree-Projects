# Función que calcula el factorial de un número de forma recursiva.

def factorial_recursivo(N):
    if type(N) is float:
        raise ValueError("No se puede calcular el factorial de un número con decimales.")
    elif type(N) is int and N < 0:
        raise ValueError("No se puede calcular el factorial de un entero negativo.")
    elif type(N) is int and N >= 0:
        if N == 0 or N == 1:
            return N
        else:
            return N * factorial_recursivo(N-1)


print(factorial_recursivo(12))
