from utils import imprimir_menu, encontrar_base_de_datos, indexar_fichero, buscador, paginacion_resultados
from utils import imprimir_resultados, buscador_descripcion_union, buscador_descripcion_interseccion, union_interseccion
from utils import guardar_indices_ficheros, leer_indices_ficheros
from sys import argv


# Índices y lista de entradas
indice_titulos = {}
indice_directores = {}
indice_descripciones = {}
entradas = []


# Indexado
lista_indices = [indice_titulos, indice_directores, indice_descripciones, entradas]
lista_ficheros = ['file_titulos.txt', 'file_directores.txt', 'file_descripciones.txt', 'file_entradas.txt']

try:
    fichero_prueba = open(argv[1] + '\\file_titulos.txt', 'r')
    print('Cargando los índices desde disco.')
    fichero_prueba.close()

    for i in range(len(lista_indices)):
        leer_indices_ficheros(lista_indices[i], lista_ficheros[i], argv[1])

except FileNotFoundError:
    for ruta in encontrar_base_de_datos(argv[1]):
        indexar_fichero(ruta, indice_titulos, indice_directores, indice_descripciones, entradas)

    for i in range(len(lista_indices)):
        guardar_indices_ficheros(lista_indices[i], lista_ficheros[i], argv[1])


# Menú
salir = False
while not salir:
    imprimir_menu()
    op = input('Introduce una opción: ')

    if op == '1':
        resultado = buscador(input("Introduce el titulo: "), indice_titulos, entradas)
        imprimir_resultados(resultado, paginacion_resultados(resultado), 1)

    if op == '2':
        directores_no_ordenados = []
        for director in indice_directores:
            directores_no_ordenados.append(entradas[indice_directores[director][0]][3])
        directores_ordenados = sorted(directores_no_ordenados)
        for director in directores_ordenados:
            print(director)

    if op == '3':
        resultado = buscador(input("Introduce el director: "), indice_directores, entradas)
        imprimir_resultados(resultado, paginacion_resultados(resultado), 1)

    if op == '4':
        busqueda, interseccion = union_interseccion(input("Introduce palabras contenidas en la descripción: "))
        if interseccion:
            resultado = buscador_descripcion_interseccion(busqueda, indice_descripciones, entradas)
        else:
            resultado = buscador_descripcion_union(busqueda, indice_descripciones, entradas)
        imprimir_resultados(resultado, paginacion_resultados(resultado), 1)

    if op == '5':
        salir = True
