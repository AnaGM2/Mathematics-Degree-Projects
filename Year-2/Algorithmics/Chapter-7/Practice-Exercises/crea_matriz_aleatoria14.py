from sys import argv
from archivosyargumentos import matriz_aleatoria


with open(argv[1], 'w') as fichero:
    fichero.write(str(matriz_aleatoria(int(argv[2]), int(argv[3]))))
