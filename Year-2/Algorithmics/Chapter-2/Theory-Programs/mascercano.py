a = int(input('Primer número: '))
b = int(input('Segundo número: '))
c = int(input('Tercer número: '))
d = int(input('Cuarto número: '))
e = int(input('Quinto número: '))

mascercano = b

if abs(c-a) < abs(mascercano-a):
    mascercano = c
if abs(d-a) < abs(mascercano-a):
    mascercano = d
if abs(e-a) < abs(mascercano-a):
    mascercano = e

print(mascercano)
