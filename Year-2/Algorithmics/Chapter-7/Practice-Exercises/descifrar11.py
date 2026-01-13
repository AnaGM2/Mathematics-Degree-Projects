from sys import argv
from archivosyargumentos import descifrar_avanzado


contrasena = input('Introduzca una contraseña para descifrar: ')


with open(argv[1], 'r', encoding="utf-8") as fichero:
    texto_cifrado = fichero.readline()


texto_descifrado = descifrar_avanzado(texto_cifrado, contrasena)

print('El texto descifrado es: ', texto_descifrado)
