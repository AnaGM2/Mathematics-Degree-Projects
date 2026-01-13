from sys import argv

def leer_matriz(fichero):
	matriz = []
	with open(fichero, 'r', encoding="utf8") as f:
		for line in f:
			line = line.strip()
			fila = line.split(' ')
			fila_numeros = []
			for cad in fila:
				fila_numeros.append(int(cad))
			
			matriz.append(fila_numeros)
	return matriz
	
def borde_matriz(matriz):
	numeros_bordes = []
	for elemento in matriz[0]:
		numeros_bordes.append(elemento)
	for elemento in matriz[-1]:
		numeros_bordes.append(elemento)
	for fila in matriz:
		numeros_bordes.append(fila[0])
	for fila in matriz:
		numeros_bordes.append(fila[-1])
	return numeros_bordes

	
matriz1 = leer_matriz(argv[1])
matriz2 = leer_matriz(argv[2])

bordes_matriz1 = borde_matriz(matriz1)
suma_bordes_matriz1 = 0
cache_bordes = []

for element in bordes_matriz1:
	if element not in cache_bordes:
		suma_bordes_matriz1 += element
		cache_bordes.append(element)

esquinas_matriz2 = [ matriz2[0][0], matriz2[0][-1], matriz2[-1][0], matriz2[-1][-1] ]
suma_esquinas_matriz2 = 0
for element in esquinas_matriz2:
	suma_esquinas_matriz2 += element
	
print(suma_bordes_matriz1 - suma_esquinas_matriz2)

