# Solución parcial al ejercicio 3.6 de la práctica 2

# Función que simplemente imprime el menú del programa
# No recibe ningún parámetro de entrada ni devuelve nada
def imprimir_menu():
    print("1. Introducir el primer vector")
    print("2. Introducir el segundo vector")
    print("3. Calcular la suma")
    print("4. Calcular la diferencia")
    print("5. Calcular el producto escalar")
    print("6. Finalizar")

# Primer vector: por defecto (0, 0, 0)
x1=0.0
y1=0.0
z1=0.0

# Segundo vector: por defecto (0, 0, 0)
x2=0.0
y2=0.0
z2=0.0

salir=False
while not salir:

    #Imprimir menú y pedir operacicón
    imprimir_menu()
    op=input("Introduce la operación: ")

    #Operaciones 1 y 2: lectura de primer y segundo vector
    if op == '1':
        x1= float(input("Introduce la componente x: "))
        y1 = float(input("Introduce la componente y: "))
        z1 = float(input("Introduce la componente z: "))
    elif op == '2':
        x2 = float(input("Introduce la componente x: "))
        y2 = float(input("Introduce la componente y: "))
        z2 = float(input("Introduce la componente z: "))
    #Operación 3: suma de vectores
    if op == '3':
        x3=x1+x2
        y3=y1+y2
        z3=z1+z2
        print("El resultado es ({}, {}, {})".format(x3,y3,z3))
    #Operación 6: salir
    if op== '6':
        salir=True
    else:
        print("Opción inválida")
