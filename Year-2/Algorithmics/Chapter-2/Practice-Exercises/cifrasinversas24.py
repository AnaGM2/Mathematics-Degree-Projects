# Programa que imprime las cifras en orden inverso de un número.

numero = int(input("Introduce un natural: "))

while numero != 0:
    print(numero % 10)
    numero = numero // 10
