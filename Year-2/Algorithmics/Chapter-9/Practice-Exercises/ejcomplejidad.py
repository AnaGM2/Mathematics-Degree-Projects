def examen1(lista):
	for i in range(0, 2):
		for j in range(0, i+1):
			prod = 1
			k = 0
			while prod != 0 and k < len(lista):
				prod = prod * lista[k]
				k += 1
			print(prod)

# Talla del problema: len(lista) o (n)
# Mejor caso: El primer elemento de lista es 0
# Peor caso: No hay ceros en la lista
# Cota inferior: ci(n)=1, Ω(1)
# Cota superior: cs(n)=1+n, O(n)