# -*- coding: utf-8 -*-
"""
Created on Wed Nov 04 00:36:28 2020

@author: julio
"""


import numpy as np
import matplotlib.pyplot as plt


def mifuncion(x):
    return x**2

x = np.linspace(-10,10)
y = mifuncion(x)

plt.plot(x,y)

# REPRESENTACIÓN GRÁFICA DE CURVAS EN ECUACIONES PARAMÉTRICAS

# La curva f(x)=x**2 puede expresarse en coordenadas paramétricas como:
# x(t)=t
# y(t)=t**2
# con t en (-10,10).

t = np.linspace(-10,10)
x = t
y = t**2

plt.plot(x,y)

# Muchas curvas tales como circunferencias, elipses, etc. pueden expresarse
# en coordenadas paramétricas.

# Por ejemplo, la circunferencia de centro (0,0) y radio r:
# x(t) = r*sin(t)
# y(t) = r*cos(t)
# con t en (0,2*pi).

r = 2
t = np.linspace(0,2*np.pi)
x = r*np.cos(t)
y = r*np.sin(t)

plt.plot(x,y) # Parece una elipse...
    
# Una opción:
    
plt.figure(figsize=(5,5))
plt.plot(x,y) 

# Otra opción:
    
plt.axis("equal")
plt.plot(x,y)  

# Las representaciones gráficas se pueden integrar en funciones:
    
def circu1(r):
    t=np.linspace(0,2*np.pi,100)
    x=r*np.cos(t)
    y=r*np.sin(t)
    plt.axis("equal")
    plt.plot(x,y,'k')

circu1(2)

# Sin embargo, una función que esté destinada a formar parte de otros cálculos
# debe devolver un return:
    
def area_triangulo(base,altura):
    return base*altura/2

area = area_triangulo(1,2)

2*area

# Se puede invertir el orden de los argumentos si los llamamos por su nombre:

area_triangulo(altura = 2, base = 1)

# También se le puede pedir al usuario la base y la altura:
    
def area_triangulo2():
    base = float(input("Introduzca la base del triángulo:"))
    altura = float(input("Introduzca la altura del triángulo:"))
                   
    return base*altura/2    

area_triangulo2()

area = area_triangulo2()

# Bucle if:
    
def par(n):
    if n%2 == 0:
        print("n es par")
    else: 
        print("n es impar")
        
par(4)

# Bucle for:
    
def pares1(n):
    for i in np.arange(0,n,2):
        print(i)
        
pares1(9)

def pares2(n):
    lista = []
    for i in range(n):
        if i%2 == 0:
            lista.append(i)
    return lista

pares2(10)

# Bucle while:
    
# Sabemos que la sucesión (1+1/n)**n tiende al número e cuando n tiende a
# infinito.

e = np.exp(1)

# Esto quiere decir que dado epsilon>0, existe un n0 tal que si n>=n0 entonces
# |xn-e|<epsilon.

def sucesion1(epsilon):
    n = 1 # En el primer paso...
    x = 2 # El primer elemento de la sucesión vale 2.
    lista = [2]
    while abs(x-e)>epsilon: # Si queremos términos más cercanos que epsilon...
        n = n+1 # Damos más pasos
        x = (1+1/n)**n
        lista.append(x) # Que añadimos a la lista.
    return lista # Devolvemos la lista.

sucesion1(0.5)
sucesion1(0.05)
sucesion1(0.005)