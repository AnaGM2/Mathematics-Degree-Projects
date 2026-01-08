# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 09:27:12 2020

@author: gilpe
"""

##################################
#PRÁCTICA 4
##################################


import numpy as np
import matplotlib.pyplot as plt


#EJERCICIO 1
#Circunferencia de radio 2 centrada en el (1,3)
r = 2
a = 1
b = 3
t = np.linspace(0,2*np.pi)
x = a+r*np.cos(t)
y = b+r*np.sin(t)
plt.axis("equal")
plt.plot(x,y) 
#Función
def circu2(a,b,r):
    t = np.linspace(0,2*np.pi)
    x = a+r*np.cos(t)
    y = b+r*np.sin(t)
    plt.axis("equal")
    plt.plot(x,y)
#Damos valores 
circu2(1,1,2)
circu2(1,-1,6)
circu2(2,7,1)


#EJERCICIO 2
#Elipse con semiejes 2 y 1
c = 2
d = 1
t = np.linspace(0,2*np.pi)
x = c*np.cos(t)
y = d*np.sin(t)
plt.axis("equal")
plt.plot(x,y) 
#Función
def elipse(c,d):
    t = np.linspace(0,2*np.pi)
    x = c*np.cos(t)
    y = d*np.sin(t)
    plt.axis("equal")
    plt.plot(x,y)
#Damos valores
elipse(2,1)
elipse(2,19)
#Probamos a meter la circunferencia y la elipse en una función
def circu_elipse(a,b,r,c,d):
    t = np.linspace(0,2*np.pi)
    x = a+r*np.cos(t)
    y = b+r*np.sin(t)
    plt.axis("equal")
    plt.plot(x,y,"r")
    z = c*np.cos(t)
    w = d*np.sin(t)
    plt.axis("equal")
    plt.plot(z,w)
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.title("CIRCUNFERENCIA Y ELIPSE")
    plt.legend(("Circunferencia","Elipse"),
               loc = 'best')
#Damos valores
circu_elipse(1,1,2,1,3)
circu_elipse(2,5,1,7,2)
circu_elipse(0,0,1,1,2)
circu_elipse(0,0,1,2,1)
circu_elipse(1,1,0.5,1,2)
circu_elipse(1,1,0.5,2,1)


#EJERCICIO 3
#Pintamos una parábola
a = 1
b = 2
c = 3
def parab(x):
    return a*x**2+b*x+c
x = np.linspace(-10,10)
y = parab(x)
plt.plot(x,y)
#Hacemos la función
def Parabola(a,b,c):
    def parab(x):
        return a*x**2+b*x+c
    x = np.linspace(-10,10)
    y = parab(x)
    vx = -b/(2*a)
    vy = parab(vx)
    plt.plot(x,y,"black")
    plt.axvline(-b/(2*a),c = 'r')
    plt.axhline(-b/(2*a),c = 'r')
    plt.plot(vx,vy,"*g")
#Damos valores
Parabola(-3,-2,1)
Parabola(6,7,6)


#EJERCICIO 4
def traza(A):
   d = np.diag(A)
   return sum(d)
traza(np.array([[1,2,3],[2,4,5]]))


#EJERCICIO 5
#Primera opción
np.arange(1,100,2)
#Segunda opción
for x in range(1,100):
    if x%2==1:
        print(x)
#Tercera opción
for i in range(1,100,2):
    print(i)
#Cuarta opción
def impares(x):
    v = []
    for i in range(x):
        if i%2!=0:
            v.append(i)
    return(v)
impares(100)


#EJERCICIO 6
#Primera función
def entero(n):
    if n==int(n):
        print('El número',n,'es entero.')
    else:
        print('El número',n,'no es entero.')
entero(12)
entero(2.4)
#Segunda función
def primo1(n):
    if n==1:
        print(n,'no es primo.')
    else:
        primo = True 
        for i in range(2,n):
            if n%i==0:
                primo = False
        if primo==True:
            print(n,'es primo.')
        else:
            print(n,'no es primo.')
primo1(13)
primo1(14)
def primo2(n):
    cont=0
    for i in range(2,n):
        resto = n%i
        print('{} % {} = {}'.format(n,i,resto))
        if resto==0:
            cont=cont+1
    if cont==0:
        print('El número {} es un número primo.'.format(n))
    else:
        print('El número {} no es un número primo.'.format(n))
primo2(12)
primo2(13)


#EJERCICIO 7
def sumMat(A,B):
    fa,ca = A.shape
    fb,cb = B.shape
    if (fa!=fb) or (ca!=cb):
        print('las matrices no tienen las mismas dimensiones.')
    else:
        C = np.zeros([fa,ca])
        for i in range(0,fa):
            for j in range(0,ca):
                C[i,j] = A[i,j]+B[i,j]
        return C
sumMat(2*np.ones([3,3]),3*np.ones([3,3]))


#EJERCICIO 8
def prodMat(A,B):
    fa,ca = A.shape
    fb,cb = B.shape
    if (ca!=fb):
        print('las matrices no tienen las dimensiones adecuadas.')
    else:
        C = np.zeros([fa,cb])
        #Hay que rellenar cada elemento C[i,j]
        for i in range(0,fa):
            for j in range(0,cb):
                C[i,j] = np.dot(A[i,:],B[:,j])
        return C 
prodMat(2*np.ones([3,3]),np.array([[1,2,3],[2,4,5],[1,2,4]]))


#EJERCICIO 9
def det2(A):
    """
    El argumento de entrada debe ser una matriz 2 por 2
    """
    fa,ca = A.shape
    D = 0
    if (ca==fa & ca==2):
        D = A[0,0]*A[1,1]-A[0,1]*A[1,0]
    else:
        print("La matriz no tiene la dimensión adecuada")
        D = None
    return D
det2(2*np.ones([2,2]))
det2(np.ones([3,3]))


#EJERCICIO 10
def adjunto(A,i,j):  
    fa,ca = A.shape
    B = np.copy(A)
    B = np.delete(B,i,0)
    return (-1)**(i+j)*det2(np.delete(B,j,1))
def det3(A):
    fa,ca = A.shape
    det = 0
    if (fa!=3) or (ca!=3):
        print('La matriz debe ser de orden 3.')
    else:
        for j in range(fa):
            det = det + A[0,j]*adjunto(A,0,j)
    return det
det3(np.array([[1,2,-1],[1,1,1],[2,4,-2]]))
            
