# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:10:43 2022

@author: gilpe
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci

# Polinomios de Chebyshev
def Chebyshev(n):      
    if n == 0:
        T = np.array([1])
        return T
    if n == 1:
        T = np.array([1,0])
        return T
    else:
        Tn1 = Chebyshev(n-1)
        Tn2 = Chebyshev(n-2)
        Tn = np.polysub(np.polymul(np.array([2,0]),Tn1),Tn2)
    return Tn

# Polinomios de Legendre
def Legendre(n):
    if n == 0:
        L = np.array([1])
        return L
    if n == 1:
        L = np.array([1,0])
        return L
    else:
        m = n-1
        P1 = np.array([(2*m+1)/(m+1),0])
        P2 = np.array([m/(m+1)])
        Ln1 = Legendre(n-1)
        Ln2 = Legendre(n-2)
        return np.polysub(np.polymul(P1,Ln1),np.polymul(P2,Ln2))

def cv(x,a,b,opcion):
    """
    Opción 1: [a,b]---->[-1,1]
    Opción 2: [-1,1]---->[a,b]
    """
    if opcion == 1:
        y = 2/(b-a)*(x-a)-1
    if opcion == 2:
        y = (b-a)*(x+1)/2+a
    return y

def dif_divididas(x,y):
    n=len(x)-1
    A = np.zeros((n+1,n+1))
    for i in range(len(x)):
        A[i,0] = y[i]
    for j in range(1,n+1):
        for i in range(j,n+1):
            A[i,j] = (A[i][j-1] - A[i-1][j-1]) / (x[i]-x[i-j])
    return A

def PolNewton(x,y):
    n=len(x)-1
    DD = np.diag(dif_divididas(x,y))
    monom=np.array([1])
    pol=np.array([0])
    for i in range(n+1):
        pol=np.polyadd(pol,DD[i]*monom)
        monom=np.polymul(monom,[1, -x[i]])
    return pol


##########################
# EJERCICIO 1
##########################

def f1(x):
    return np.exp(-2*x)*np.cos(3*x)

# Apartado a

L0 = Legendre(0)
L0
a0 = sci.quad(lambda x: f1(x)*np.polyval(L0,x),-1,1)[0]/sci.quad(lambda x: np.polyval(L0,x)**2,-1,1)[0]
print(a0)

def AproxL(f,n):
    Sol=np.array([0])
    for i in range(n+1):
        Li = Legendre(i)
        num = sci.quad(lambda x: f(x)*np.polyval(Li,x),-1,1)[0]
        den = sci.quad(lambda x: np.polyval(Li,x)**2,-1,1)[0]
        coef = num/den
        Sol=np.polyadd(Sol,coef*Li)
    return Sol

aL4 = AproxL(f1,4)

def w(x):
    return 1/np.sqrt(1-x**2)

def AproxC(f,n):
    Sol=np.array([0])
    for i in range(n+1):
        Ti = Chebyshev(i)
        num = sci.quad(lambda x: w(x)*f(x)*np.polyval(Ti,x),-1,1)[0]
        den = sci.quad(lambda x: w(x)*np.polyval(Ti,x)**2,-1,1)[0]
        coef = num/den
        Sol=np.polyadd(Sol,coef*Ti)
    return Sol

aCh4 = AproxC(f1,4)

# Apartado b

x1 = np.linspace(-1,1,100)

plt.plot(x1,f1(x1),x1,np.polyval(aL4,x1),x1,np.polyval(aCh4,x1))
plt.legend(["Función", "Aprox. Legendre", "Aprox. Chebyshev"],loc='best')
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráficas ejercicio 1")

# Apartado c

error_L = np.sqrt(sci.quad(lambda x: (f1(x)-np.polyval(aL4,x))**2,-1,1)[0])
print('Error Legendre:',error_L)
error_C = np.sqrt(sci.quad(lambda x: w(x)*(f1(x)-np.polyval(aCh4,x))**2,-1,1)[0])
print('Error Chebyshev:',error_C)


##########################
# EJERCICIO 2
##########################

def f2(x):
    return np.exp(x)*np.sin(3*x)

# Apartado a

raicesCh = np.sort(np.roots(Chebyshev(7)))
nodosCh = cv(raicesCh,3,6,2)

PolNewton_6_A = PolNewton(nodosCh, f2(nodosCh))
print(PolNewton_6_A)

# Apartado b

nodos = np.array([3.1,3.5,4,4.8,5.3,5.7,5.9])

PolNewton_6_B = PolNewton(nodos, f2(nodos))
print(PolNewton_6_B)

# Apartado c

f2cv=lambda x: f2(cv(x,3,6,2))

aL6cv=AproxL(f2cv,6)

al6 = lambda x: np.polyval(aL6cv,cv(x,3,6,1))

# Apartado d

x2 = np.linspace(3,6,100)

plt.plot(x2,f2(x2),'b',nodosCh,f2(nodosCh),'om',x2,np.polyval(PolNewton_6_A,x2),'m',nodos,f2(nodos),'oy',x2,np.polyval(PolNewton_6_B,x2),'y',x2,al6(x2),'g')
plt.legend(["Función","Nodos Chebyshev","Pol. Lagrange-Chebyshev","Nodos Newton","Pol. Newton","Aprox. Legendre"],loc="best")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráficas ejercicio 2")
