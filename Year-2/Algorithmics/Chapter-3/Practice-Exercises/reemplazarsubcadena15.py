# Función que reemplaza todas las apariciones de una subcadena por otra dada.

def reemplazar_subcadena(cadenalarga, busqueda, reemplazo):
    resultado = ""
    skip = 0
    for i in range(len(cadenalarga)):
        if skip > 0:
            skip -= 1
            continue
        if len(cadenalarga[i:]) < len(busqueda):
            resultado += cadenalarga[i:]
            break
        if cadenalarga[i:i + len(busqueda)] == busqueda:
            resultado += reemplazo
            skip = len(busqueda) - 1
        else:
            resultado += cadenalarga[i]
    return resultado


print(reemplazar_subcadena("Cadena de entrada", "en", "AA"))
