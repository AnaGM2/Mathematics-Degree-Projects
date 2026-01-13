from sys import argv


def leer_usuarios(ruta_fichero):
    lista = []
    with open(ruta_fichero, 'r') as fichero:
        fichero.readline()
        for linea_con_espacios in fichero:
            linea = linea_con_espacios.strip()
            contador = 0
            nombre = ""
            for ncaracter in range(len(linea)):
                contador += 1
                if linea[ncaracter] != ";":
                    nombre += linea[ncaracter]
                else:
                    break
            apellidos = ""
            for ncaracter in range(contador, len(linea)):
                contador += 1
                if linea[ncaracter] != ";":
                    apellidos += linea[ncaracter]
                else:
                    break
            edad = ""
            for ncaracter in range(contador, len(linea)):
                edad += linea[ncaracter]
            lista.append((nombre, apellidos, int(edad)))
    return lista


print(leer_usuarios(argv[1]))
