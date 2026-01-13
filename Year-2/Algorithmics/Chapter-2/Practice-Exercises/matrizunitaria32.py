# Programa que imprime una matriz unitaria del tamaño indicado.

dimension = int(input('Introduce la dimensión: '))
contador = 1

for i in range(1, dimension+1):
    for j in range(1, dimension+1):
        if contador != dimension:
            contador += 1
            if i == j:
                print("1", end="")
            else:
                print("0", end="")
        else:
            contador = 1
            if i == j:
                print("1")
            else:
                print("0")
