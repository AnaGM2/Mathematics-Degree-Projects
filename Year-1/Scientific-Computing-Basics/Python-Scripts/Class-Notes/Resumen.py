# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 13:08:20 2020

@author: gilpe
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si
from mpl_toolkits import mplot3d

 
##########################
#GENERAL
##########################

#Cociente
10//3

#Resto
10%3

#Cociente y resto
divmod(10,3)

#Redondeo
round(1.338747,1)

#Valor absoluto
abs(-2)

#Hipotenusa de un triángulo
np.hypot(2,3)

#De grados a radianes
np.radians(180)

#De radianes a grados
np.degrees(2*np.pi)

#Mínimo común múltiplo
np.lcm(12,20)

#Máximo común divisor
np.gcd(12,30)

#Parte real de un número complejo
np.real(2 + 3j)

#Parte imaginaria de un número complejo
np.imag(2 + 3j)

#Conjugado de un número complejo
np.conj(2 + 3j)
np.conjugate(2 + 3j)

#Parte entera
np.floor(-2.3)

#Parte entera por arriba
np.ceil(2.3)

#Entero más cercano a 0
np.fix(2.3)

#Convertir a número real para poder operar
float(1)

#Del primer al último elemento
range(1,100)

#Print con llaves
print('{}+{}={}'.format(1,2,3))

#Integral
si.quad(lambda x: 2*x,0,4.5)


##########################
#LISTAS, TUPLAS Y VECTORES
##########################

lista = [1,2,1,-3,1,2]
v = np.array([1.2,2.65,-4.89])
w = np.array([1,4,2])

#Añadir elemento al final de una lista
lista.append(7)

#Contar elemento de una lista
lista.count(1)

#Añadir elemento iterable al final de una lista
lista.extend(range(2))

#Primera posición de un elemento en una lista
lista.index(2)

#Añadir elemento a una lista
lista.insert(2,3.4)

#Eliminar último elemento de una lista
lista.pop()

#Eliminar elemento la primera vez que aparece en una lista
lista.remove(1)

#Invertir orden de una lista
lista.reverse()

#Ordenar una lista
lista.sort()

#Array linspace
np.linspace(0,10,100)

#Repetir elementos
np.repeat([1,2],[2,3])

#Array arange
np.arange(1,10,2)

#Array random
np.random.rand(4)
np.random.randint(1,10,3)
np.random.sample(2)

#Redondear elementos de un array
np.rint(v)

#Redondear elementos de un array hacia el más cercano a 0
np.fix(v)

#Producto vectorial
np.cross(v,w)


##########################
#MATRICES
##########################

A = np.array([[1,2,1],[9,3,5],[4,2,3]])
B = np.array([[2,3,5],[3,6,4]])
b = np.array([1,3,0])

#Matriz triangular
np.triu(A)
np.tril(A)

#Matriz inversa
np.linalg.inv(A)

#Determinante de una matriz
np.linalg.det(A)

#Matriz identidad
np.eye(3)

#Matriz transpuesta
A.T

#Rango de una matriz
np.linalg.matrix_rank(A)

#Eliminar fila o columna de una matriz
np.delete(A,2,1)

#Añadir fila o columna a una matriz
np.insert(A,2,np.array([3,2,1]),0)

#Juntar varias matrices
np.concatenate((A,B),0)

#Repeat
np.repeat(A,2,0)

#Random
np.random.randint(2,5,(2,5))

#Producto de matrices
np.dot(B,A)

#Traza de una matriz
np.trace(A)

#Sistema de ecuaciones
np.linalg.solve(A,b)

#Norma de una matriz
np.linalg.norm(A)

#Número de filas y de columnas
A.shape


##########################
#GRÁFICOS
##########################

def seno(x):
    return np.sin(x)
def coseno(x):
    return np.cos(x)
x = np.linspace(0,2*np.pi,100)
y = seno(x)
z = coseno(x)

#Varios en uno
plt.plot(x,y,x,z)

#Líneas rectas
plt.axvline(2,c='r')
plt.axhline(0,c='k')

#Cambiar límites
plt.xlim(1,5)
plt.ylim(-0.5,0.5)

#Varios separados
plt.subplot(211)
plt.plot(x,y,'r')
plt.subplot(212)
plt.plot(x,z,'k')

#Título
plt.title('Gráfica')

#Etiquetas de los ejes
plt.xlabel('Eje x')
plt.ylabel('Eje y')

#Leyenda
plt.legend(('Gráfica 1','Gráfica 2'),loc='lower right')

#Texto
plt.text(1,2,'Hola')

#Maya
plt.grid()

#Tamaño
plt.figure(figsize=(10,5))
plt.axis('equal')

#Transparencia
plt.plot(x,y,alpha=0.4)

#Tipo de símbolo
plt.plot(x,y,marker='o',mec='k',mew=2,mfc='r')

#Tipo de línea
plt.plot(x,y,ls='--',lw=3)

#Para representar funciones a trozos
np.vectorize(f)

#Gráficos 3D
ax = plt.axes(projection='3d')
x = np.linspace(0,100,1000)
y = np.sin(x)
z = np.cos(x)
ax.plot3D(x,y,z)

#Gráficos estadísticos
posición = [-1,4,9]
x = ['Primero','Segundo','Tercero']
y = [35,82,17]
plt.bar(posición,y)     #De barras
plt.xticks(posición,x)
plt.step(x,y)           #De escaleras
plt.hist(y,bins=2)      #Histograma
plt.pie(y,labels=x)     #De sectores
