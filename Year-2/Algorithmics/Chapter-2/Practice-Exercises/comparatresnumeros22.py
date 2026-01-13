# Programa que compara 3 números.

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))

mayor = a
menor = a

if b > mayor:
    mayor = b
if c > mayor:
    mayor = c

if b < menor:
    menor = b
if c < menor:
    menor = c

print("Mayor: ", mayor, "\nMenor: ", menor)
