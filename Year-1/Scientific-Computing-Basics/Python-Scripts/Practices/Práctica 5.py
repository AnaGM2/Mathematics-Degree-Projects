# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 08:41:37 2020

@author: gilpe
"""

##################################
#PRÁCTICA 5
##################################


import numpy as np
import matplotlib.pyplot as plt

#EJERCICIO 1
#Con las posiciones de Python:
def MatTridPython(n):
    A = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            if i==j:
                A[i,j] = i
            elif i==j+1 or i==j-1:
                A[i,j] = j
    return A
MatTridPython(3)
#Con las posiciones correctas:
def MatTrid(n):
    A = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            if i==j:
                A[i,j] = i+1
            elif i==j+1 or i==j-1:
                A[i,j] = j+1
    return A
MatTrid(4)


#EJERCICIO 2
#Dibujamos los 100 primeros términos de la sucesión:
v = []
for n in range(1,101):
    an = (n-np.sqrt(n))/(2*n+3*(n**2+2*n)**(1/3))
    v.append(an)
print(v)
np.array(v)
plt.plot(v)
#Otra forma:
for n in range(1,101):
    an = (n-np.sqrt(n))/(2*n+3*(n**2+2*n)**(1/3))
    plt.plot(n,an,'*b')
#Obtenemos el valor de k y ak pedidos:
n = 1
an = (n-np.sqrt(n))/(2*n+3*(n**2+2*n)**(1/3))
while np.abs(an-1/2)>0.005:
    n = n+1
    an = (n-np.sqrt(n))/(2*n+3*(n**2+2*n)**(1/3))
print([n,an])
#Obtenemos los ak con k múltiplo de 100000:
n = 1
an = (n-np.sqrt(n))/(2*n+3*(n**2+2*n)**(1/3))
while np.abs(an-1/2)>0.005:
    n = n+1
    an = (n-np.sqrt(n))/(2*n+3*(n**2+2*n)**(1/3))
    if n%100000 == 0:
        print([n,an])
#Programa que se detiene a los 3000000 de iteraciones:
n = 1
an = (n-np.sqrt(n))/(2*n+3*(n**2+2*n)**(1/3))
while np.abs(an-1/2)>0.005:
    n = n+1
    an = (n-np.sqrt(n))/(2*n+3*(n**2+2*n)**(1/3))
    if n%100000 == 0:
        print([n,an])
    if n>3000000:
        print([n,an])
        break
    
    
#EJERCICIO 3
#Primera forma
def ClasSist(A,b):
    """
    La matriz A debe ser cuadrada
    El vector b de términos independientes debe tener tantos elementos como filas tenga A
    """
    f,c = A.shape
    if f!=c:
        print("La matriz", A, "no es cuadrada")
    else:
        Amp = np.concatenate((A,b.T),axis=1)
        rA = np.linalg.matrix_rank(A)
        rAmp = np.linalg.matrix_rank(Amp)
        if rA!=rAmp:
            print('El sistema es incompatible')
        elif rA == c:
            print('El sistema es compatible determinado')
        else:
            print('El sistema es compatible indeterminado')
ClasSist(np.array([[1,2,-1],[1,1,1],[2,4,-2]]),np.array([[2,3,1]]))
#Segunda forma
def ClasSist2(A,b):
    f,c = A.shape
    if f==c:
        Ab = np.insert(A,c,b,1)
        rA = np.linalg.matrix_rank(A)
        rAb = np.linalg.matrix_rank(Ab)
        if rA==rAb:
            if rA==c:
                print('El sistema es compatible determinado')
            elif rA!=c:
                print('El sistema es compatible indeterminado')
        else:
            print('El sistema es incompatible')
    else:
        print('La matriz A debe ser cuadrada')
ClasSist2(np.array([[1,2,-1],[1,1,1],[2,4,-2]]),np.array([[2,3,1]]))


#EJERCICIO 4
#Usamos una función que calcula el determinante de una matriz de orden 2:
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
#Usamos una función que calcula el adjunto de A:
def adjunto(A,i,j):  
    fa,ca = A.shape
    B = np.copy(A)
    B = np.delete(B,i,0)
    return (-1)**(i+j)*det2(np.delete(B,j,1))
#Usamos una función que calcula el determinate de A:
def det3(A):
    fa,ca = A.shape
    det = 0
    if (fa!=3) or (ca!=3):
        print('La matriz debe ser de orden 3.')
    else:
        for j in range(fa):
            det = det + A[0,j]*adjunto(A,0,j)
    return det
#Definimos la función que calcula la inversa de A:
def InvMat(A):
    """
    La matriz A debe ser cuadrada
    """
    f,c = A.shape
    if f!=c:
        print("La matriz", A, "no es cuadrada")
    elif det3(A)==0:
        print("La matriz", A, "no tiene inversa")
    else:
        B = np.zeros((f,f))
        for i in range(f):
            for j in range(c):
                B[i,j] = adjunto(A,i,j)
        Ainv = B.T/det3(A)
        return Ainv
InvMat(np.array([[1,2,1],[1,1,1],[2,4,-2]]))
