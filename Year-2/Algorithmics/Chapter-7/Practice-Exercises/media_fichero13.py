from sys import argv

suma = 0
contador = 0

with open(argv[1], 'r') as fichero:
    for linea in fichero:
        suma += float(linea)
        contador += 1

print('La media de los números del fichero es', suma/contador)
