# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 12:10:10 2022

@author: gilpe
"""

import numpy as np
import numpy.polynomial.polynomial as npp
import matplotlib.pyplot as plt
import scipy.integrate as sci


np.random.seed(0)   # Fijamos semilla


##########################
# EJERCICIO 1
##########################

A = np.random.randint(-4, 9, [5,5])
A

At = A.T    # Traspuesta
print(At)
det = np.linalg.det(A)      # Determinante
print(det)
Ainv = np.linalg.inv(A)     # Inversa
print(Ainv)
r = np.linalg.matrix_rank(A)    # Rango
r
np.dot(A,A)

A**2


##########################
# EJERCICIO 2
##########################

b = np.random.randint(2, 7, [5,1])
x =np.dot(Ainv,b)           # Una opción
xsol = np.linalg.solve(A,b)
print(xsol)


##########################
# EJERCICIO 3
##########################

A[0,:]                      # Primera fila
A[0]

A[:,4]                      # Última columna
A[:,-1]

A[1,2]                      # Elemento de la posición (2,3)

A[[0,2],:]                  # Fila 1 y 3

A[0:2,:]                    # Dos primeras filas

D = np.diag(np.diag(A))     # Matriz diagonal

d1 = np.diag(A,1)           # Diagonales
d_1= np.diag(A,-1)


##########################
# EJERCICIO 4
##########################

# En potencias crecientes
P1 = npp.Polynomial([2,-1,-2,1])
r1 = P1.roots()

x1 = np.linspace(-10,10,100)
plt.plot(x1,P1(x1),r1,P1(r1),'*r',x1,0*x1,'g')
plt.title("Gráfica de $P_1(x)$")
plt.xlabel('X')
plt.ylabel('Y')

# En potencias decrecientes
P = np.array([1,-2,-1,2])
r = np.roots(P)

x1 = np.linspace(-10,10,100)
plt.plot(x1,np.polyval(P,x1),r,np.polyval(P,r),'*r',x1,0*x1,'g')
plt.title("Gráfica de $P(x)$")
plt.xlabel('X')
plt.ylabel('Y')

raices = np.array([0,1])
npp.polyfromroots(raices)


##########################
# EJERCICIO 5
##########################

def f5(x):
    return np.exp(-3*x)*np.sin(x)

x = np.linspace(-1,0,100)
plt.plot(x,f5(x),'g',label='$exp(-3x)*sin(x)$')
plt.legend(loc='best')
plt.title("Gráfica de $f_5(x)$")
plt.xlabel('X')
plt.ylabel('Y')


##########################
# EJERCICIO 6
##########################

x1 = np.linspace(-np.pi,np.pi,100)
plt.plot(x1, np.sin(x1),'b',label='$sen(x)$')
plt.plot(x1,np.sin(x1)**2,'g',label='$sen(x)^2$')
plt.plot(x1,np.sin(x1**2),'r',label='$sen(x^2)$')
plt.legend(loc='best')
plt.title("Gráficas ejercicio 6")
plt.xlabel('X')
plt.ylabel('Y')
# Etiquetas juntas
plt.legend(('$sen(x)$','$sen(x)^2$','$sen(x^2)$'),loc='best')


##########################
# EJERCICIO 7
##########################

plt.figure(figsize=(10,14))

plt.subplot(3,1,1)
plt.plot(x1, np.sin(x1),'.-b',label='$sen(x)$')
plt.legend(loc='best')
plt.title("Gráfica $sen(x)$")
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(3,1,2)
plt.plot(x1,np.sin(x1)**2,'.g',label='$sen(x)^2$')
plt.legend(loc='best')
plt.title("Gráfica $sen(x)^2$")
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(3,1,3)
plt.plot(x1,np.sin(x1**2),'ro',label='$sen(x^2)$')
plt.legend(loc='best')
plt.title("Gráfica $sen(x^2)$")
plt.xlabel('X')
plt.ylabel('Y')


##########################
# EJERCICIO 8
##########################

aprox = sci.quad(lambda x:np.exp(x**3)*np.sin(x**2),-2,1)
print(['Aproximación: ', aprox[0]])
print(['Estim. error: ', aprox[1]])
x10 = np.linspace(-2,1,100)
y10 = np.exp(x10**3)*np.sin(x10**2)
plt.plot(x10,y10,color='blue')
plt.fill_between(x10, 0, y10, facecolor='blue', alpha = 0.45)


##########################
# EJERCICIO 9
##########################

def Fibo(n):
    if n==1:
        sol=[1]
    else:
        sol=[1,1]
        if n>2:
            for i in range(n-2):
                sol.append(sol[-1]+sol[-2])
    return sol

print(Fibo(1))
print(Fibo(20)) 


##########################
# EJERCICIO 10
##########################

def Fibo2(n):
    sol = [1,1]
    new = 2
    while new <= n:
        sol.append(new)
        new = sol[-1]+sol[-2]
    return sol

print(Fibo2(1000))
