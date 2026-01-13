# Función que indica si un número es primo.

def esprimo(num):
    es_primo = True
    for div in range(2, num):
        if num % div == 0:
            es_primo = False
            break
    return es_primo


# Función que comprueba si una cadena es un palíndromo.

def palindromo(cadena):

    es_palin = True

    for i in range(0, len(cadena)//2):
        if cadena[i] != cadena[-i-1]:
            es_palin = False

    return es_palin


# Función que calcula el factorial de un número.

def factorial(num):
    fact = 1
    if num != 0:
        for cifra in range(1, num+1):
            fact *= cifra
    return fact



# Función que calcula el superfactorial de un número.

# from variablesyfunciones import factorial
def superfactorial(num):
    superfact = 1
    for cifra in range(2, num+1):
        superfact *= factorial(cifra)
    return superfact



# Función que calcula el compositorial de un número.

# from variablesyfunciones import esprimo
def compositorial(num):
    if num <= 3:
        return 1
    else:
        resultado = 1
        for i in range(4, num + 1):
            if not esprimo(i):
                resultado *= i
        return resultado



# Función que calcula el coeficiente binomial de dos números.

# from variablesyfunciones import factorial
def binomial(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))


# Función que imprime el menú de operaciones con vectores.

def imprimir_menu():
    print('1) Introducir el primer vector')
    print('2) Introducir el segundo vector')
    print('3) Calcular la suma')
    print('4) Calcular la diferencia')
    print('5) Calcular el producto escalar')
    print('6) Finalizar')


# Función que calcula el producto escalar de dos vectores.

def producto_escalar(vector1, vector2):
    prod = 0
    for i in range(0,len(vector1)):
        prod += vector1[i] * vector2[i]
    return prod
