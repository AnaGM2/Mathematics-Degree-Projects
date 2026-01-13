def elimina_duplicados (lista):
	if len(lista) == 1:
		return lista
	else:
		if lista[0] in lista[1:]:
			return elimina_duplicados(lista[1:])
		else:
			return [lista[0]] + elimina_duplicados(lista[1:])

print(elimina_duplicados([1, 8, 4, 3, 8 ]))
