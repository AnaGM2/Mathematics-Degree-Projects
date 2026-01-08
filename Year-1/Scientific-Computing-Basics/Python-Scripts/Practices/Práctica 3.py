# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 08:56:42 2020

@author: gilpe
"""

##################################
#PRÁCTICA 3
##################################


import numpy as np
import matplotlib.pyplot as plt


#EJERCICIO 1
a = "hola mundo"
type(a)
#Cadena de caracteres
b = (1,3,"hola",True)
type(b)
#Tupla
c = [1,3,"hola",True]
type(c)
#Lista
a[0]
#Da el primer caracter
a[5:]
#Da los caracteres a partir del sexto
a[::3]
#Da los caracteres de 3 en 3
b[0]
#Da el primer elemento
b[1:]
#Da los elementos a partir del segundo
b[1:2]
#Da el segundo elemento
c[1:]
#Da los elementos a partir del segundo
c[:2]
#Da los elementos hasta el segundo
c[0:2]
#Da los 2 primeros elementos
c[::2]
#Da los elementos de 2 en 2
c[-1]
#Da el último elemento
c[-2]
#Da el penúltimo elemento


#EJERCICIO 2
L = ["una lista",[1,2]]
L[0]
#Da el primer elemento
L[1][0]
#Da el primer elemento de la lista que es el segundo elemento de L
L[1][1]
#Da el segundo elemento de la lista que es el segundo elemento de L


#EJERCICIO 3
t = 1,2,3
T = (1,2,3)
type(t)==type(T)
#Son del mismo tipo (tuplas)


#EJERCICIO 4
a = [66.25,333,333,1,1234.5]
print(a.count(333),a.count(66.25),a.count("x"))
#Cuenta cuántos de cada uno de los elementos hay en la lista
a.insert(2,-1)
#Añade un -1 en la tercera posición
a.append(333)
#Añade un 333 al final
a.index(333)
#Devuelve la primera posición en la que aparece el 333
a.remove(333)
#Elimina el primer 333 que aparece en la lista
a.reverse()
#Invierte el orden de la lista
a.sort()
#Ordena los elementos de la lista de menor a mayor
a.pop()
#Devuelve y elimina el último elemento de la lista


#EJERCICIO 5
A = np.eye(6)
B = np.tril(-np.ones(6),-2)
C = np.diag(np.exp(1)*np.ones(4),2)
D = np.diag(np.pi*np.ones(3),3)
E = np.diag(3*np.ones(2),4)
F = np.diag(-np.ones(1),5)
M = A+B+C+D+E+F


#EJERCICIO 6
def trig(a):
    s = np.sin(a)
    c = np.cos(a)
    t = np.tan(a)
    return s,c,t
trig(np.pi/2)
trig(np.pi)


#EJERCICIO 7
def circu(r):
    A = np.pi*r**2
    L = 2*np.pi*r
    return(A,L)
circu(3)


#EJERCICIO 8
x = np.linspace(0,2*np.pi)
plt.plot(x,np.sin(x),'r',x,np.cos(x),'g:')
plt.title('Seno y coseno')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(('Seno','Coseno'), loc = 'lower right')


#EJERCICIO 9
x = np.linspace(-5*np.pi,5*np.pi,200)
plt.figure(figsize = (15,5))
plt.subplot(131)    #1 fila, 3 columnas, posición 1
plt.plot(x,x*np.sin(x),'y--')
plt.title('xsin(x)')
plt.xlabel('x')
plt.ylabel('xsin(x)')
plt.subplot(132)    #1 fila, 3 columnas, posición 2
plt.plot(x,x*np.cos(x),'c:')
plt.title('xcos(x)')
plt.xlabel('x')
plt.ylabel('xcos(x)')
plt.subplot(133)    #1 fila , 3 columnas, posición 3
plt.plot(x,x*np.log(x),'m-.')
plt.title('xln(x)')
plt.xlabel('x')
plt.ylabel('xln(x)')


#EJERCICIO 10
def f(x):
    f = x**3-4*x**2+x+6
    return f

def derf(x):
    df = 3*x**2-8*x+1
    return df


x = np.linspace(-2,4,100)
plt.plot(x,f(x),'b',0,f(0),'*g',np.roots(np.array([1,-4,1,6])),[0,0,0],'ro',x,x+6,'y')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráficas ejercicio 10')