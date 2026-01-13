# Función que devuelve una lista con números introducidos individualmente hasta escribir fin.

def introducir_lista():
    lista = []
    entrada = input('Introduzca un número: ')
    while entrada != 'fin':
        try:
            numero = int(entrada)
            lista.append(numero)
            entrada = input('Introduzca un número: ')
        except ValueError:
            raise ValueError('Esto no es un múmero entero.')
    return lista


print(introducir_lista())
