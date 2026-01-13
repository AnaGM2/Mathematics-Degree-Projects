a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
c = float(input("Introduce el tercer número: "))

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

print("Mayor:", mayor, ", Menor:", menor)
