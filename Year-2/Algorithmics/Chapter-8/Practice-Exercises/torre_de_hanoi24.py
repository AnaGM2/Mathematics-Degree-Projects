# Función que recrea las Torres de Hanoi.

def torre_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        destino.append(origen.pop())
        print_resultado()
        return
    torre_de_hanoi(n-1, origen, auxiliar, destino)
    destino.append(origen.pop())
    print_resultado()
    torre_de_hanoi(n-1, auxiliar, destino, origen)


A = [3, 2, 1]
B = []
C = []


def print_resultado():
    print(A)
    print(B)
    print(C)
    print("#####################")


torre_de_hanoi(3, A, C, B)

