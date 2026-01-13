from os import scandir


# Función que imprime el menú con las acciones disponibles.

def imprimir_menu():
    print('\n')
    print('1) Buscar por título')
    print('2) Listar directores')
    print('3) Buscar por director')
    print('4) Buscar por descripción')
    print('5) Salir')


# Función que hace que la búsqueda funcione independientemente de acentos y mayúsculas.

def preprocesar(busqueda):
    busqueda = busqueda.lower()

    acentos = "áéíóú"
    letras = "aeiou"

    for caracter in busqueda:
        if caracter in acentos:
            busqueda = busqueda.replace(caracter, letras[acentos.find(caracter)])
    return busqueda


# Función que elimina los signos de puntuación de una cadena.

def sin_puntuacion(cadena):
    for caracter in cadena:
        if not caracter.isalnum() and caracter != ' ':
            cadena = cadena.replace(caracter, "")
    return cadena


# Función que devuelve una lista con las palabras de una cadena.

def extrae_palabras(cadena):
    cadena = sin_puntuacion(cadena)
    lista = cadena.strip().split(" ")
    return lista


# Función que actualiza los índices de títulos y directores.

def anyadir_basico(clave, indice, posicion):
    preproc = preprocesar(clave)
    if preproc not in indice:
        indice[preproc] = []
    indice[preproc].append(posicion)


# Función que actualiza el índice de descripciones.

def anyadir_descripcion(desc, indice, posicion):
    # Diccionario que guarda las palabras de la descripcion
    # ya agregadas al indice
    anyadidas = {}

    # Iteramos sobre las palabras de las descripcion
    for palabra in extrae_palabras(desc):
        preproc = preprocesar(palabra)

        # Si no se ha agregado al indice la palabra:
        if preproc not in anyadidas:

            # Se marca como agregada al indice
            anyadidas[preproc] = True

            # Si el indice no contiene la palabra porque
            # no se ha indexado ninguna descripcion que la contenga:
            # Agregamos una entrada al indice cuya clave es una lista vacia
            if preproc not in indice:
                indice[preproc] = []

            # Agregramos la posicion al final de la entrada
            indice[preproc].append(posicion)


# Función de indexado.

def indexar_fichero(ruta_fichero, ind_titulos, ind_directores, ind_descripciones, entradasbd):
    with open(ruta_fichero, "r", encoding='utf-8') as f:
        for linea in f:
            linea = linea.rstrip("\n")

            # Extraer datos de la linea
            id, titulo, anyo, director, tipo, descripcion = linea.split("\t")

            # Agregar datos a lista de tuplas
            posicion = len(entradasbd)
            entradasbd.append((id, titulo, anyo, director, tipo, ruta_fichero))

            # Actualizar indices
            anyadir_basico(titulo, ind_titulos, posicion)
            anyadir_basico(director, ind_directores, posicion)
            anyadir_descripcion(descripcion, ind_descripciones, posicion)


# Función que devuelve una lista con las rutas de las bases de datos en la carpeta pasada por argumento.

def encontrar_base_de_datos(ruta):
    rutas_bases_de_datos = []
    with scandir(ruta) as dir:
        for file in dir:
            if file.is_file() and file.name.endswith(".tsv"):
                rutas_bases_de_datos.append(file.path)
            elif file.is_dir():
                rutas_bases_de_datos += encontrar_base_de_datos(file.path)
    return rutas_bases_de_datos


# Función para buscar por título o director.

def buscador(busqueda, indice, entradasbd):
    preproc = preprocesar(busqueda)
    result = []
    if preproc in indice:
        for posicion in indice[preproc]:
            result.append(entradasbd[posicion])
    return result


# Función que separa por páginas de 20 elementos los resultados de una búsqueda.

def paginacion_resultados(resultado):
    if len(resultado) < 20:
        return [resultado]
    else:
        return [resultado[:20]] + paginacion_resultados(resultado[20:])


# Función que imprime los resultados por páginas de 20 elementos.

def imprimir_resultados(resultado, lista_de_páginas, num_pagina):
    print('\n')
    if len(resultado) == 0:
        print("0 elementos encontrados.")
        return

    elif len(resultado) == 1:
        print(len(resultado), "elemento encontrado.")

    else:
        if len(lista_de_páginas) == 1:
            print(len(resultado), "elementos encontrados.")
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
    print('\n')

    mostrar_descripcion(resultado, lista_de_páginas, num_pagina)


# Función que muestra la descripción del resultado indicado.

def mostrar_descripcion(resultado, lista_de_páginas, num_pagina):
    pagina = lista_de_páginas[num_pagina - 1]

    if len(lista_de_páginas) == 1:
        print("Introduce el número de resultado para el que quieres visualizar la descripción")
        num_resultado = input("o 0 para volver al menú principal: ")
    else:
        print("Introduce el número de resultado para el que quieres visualizar la descripción,")
        num_resultado = input("0 para volver al menú principal, S para pasar a la página siguiente o A para pasar a la página anterior: ")

    if num_resultado == 'S':
        if num_pagina != len(lista_de_páginas):
            imprimir_resultados(resultado, lista_de_páginas, num_pagina + 1)
        else:
            imprimir_resultados(resultado, lista_de_páginas, num_pagina)
    elif num_resultado == 'A':
        if num_pagina != 1:
            imprimir_resultados(resultado, lista_de_páginas, num_pagina - 1)
        else:
            imprimir_resultados(resultado, lista_de_páginas, num_pagina)
    elif int(num_resultado) == 0 or not (num_pagina - 1) * 20 < int(num_resultado) <= (num_pagina - 1) * 20 + len(pagina):
        # pag1 : num > 0 and num <= 20
        # pag2 : num > 20 and num <= 40
        # pag3 : num > 40 and num <= 60
        return
    else:
        num_resultado_en_20 = int(num_resultado) - 20 * (num_pagina - 1)
        # pag1 : num
        # pag2 : num - 20
        # pag3 : num - 40
        # pag4 : num - 60
        id_a_buscar = pagina[num_resultado_en_20 - 1][0]
        ruta_fichero = pagina[num_resultado_en_20 - 1][5]

        with open(ruta_fichero, "r", encoding='utf-8') as f:
            for linea in f:
                lista_linea = linea.strip().split("\t")
                id = lista_linea[0]
                if id == id_a_buscar:
                    descripcion = lista_linea[5]
                    print('\n')
                    print(descripcion)

        imprimir_resultados(resultado, lista_de_páginas, num_pagina)


# Función que indica si la búsqueda se realiza por unión o por intersección.

def union_interseccion(busqueda):
    palabras = extrae_palabras(busqueda)
    if len(palabras) == 1:
        return busqueda, False

    union = True
    interseccion = True
    for i in range(len(palabras)):
        if i % 2 != 0:
            if palabras[i] != 'OR':
                union = False
            if palabras[i] != 'AND':
                interseccion = False

    busqueda_arreglada = ""
    if union or interseccion:
        for i in range(len(palabras)):
            if i % 2 == 0:
                busqueda_arreglada += palabras[i]
                busqueda_arreglada += " "
    else:
        busqueda_arreglada = busqueda
    return busqueda_arreglada, interseccion


# Función para buscar por descripción realizando la unión de las palabras.

def buscador_descripcion_union(busqueda, indice, entradasbd):
    result = []
    palabras = extrae_palabras(busqueda)
    for palabra in palabras:
        preproc = preprocesar(palabra)
        if preproc in indice:
            for posicion in indice[preproc]:
                if entradasbd[posicion] not in result:
                    result.append(entradasbd[posicion])
    return result


# Función para buscar por descripción realizando la intersección de las palabras.

def buscador_descripcion_interseccion(busqueda, indice, entradasbd):
    posiciones = range(len(entradasbd))
    result = []
    palabras = extrae_palabras(busqueda)
    for palabra in palabras:
        preproc = preprocesar(palabra)
        if preproc in indice:
            nuevas_posiciones = []
            for posicion in indice[preproc]:
                if posicion in posiciones:
                    nuevas_posiciones.append(posicion)
            posiciones = nuevas_posiciones
    for posicion in posiciones:
        result.append(entradasbd[posicion])
    return result


# Función que guarda los índices en ficheros en el directorio.

def guardar_indices_ficheros(indice, fichero, ruta_directorio):
    ruta = ruta_directorio + '\\' + fichero
    with open(ruta, 'w', encoding="utf-8") as f:
        if type(indice) == list:
            for tupla in indice:
                for elemento in tupla:
                    f.write(elemento + '\n')
                f.write('########\n')
        else:
            for clave in indice:
                f.write(clave + '\n')
                f.write(str(indice[clave]) + '\n')
                f.write('########\n')


# Función que lee los índices guardados en ficheros en el directorio.

def leer_indices_ficheros(indice, fichero, ruta_directorio):
    ruta = ruta_directorio + '\\' + fichero
    with open(ruta, 'r', encoding="utf-8") as f:

        if type(indice) == list:
            lista = []
            for linea in f:
                if linea.strip() == '########':
                    indice.append(tuple(lista))
                    lista = []
                else:
                    lista.append(linea.strip())

        else:
            clave = ''
            lista_numeros = []
            for linea in f:
                linea = linea.strip()

                if linea == '########':
                    indice[clave] = lista_numeros
                    clave = ''
                    lista_numeros = []

                elif linea != '' and linea[0] == '[' and linea[-1] == ']':
                    acumulador = ''
                    for i in range(1, len(linea)):
                        if linea[i] == ',' or linea[i] == ']':
                            lista_numeros.append(int(acumulador))
                            acumulador = ''
                        else:
                            acumulador += linea[i]

                else:
                    clave = linea


