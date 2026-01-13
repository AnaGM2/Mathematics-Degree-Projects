from os import scandir
from sys import argv

with scandir(argv[1]) as dir:
    for file in dir:
        print('Nombre: {0}'.format(file.name))
        print('Ruta: {0}'.format(file.path))
        print('¿Es un directorio? {0}'.format(file.is_dir()))
        print('¿Es un archivo? {0}'.format(file.is_file()))


def encontrar_base_de_datos(ruta):
    rutas_bases_de_datos = []
    with scandir(ruta) as dir:
        for file in dir:
            if file.is_file() and file.name.endswith(".tsv"):
                rutas_bases_de_datos.append(file.path)
            elif file.is_dir():
                rutas_bases_de_datos += encontrar_base_de_datos(file.path)
    return rutas_bases_de_datos


print(encontrar_base_de_datos(argv[1]))


# Función que imprime los resultados por páginas de 20 elementos.

def imprimir_resultados(resultado, lista_de_páginas, num_pagina):
    if len(resultado) == 1:
        print(len(resultado), "elemento encontrado. Página ", num_pagina, " de ", len(lista_de_páginas), ":")
    else:
        print(len(resultado), "elementos encontrados. Página ", num_pagina, " de ", len(lista_de_páginas), ":")

    num_empieza = 20 * (num_pagina - 1) + 1
    pagina = lista_de_páginas[num_pagina - 1]

    for i in range(len(pagina)):
        NUM = str(num_empieza + i)
        titulo = pagina[i][1]
        anyo = pagina[i][2]
        director = pagina[i][3]
        tipo_obra = pagina[i][4]
        ruta_fichero = pagina[i][5]
        print(NUM + ". \t" + titulo + " (" + anyo + "). \t" + director + ". \t" + tipo_obra + " [" + ruta_fichero + "]")
