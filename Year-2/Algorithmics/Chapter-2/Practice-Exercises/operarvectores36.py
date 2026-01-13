def imprimir_menu():
    print('1) Introducir el primer vector')
    print('2) Introducir el segundo vector')
    print('3) Calcular la suma')
    print('4) Calcular la diferencia')
    print('5) Calcular el producto escalar')
    print('6) Finalizar')


def producto_escalar(vector1, vector2):
    prod = 0
    for i in range(0, len(vector1)):
        prod += vector1[i] * vector2[i]
    return prod


x1 = 0.0
y1 = 0.0
z1 = 0.0

x2 = 0.0
y2 = 0.0
z2 = 0.0

salir = False
while not salir:
    imprimir_menu()
    op = input('Introduce la operación: ')

    if op == '1':
        x1 = float(input('Introduce la componente x: '))
        y1 = float(input('Introduce la componente y: '))
        z1 = float(input('Introduce la componente z: '))

    if op == '2':
        x2 = float(input('Introduce la componente x: '))
        y2 = float(input('Introduce la componente y: '))
        z2 = float(input('Introduce la componente z: '))

    if op == '3':
        x3 = x1 + x2
        y3 = y1 + y2
        z3 = z1 + z2
        print('El resultado es ({},{},{})'.format(x3, y3, z3))

    if op == '4':
        x3 = x1 - x2
        y3 = y1 - y2
        z3 = z1 - z2
        print('El resultado es ({},{},{})'.format(x3, y3, z3))

    if op == '5':
        vector1 = (x1, y1, z1)
        vector2 = (x2, y2, z2)
        print('El resultado es ', producto_escalar(vector1, vector2))

    if op == '6':
        salir = True
