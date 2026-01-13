# Programa que detecta un número en coma flotante.

num = input("Introduce un número en coma flotante: ")
flotante = True
contador = 0

for i in range(0, len(num)):
    if num[i] != "0" and num[i] != "1" and num[i] != "2" and num[i] != "3" and num[i] != "4" and num[i] != "5" \
            and num[i] != "6" and num[i] != "7" and num[i] != "8" and num[i] != "9" and num[i] != ".":
        flotante = False
    elif num[i] == ".":
        contador += 1
        if i == 0 or i == len(num)-1:
            flotante = False

if contador > 1 or flotante == False:
    print("No es un número en coma flotante.")
else:
    print("Es un número en coma flotante.")
