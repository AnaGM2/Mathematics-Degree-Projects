from sys import argv
from archivosyargumentos import multiplicacion_matrices, convertir_a_matriz

with open(argv[1], 'r') as fichero:
    M1 = convertir_a_matriz(fichero.readline())

with open(argv[2], 'r') as fichero:
    M2 = convertir_a_matriz(fichero.readline())

with open(argv[3], 'w') as fichero:
    fichero.write(str(multiplicacion_matrices(M1, M2)))
