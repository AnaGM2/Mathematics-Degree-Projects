from listas import es_numero

# Función que convierte una cadena con números separados por coma y espacio en una lista.


def convertir_a_lista(cadena):
    lista_final = []
    acumulador = ""
    for caracter in cadena:
        if es_numero(caracter):
            acumulador += caracter
        elif caracter == ",":
            lista_final.append(int(acumulador))
            acumulador = ""
        elif caracter != " ":
            raise ValueError("La cadena tiene un formato erróneo.")
    lista_final.append(int(acumulador))
    return lista_final


print(convertir_a_lista('2, 3, 4543, 4, 5667, 5'))
