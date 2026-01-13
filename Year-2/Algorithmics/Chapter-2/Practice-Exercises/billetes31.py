# Programa que imprime el desglose en la menor cantidad de billetes y monedas de una cantidad entera de euros.

cantidad = int(input("Introduce la cantidad: "))

if cantidad >= 500:
    billetes = cantidad // 500
    print(billetes, 'de 500')
    cantidad = cantidad % 500

if cantidad >= 200:
    billetes = cantidad // 200
    print(billetes, 'de 200')
    cantidad = cantidad % 200

if cantidad >= 100:
    billetes = cantidad // 100
    print(billetes, 'de 100')
    cantidad = cantidad % 100

if cantidad >= 50:
    billetes = cantidad // 50
    print(billetes, 'de 50')
    cantidad = cantidad % 50

if cantidad >= 20:
    billetes = cantidad // 20
    print(billetes, 'de 20')
    cantidad = cantidad % 20

if cantidad >= 10:
    billetes = cantidad // 10
    print(billetes, 'de 10')
    cantidad = cantidad % 10

if cantidad >= 5:
    billetes = cantidad // 5
    print(billetes, 'de 5')
    cantidad = cantidad % 5

if cantidad >= 2:
    billetes = cantidad // 2
    print(billetes, 'de 2')
    cantidad = cantidad % 2

if cantidad >= 1:
    print(cantidad, 'de 1')
    cantidad = cantidad % 1
