palabra = input("Introduce la palabra a buscar: ")
intentos = 6
adivinadas = []

for i in range(1, 20):
    print("")

for j in range(len(palabra)):
    print("_ ", end="")


while intentos > 0:
    letra = input("\nDame una letra o una palabra: ")

    if len(letra) == 1 and len(palabra) > 1:
        if letra in palabra:
            adivinadas.append(letra)
            for i in range(len(palabra)):
                if palabra[i] in adivinadas:
                    print(palabra[i], " ", end="")
                else:
                    print("_ ", end="")
        else:
            intentos -= 1
            if intentos > 0:
                print("La palabra no contiene esa letra, te quedan", intentos, " intentos.")
            else:
                print("Lo siento, has perdido, te has quedado sin intentos.")

    else:
        if letra == palabra:
            print("¡Enhorabuena, has ganado!")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print("Esa no es la palabra correcta, te quedan ", intentos, " intentos.")
            else:
                print("Lo siento, has perdido, te has quedado sin intentos.")
