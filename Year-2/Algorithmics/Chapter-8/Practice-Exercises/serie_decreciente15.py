# Función que imprime la serie decreciente de números naturales del n al 1 de forma recursiva.

def serie_decreciente(n):
    if n == 1:
        print(1)
    else:
        print(n)
        serie_decreciente(n-1)


serie_decreciente(7)
