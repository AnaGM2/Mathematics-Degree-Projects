def menor_fila(i, matriz1, matriz2):
	filas_concat = matriz1[i] + matriz2[i]
	menor_numero = matriz1[i][0]
	for element in filas_concat:
		if element < menor_numero:
			menor_numero = element
	return menor_numero

def maximo_columna(j, matriz1, matriz2):
	columnas_concat = []
	# for i in range(len(matriz1)):
	#	columnas_concat += [matriz1[i][j]), matriz2[i][j]]
	for fila in matriz1:
		columnas_concat.append(fila[j])
	for fila in matriz2:
		columnas_concat.append(fila[j])
	
	maximo_numero = matriz1[0][j]
	for element in columnas_concat:
		if element > maximo_numero:
			maximo_numero = element
	return maximo_numero

def combina_matrices(matriz1, matriz2):
	if len(matriz1) != len(matriz2):
		raise ValueError("Las matrices no tienen el mismo número de filas")
	for i in range(len(matriz1)):
		if len(matriz1[i]) != len(matriz1[0]) or len(matriz2[i]) != len(matriz1[0]):
			raise ValueError("Las matrices no tienen el mismo número de columnas")

	matriz_salida = []
	
	for i in range(len(matriz1)):
		matriz_salida.append([])
		for j in range(len(matriz1[i])):
			if matriz1[i][j] < matriz2[i][j]:
				matriz_salida[i].append(menor_fila(i, matriz1, matriz2))
			else:
				matriz_salida[i].append(maximo_columna(j, matriz1, matriz2))
	
	return matriz_salida
	
A=[   
[0,-1,-2,3],   
[4,-3,2,8],   
[3,2,1,0]
]

B=[   
[7,8,-2,-3],   
[5,6,0,-8],   
[0,2,6,-5]
]

print(combina_matrices(A, B))