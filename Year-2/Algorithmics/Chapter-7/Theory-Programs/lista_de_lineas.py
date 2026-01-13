nombre_archivo = "input.txt"

with open(nombre_archivo, 'r', encoding='utf-8') as f:
    lista_de_lineas= []
    for linea in f:
        lista = []
        if linea[-1] == "\n":
            linea = linea[:-1]
        campos = linea.split(':')[1].split(',')
        for elem in campos:
            lista.append(float(elem))
        lista_de_lineas.append(lista)
    print(lista_de_lineas)
    
