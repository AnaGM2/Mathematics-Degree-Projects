import random
import time

# Implementación básica
def maximo_lista_basic(lista):
    maximo=None
    for elem in lista:
        if maximo is None or elem > maximo:
            maximo=elem
    return maximo

#Implementación DyV
def pequeno(X):
    return len(X) <= 1

def trivial(X):
    if len(X) > 0:
        return X[0]
    else:
        return None

def descomponer(X):
    mitad=len(X) // 2
    return [ X[:mitad] , X[mitad:] ]

def combinar(X):
    if X[0] > X[1]:
        return X[0]
    else:
        return X[1]

def maximo_lista_DyV(X):
    if pequeno(X):
        return trivial(X)
    solucionesParciales=[]
    for q in descomponer(X):
        solucionesParciales.append(maximo_lista_DyV(q))
    return combinar(solucionesParciales)


lista=[]
for i in range(1000000):
    lista.append(random.randint(1,500))

inicio=time.time()
print(maximo_lista_basic(lista))
fin=time.time()
print("Tiempo empleado: {}".format(fin-inicio))

inicio=time.time()
print(maximo_lista_DyV(lista))
fin=time.time()
print("Tiempo empleado: {}".format(fin-inicio))
