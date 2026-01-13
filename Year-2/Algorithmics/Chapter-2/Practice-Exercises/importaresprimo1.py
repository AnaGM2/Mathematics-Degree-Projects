from variablesyfunciones import esprimo

inicio = int(input("Introduce el inicio del rango: "))
fin = int(input("Introduce el fin del rango: "))
for i in range(inicio, fin+1):
    if esprimo(i):
        print(i)
