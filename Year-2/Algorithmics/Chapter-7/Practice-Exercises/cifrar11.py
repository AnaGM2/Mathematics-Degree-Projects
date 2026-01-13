from sys import argv
from archivosyargumentos import cifrar_avanzado


contrasena = input('Introduzca una contraseña: ')
texto = input('Introduzca un texto a encriptar: ')

texto_cifrado = cifrar_avanzado(texto, contrasena)


with open(argv[1], 'w', encoding="utf-8") as fichero:
    fichero.write(texto_cifrado)

