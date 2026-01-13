def quitar_acentos(cadena):
	acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
	nueva_cadena = ""
	for i in cadena:
		if i in acentos:
			nueva_cadena += acentos[i]
		else:
			nueva_cadena += i
	return nueva_cadena


def ordenada(cad):
	if len(cad) == 1:
		return True
	else:
		if quitar_acentos(cad[0].lower()) < quitar_acentos(cad[1].lower()):
			return ordenada(cad[1:])
		else:
			return False
