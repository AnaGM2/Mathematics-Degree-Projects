# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:10:11 2022

@author: gilpe
"""

import numpy as np
import scipy.linalg as la


##########################
# EJERCICIO 1
##########################

# Apartado a

A = np.array([[3,1],[3,1.0001]],dtype=float)
b = np.array([7,7.0001])
x1 = la.solve(A,b)
print(x1)

b2 = np.array([7,6.9999])
x2 = la.solve(A,b2)
print(x2)

np.linalg.cond(A)
np.linalg.norm(A)*np.linalg.norm(np.linalg.inv(A))

A2 = np.array([[3,1],[3,1]],dtype=float)
x3 = la.solve(A2,b)
print(x3)   # Sistema incompatible.

b3 = np.array([7,7])
x4 = la.solve(A,b3)
print(x4)   # Sistema compatible indeterminado, da una solución pero son infinitas.

# El sistema está mal condicionado.
# Pequeñas modificaciones en los datos producen grandes cambios en los resultados.

# Apartado b

A3 = np.array([[0.003,1],[3,1]],dtype=float)
b4 = np.array([1.006,7])
x5 = la.solve(A3,b4)
print(x5)

np.linalg.cond(A3)

# Gauss: primera por mil y resto a la segunda
A4 = np.array([[0.003,1],[0,999]],dtype=float)
b5 = np.array([1.006,999])
np.linalg.cond(A4)  # Aumenta el número de condición

# Pivoteo parcial
# 3x+y=7
# 0.003x+y=1.006
A5 = np.array([[3,1],[0,-0.999]],dtype=float)
b6 = np.array([7,-0.999])
np.linalg.cond(A5)


##########################
# EJERCICIO 2
##########################

def cambio_filas(A,i,j):
    subs=np.copy(A[i])
    A[i] = A[j]
    A[j] = subs
    return A

def prod_fila(A,i,c):
    subs=np.copy(A[i])
    A[i] = c*subs
    return A

def suma_filas(A,i,j,c):
    subs=np.copy(A[i])
    A[i] = subs + c*A[j]
    return A

# Ejemplos:

A=np.identity(3)
cambio_filas(A,0,2)
prod_fila(A,1,1/2)
suma_filas(A,2,0,3/2)

A=np.array([[1,0,2],[-1,2,1],[3,2,-2]],dtype=float)
cambio_filas(A,0,2)
prod_fila(A,1,1/2)
suma_filas(A,2,0,3/2)


##########################
# EJERCICIO 3
##########################

def sust_Regresiva(A,b):
    n=len(A)
    x=np.zeros([n,1])
    for i in range(n-1,-1,-1):
        x[i] = (1/A[i,i])*(b[i]-np.dot(A[i,:],x))
    return x
    
# Ejemplo:
A= np.array([[1,2,3],[0,2,2],[0,0,1]],dtype=float)
b=np.array([0,0,6])
la.solve(A,b)
sust_Regresiva(A,b)

def sust_Progresiva(A,b):
    n=len(A)
    x=np.zeros([n,1])
    for i in range(0,n):
        x[n-1-i] = (1/A[i,n-1-i])*(b[i]-np.dot(A[i,:],x))
    return x
    
# Ejemplo:
A1= np.array([[0,0,1],[0,2,2],[1,2,3]],dtype=float)
b1=np.array([6,0,0])
la.solve(A1,b1)
sust_Progresiva(A1,b1)


##########################
# EJERCICIO 4
########################## 

def gauss_parcial_incompleto(A,b):
    n=len(A)
    for i in range(n):
        k=np.argmax(abs(A[i::,i]))+i #saber posicion, i ajusta contador
        cambio_filas(b,i,k)
        cambio_filas(A,i,k)
        
        for j in range(i+1,n):
            suma_filas(b,j,i,-A[j][i]/A[i][i]) #if A[i][i]==0, busca en la col y permuta
            suma_filas(A,j,i,-A[j][i]/A[i][i])          
    return sust_Regresiva(A,b)  

def gauss_parcial(A,b):
    n=len(A)
    for i in range(n):
        k=np.argmax(abs(A[i::,i])) + i
        cambio_filas(b,i,k)
        cambio_filas(A,i,k)
        
        if A[i][i] !=0:
            for j in range(i+1,n):
            # comprobar que A[i][i]!=0 y si no cambio_filas, poner if aquí
                suma_filas(b,j,i,-A[j][i]/A[i][i])
                suma_filas(A,j,i,-A[j][i]/A[i][i])
        else:
            for l in range(i+1,n):
                if A[l][i]!=0:
                    cambio_filas(b,i,l)
                    cambio_filas(A,i,l)
                    break
    return sust_Regresiva(A,b)

A = np.array([[1,2,-3],[3,1,-2],[2,-3,1]],dtype=float)
b = np.array([-16,-10,-4])
la.solve(A,b)
gauss_parcial(A,b)
gauss_parcial_incompleto(A,b)

A1 = np.array([[1,0,-3,2],[3,0,-2,2],[2,-3,1,4],[2,3,3,7]],dtype=float)
b1 = np.array([-16,-10,-4,12])
la.solve(A1,b1)
gauss_parcial(A1,b1)


##########################
# EJERCICIO 5
##########################  

A = np.array([[0,1,2],[1,1,-1],[2,1,0]],dtype=float)
Acopy = np.copy(A)
P = np.identity(len(A))

cambio_filas(A,0,1)
cambio_filas(P,0,1)

suma_filas(A,2,0,-2)
suma_filas(P,2,0,-2)

suma_filas(A,2,1,1)
suma_filas(P,2,1,1)

prod_fila(A,2,1/4)
prod_fila(P,2,1/4)

suma_filas(A,0,1,-1)
suma_filas(P,0,1,-1)

suma_filas(A,1,2,-2)
suma_filas(P,1,2,-2)

suma_filas(A,0,2,3)
suma_filas(P,0,2,3)

np.dot(P,Acopy)

la.inv(Acopy)


##########################
# EJERCICIO 6
##########################  

# A simétrica y definida positiva
A = np.array([[7,3,-1,2],[3,8,1,-4],[-1,1,4,-1],[2,-4,-1,6]],dtype=float)

# P es una matriz de permutaciones
# L es una matriz triangular inferior con unos en la diagonal
# U es una matriz triangular superior

P, L, U = la.lu(A)  # scipy, no está en numpy
P
L
U

# Verificación:
L@U
np.dot(L,U)
A

