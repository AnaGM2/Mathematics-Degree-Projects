# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 12:37:58 2022

@author: gilpe
"""

import numpy as np
import scipy.linalg as la


##########################
# EJERCICIO 1
##########################

def Jacobi(A,b,x0,norma,error,k):
    D = np.diag(np.diag(A))
    L = -np.tril(A-D)
    U = -np.triu(A-D)
    M = D
    N = L+U
    B = np.dot(la.inv(M),N)
    c = np.dot(la.inv(M),b)
    val = la.eig(B)[0]  # Da los valores propios y los vectores propios.
    ro = max(abs(val))
    if ro >= 1:
        print("El método no es convergente")
        return[x0,0,ro]
    i=1
    while True:
        if i>=k:
            print("El método no es convergente en", k, "iteraciones")
            return[x0,0,ro]
        x1=np.dot(B,x0)+c
        if la.norm(x1-x0,norma)<error:
            return[x1,i,ro]
        i=i+1
        x0=x1.copy()
        
        
##########################
# EJERCICIO 2
##########################

def Gauss_seidel(A,b,x0,norma,error,k):
    D = np.diag(np.diag(A))
    L = -np.tril(A-D)
    U = -np.triu(A-D)
    M = D-L
    N = U
    B = np.dot(la.inv(M),N)
    c = np.dot(la.inv(M),b)
    val = la.eig(B)[0]  # Da los valores propios y los vectores propios.
    ro = max(abs(val))
    if ro >= 1:
        print("El método no es convergente")
        return[x0,0,ro]
    i=1
    while True:
        if i>=k:
            print("El método no es convergente en", k, "iteraciones")
            return[x0,0,ro]
        x1=np.dot(B,x0)+c
        if la.norm(x1-x0,norma)<error:
            return[x1,i,ro]
        i=i+1
        x0=x1.copy()
        
        
##########################
# EJERCICIO 3
##########################

# Apartado a

A3a = np.array([[4,-1,0,-1,0,0],[-1,4,-1,0,-1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]],dtype=float)
b3a = np.array([0,5,0,6,-2,6],dtype=float)
x03a = np.zeros(6)

J3a = Jacobi(A3a,b3a,x03a,np.inf,10**(-6),100)
G3a = Gauss_seidel(A3a,b3a,x03a,np.inf,10**(-6),100)

print("Jacobi:",J3a[0])
print("Número de iteraciones:",J3a[1])
print("Radio espectral:",J3a[2])

print("Gauss-Seidel:",G3a[0])
print("Número de iteraciones:",G3a[1])
print("Radio espectral:",G3a[2])


# Apartado b

A3b = 12*np.eye(50) + np.diag(-2*np.ones(49),1) + np.diag(-2*np.ones(49),-1) + np.diag(np.ones(48),2) + np.diag(np.ones(48),-2)
b3b = 5*np.ones(50)
x03b = np.zeros(50)

J3b = Jacobi(A3b,b3b,x03b,np.inf,10**(-6),100)
G3b = Gauss_seidel(A3b,b3b,x03b,np.inf,10**(-6),100)

print("Jacobi:",J3b[0])
print("Número de iteraciones:",J3b[1])
print("Radio espectral:",J3b[2])

print("Gauss-Seidel:",G3b[0])
print("Número de iteraciones:",G3b[1])
print("Radio espectral:",G3b[2])
