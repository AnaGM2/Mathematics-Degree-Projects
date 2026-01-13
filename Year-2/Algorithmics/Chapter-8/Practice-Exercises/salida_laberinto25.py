# Función que encuentra el camino más corto entre el punto (0, 0) al (n-1, m-1) en una matriz de nxm.

def valido(punto, mapa, anteriores):
    comprobacion0 = punto[0] < len(mapa) and punto[0] >= 0
    comprobacion1 = punto[1] < len(mapa[0]) and punto[1] >= 0
    return (comprobacion0 and comprobacion1) and mapa[punto[0]][punto[1]] == 0 and punto not in anteriores


def camino_mas_corto(opcion1, opcion2, opcion3, opcion4):
    opcion_mas_corta = None
    if opcion1 != None:
        opcion_mas_corta = opcion1
    if opcion2 != None and (opcion_mas_corta == None or len(opcion2) < len(opcion_mas_corta)):
        opcion_mas_corta = opcion2
    if opcion3 != None and (opcion_mas_corta == None or len(opcion3) < len(opcion_mas_corta)):
        opcion_mas_corta = opcion3
    if opcion4 != None and (opcion_mas_corta == None or len(opcion4) < len(opcion_mas_corta)):
        opcion_mas_corta = opcion4
    return opcion_mas_corta


def salida_laberinto(mapa, destino, anteriores):

    if destino[0] == 0 and destino[1] == 0:
        return []

    else:
        punto_opcion1 = [destino[0] - 1, destino[1]]
        punto_opcion2 = [destino[0], destino[1] - 1]
        punto_opcion3 = [destino[0] + 1, destino[1]]
        punto_opcion4 = [destino[0], destino[1] + 1]

        if valido(punto_opcion1, mapa, anteriores):
            anteriores.append(destino)
            opcion1 = salida_laberinto(mapa, punto_opcion1, anteriores).append("abajo")
        if not valido(punto_opcion1, mapa, anteriores):
            opcion1 = None

        if valido(punto_opcion2, mapa, anteriores):
            anteriores.append(destino)
            opcion2 = salida_laberinto(mapa, punto_opcion2, anteriores).append("derecha")
        if not valido(punto_opcion2, mapa, anteriores):
            opcion2 = None

        if valido(punto_opcion3, mapa, anteriores):
            anteriores.append(destino)
            opcion3 = salida_laberinto(mapa, punto_opcion3, anteriores).append("arriba")
        if not valido(punto_opcion3, mapa, anteriores):
            opcion3 = None

        if valido(punto_opcion4, mapa, anteriores):
            anteriores.append(destino)
            opcion4 = salida_laberinto(mapa, punto_opcion4, anteriores).append("izquierda")
        if not valido(punto_opcion4, mapa, anteriores):
            opcion4 = None

        return camino_mas_corto(opcion1, opcion2, opcion3, opcion4)


maze = [
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0]
]


print(salida_laberinto(maze, [len(maze) - 1, len(maze[0]) - 1], []))
