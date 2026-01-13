# Función que suma los N primeros números naturales de forma recursiva.

def serie_creciente(N):
    if N == 1:
        return N
    else:
        return N + serie_creciente(N-1)


print(serie_creciente(5))
