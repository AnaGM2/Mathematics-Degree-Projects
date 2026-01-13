from sys import argv
from archivosyargumentos import convertir_a_lista


cadena = input('Introduzca una lista: ')
lista = convertir_a_lista(cadena)


with open(argv[1], 'w') as fichero:
    for numero in lista:
        fichero.write(str(numero) + '\n')
