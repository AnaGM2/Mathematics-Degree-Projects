# Programa que compara y calcula la media de números indeterminados.

num = input("Dame un número: ")

suma = 0
contador = 0
mayor = float(num)
menor = float(num)

while num != 'fin':
    # Media
    suma += float(num)
    contador += 1
    # Mayor
    if float(num) > mayor:
        mayor = float(num)
    # Menor
    if float(num) < menor:
        menor = float(num)

    num = input("Dame un número: ")

print("Mayor: ", mayor, "\nMenor: ", menor, "\nMedia: ", suma / contador)
