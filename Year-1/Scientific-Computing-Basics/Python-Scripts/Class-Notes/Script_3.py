# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 00:36:28 2020

@author: julio
"""


import numpy as np
import matplotlib.pyplot as plt

# TUPLAS

# Las tuplas en Python son una secuencia de valores que pueden 
# ser de cualquier tipo, cadenas, enteros, floats, etc. Son objetos inmutables.

tupla1 = ("Python", True, "Python", "R", 5)
tupla2 = "Python", True, "Python", "R", 5

tupla1 == tupla2

# Extraer elementos:
    
tupla1[0]
tupla1[0:2]

# ¿Cambiar el valor de los elementos?

tupla1[0] = "dos"

# Recorrer una tupla:

for elem in tupla1:
    print(elem)

# Funciones sobre tuplas:
    
tupla1.count(True)
tupla1.count("Python")

tupla1.index(True)
tupla1.index("Python")
tupla1.index("Latex")

# Operaciones con tuplas:
    
tupla3 = 'uno', 'dos', 'tres', 'cuatro', 'cinco'

tupla1+tupla3
2*tupla1

# LISTAS

# Las listas en Python son una secuencia de valores que pueden 
# ser de cualquier tipo, cadenas, enteros, floats, etc. Son objetos mutables.

u = [1,2,3]
v = [0,1,2]
lista1 = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
lista2 = ['uno', 20 , 5.5 , [10, 15], 'cinco']

# Extraer elementos:
    
lista1[2]
lista1[0:3]
lista1[-1]

# Cambiar el valor de los elementos:
    
tercero = lista1[2]
print(tercero)
lista1[2] = 'tercero'

# Recorrer una lista:
    
for elem in lista1:
    print(elem)
    
lista3 = [1, 2, 3, 4, 5]
for i in range(len(lista3)):
    lista3[i]+=5

print(lista3)

# Funciones sobre listas:

lista1.count("uno")

lista1.index("dos")

lista3 = [1, 2, 3, 4, 5]
lista3.insert(1,'Hola')
print(lista3)

lista1 = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
lista1.append("uno más")
print(lista1)

lista4 = ['cde', 'fgh', 'abc', 'klm', 'opq']
lista4.sort()

lista5 = [3, 5, 2, 4, 1]
lista5.sort()

lista3 = [1, 2, 3, 4, 5]
lista3.reverse()
print(lista3)

lista1 = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
lista1.index('tres')

lista1 = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
lista1_modificada = lista1.pop(2)
print(lista1)
print(lista1_modificada)

lista1 = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
lista1_modificada = lista1.pop()
print(lista1)
print(lista1_modificada)


lista6 = [5, 3, 2, 4, 1]
print(len(lista6))
print(min(lista6))
print(max(lista6))
print(sum(lista6))

# Operaciones con listas:
    
u+v
2*u

# FUNCIONES

def mifuncion(x):
    2*np.sin(x)
    
mifuncion(1)

def mifuncion(x):
    return 2*np.sin(x)

mifuncion(1)

# Gráfica de una función:
    
x = np.linspace(0,np.pi)
x

x = np.linspace(0,np.pi,5)
y = mifuncion(x)

plt.plot(x,y)

x = np.linspace(0,np.pi,100)
y = mifuncion(x)

plt.plot(x,y)

plt.plot(x,y,'o')

plt.plot(x,y,'ro')

# Dos funciones en un mismo gráfico:
    
def mifuncion2(x):
    return 2*np.sin(2*x)

z = mifuncion2(x)

plt.plot(x,y)
plt.plot(x,z)

plt.plot(x,y,x,z)

# Dos gráficos en una misma imagen:

plt.subplot(121)
plt.plot(x,y)

plt.subplot(122)
plt.plot(x,z)

# Definir el tamaño de la imagen:

plt.figure(figsize=(10,5))

plt.subplot(121)
plt.plot(x,y)

plt.subplot(122)
plt.plot(x,z)