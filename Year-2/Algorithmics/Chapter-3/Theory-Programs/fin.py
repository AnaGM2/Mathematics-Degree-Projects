 # Programa que pide números en coma flotante por teclado
 # hasta que el usuario introduce la cadena 'fin'
 # Al final, imprime la media de los números introducidos

num=input("Dame un número: ")
suma=0
contador=0

while num != 'fin':
    suma += float(num)
    contador += 1
    num=input("Dame un número: ")

if contador > 0:
    print("La media es ", suma/contador)
else:
    print("No has introducido ningún número")
