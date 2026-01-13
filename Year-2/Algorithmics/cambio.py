# Versión mejorada del ejercicio 3.1 de la práctica 2
# Los billetes y monedas disponibles también se solicitan

#Petición al usuario de la cantidad que se desea dividir
cantidad=int(input("Introduce la cantidad: "))

#Petición al usuario de los billetes y monedas disponibles
billetes_str=input("Introduce el valor de los billetes y monedas disponibles, separados por espacios en blanco: ")

#Conversión de la entrada a lista de números enteros
lista_billetes_str= billetes_str.split(" ")
lista_billetes=[]
for billete_str in lista_billetes_str:
    lista_billetes.append(int(billete_str))

#Cálculo de billetes y monedas
for billete_disponible in lista_billetes:
    if cantidad >= billete_disponible:
        billetes= cantidad // billete_disponible
        print(billetes, " de ", billete_disponible)
        cantidad= cantidad % billete_disponible
