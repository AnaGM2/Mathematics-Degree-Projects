# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 12:11:17 2022

@author: gilpe
"""

import numpy as np
import numpy.polynomial.polynomial as npp

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

T2Ch=np.polynomial.chebyshev.Chebyshev([0,0,1])

nodCheby2=T2Ch.roots()
print(nodCheby2)

T2Ch=npp.polyfromroots(nodCheby2)[::-1]
print(T2Ch)

T5Ch=np.polynomial.chebyshev.Chebyshev([0,0,0,0,0,1])

nodCheby5=T5Ch.roots()
print(nodCheby5)

T5Ch=npp.polyfromroots(nodCheby5)[::-1]
print(T5Ch)

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
    
# No es mónico
print(Chebyshev(2))


##########################
# EJERCICIO 2
##########################

T2L=np.polynomial.legendre.Legendre([0,0,1])

nodL2=T2L.roots()
print(nodL2)

T2L=npp.polyfromroots(nodL2)[::-1]
print(T2L)

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

# No es mónico
print(Legendre(2))


##########################
# EJERCICIO 3
##########################

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

print(cv(0,2,4,2))


##########################   
# EJERCICIO 4
##########################

# Apartado a

p1 = Chebyshev(9)
raices1=np.roots(p1)
print(raices1)
PolNewton_8CH = PolNewton(raices1,np.exp(raices1))
print(PolNewton_8CH)  
    
# Apartado b

nodos = np.linspace(-1,1,9)

PolNewton_8CH_1 = PolNewton(nodos,np.exp(nodos)) 
print(PolNewton_8CH_1)
    
# Apartado c

x3=np.linspace(-1,1,100000)
    
Error_CH=np.max(np.abs(np.polyval(PolNewton_8CH,x3)-np.exp(x3)))
print(Error_CH) 
 
Error_Newton=np.max(np.abs(np.polyval(PolNewton_8CH_1,x3)-np.exp(x3)))
print(Error_Newton)
