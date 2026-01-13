from utils import union_interseccion, convertir_a_tupla

busqueda, interseccion = union_interseccion(input('xhxhs: '))

print(busqueda)

print('   djhejw '.strip())

if interseccion:
    print('interseccion')

try:
    with open('mdjfeioe.txt', 'r') as f:
        f.write()
except FileNotFoundError:
    print('fiurh')


print(convertir_a_tupla("'s1', 'The Grand Seduction'"))





# Función que guarda los índices en ficheros en el directorio.

def guardar_indices_ficheros_2(indice, fichero, ruta_directorio):
    ruta = ruta_directorio + '\\' + fichero
    with open(ruta, 'w', encoding="utf-8") as f:
        for elemento in indice:
            if type(indice) == list:
                f.write(str(elemento)[1:-1] + '\n')
            else:
                f.write(elemento + ':' + str(indice[elemento]) + '\n')




# Función que convierte una cadena con subcadenas separadas por coma en tupla.

def convertir_a_tupla(cadena):
    lista = []
    acumulador = ""
    for i in range(len(cadena)):
        if cadena[i] == "," and cadena[i-1] == "'":
            lista.append(acumulador)
            acumulador = ""
        elif cadena[i] == "'" and cadena[i-1] == " ":
            continue
        else:
            acumulador += cadena[i]
    lista.append(acumulador)
    return tuple(lista)
