def quitar_acentos(cadena):
	acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
	nueva_cadena = ""
	for i in cadena:
		if i in acentos:
			nueva_cadena += acentos[i]
		else:
			nueva_cadena += i
	return nueva_cadena


def combina_listas_cadenas(lista1, lista2):
	if len(lista1) != len(lista2):
		raise ValueError("La longitud de las listas no es la misma")
	
	nueva_lista = []
	
	for i in range(len(lista1)):
		if quitar_acentos(lista1[i].lower()) in quitar_acentos(lista2[-i-1].lower()):
			nueva_lista.append(lista2[-i-1])
		else:
			nueva_lista.append(lista1[i]+lista2[-i-1])
	return nueva_lista


lista1=[ "Al", "GO", "RIT" , "MIA" ]

lista2=[  "algoritmo" , "algorítmico", "gol", "ál" ]

print(combina_listas_cadenas(lista1, lista2))
		