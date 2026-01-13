class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y


origen = [0,0]
destino = Point(3, 3)

maze = [
  [0, 0, 1, 0],
  [0, 0, 1, 0],
  [1, 0, 0, 0],
  [1, 1, 0, 0],
]

a=[]
len(a)

#camino((0,0), (3,3)) = camino((0,0), (2,3)).append("abajo") ("abajo", "derecha", "abajo"...)
#camino((0,0), (3,3)) = camino((0,0), (3,2)).append("derecha") ("abajo", "derecha", "abajo"...)

def camino(dest, anterior):
  opcion1 = camino(Point(b.x - 1, b.y))
  opcion2 = camino(Point(b.x, b.y - 1))
  opcion3 = camino(Point(b.x + 1, b.y))
  opcion4 = camino(Point(b.x, b.y + 1))

  opcion_mas_corta=None
  if (opcion1 != None):
    opcion_mas_corta=opcion1
  if (opcion2 != None and (opcion_mas_corta == None or len(opcion2) < len(opcion_mas_corta))):
    opcion_mas_corta=opcion2
  if (opcion3 != None and (opcion_mas_corta == None or len(opcion3) < len(opcion_mas_corta))):
    opcion_mas_corta=opcion3
  if (opcion4 != None and (opcion_mas_corta == None or len(opcion4) < len(opcion_mas_corta))):
    opcion_mas_corta=opcion4
  return opcion_mas_corta

def valido(b: Point):
  return (b.x <= 3 and b.y <= 3) and maze[b.x][b.y] == 0