# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 12:48:38 2022

@author: gilpe
"""

import numpy as np
import matplotlib.pyplot as plt

def PolLagrange(x,y):
    A = np.vander(x)
    return np.dot(np.linalg.inv(A),y)

def dif_divididas(x,y):
    n=len(x)-1
    A = np.zeros((n+1,n+1))
    for i in range(len(x)):
        A[i,0] = y[i]
    for j in range(1,n+1):
        for i in range(j,n+1):
            A[i,j] = (A[i][j-1] - A[i-1][j-1]) / (x[i]-x[i-j])
    return A


##########################
# EJERCICIO 1
##########################

def PolNewton(x,y):
    n=len(x)-1
    DD = np.diag(dif_divididas(x,y))
    monom=np.array([1])
    pol=np.array([0])
    for i in range(n+1):
        pol=np.polyadd(pol,DD[i]*monom)
        monom=np.polymul(monom,np.array([1, -x[i]]))
    return pol

# Datos ejercicio 2.7
x=np.array([0,1,2,4])
y=np.array([1,5,10,24])

print(np.polyfit(x,y,3))
print(PolNewton(x,y))


##########################
# EJERCICIO 2
##########################

def fRunge(x):
    return 1/(1+x**2)

# Apartado a

x2 = np.linspace(-5,5,5)

dif_divididas(x2,fRunge(x2))
PRungeLagr = PolLagrange(x2,fRunge(x2))
print(PRungeLagr)

print(PolNewton(x2,fRunge(x2)))

# Apartado b

t = [4,8,12,16]
a = -5
b = 5
x2_B=[np.linspace(a,b,n+1) for n in t]
y2_B=[fRunge(x2_B[i]) for i in range(len(t))]
P=[np.polyfit(x2_B[i],y2_B[i],len(x2_B[i])-1) for i in range(len(t))]
X = np.linspace(a,b,100)

plt.plot(X,fRunge(X),label='Función Runge')
for i in range(len(t)):
    plt.plot(X,np.polyval(P[i],X), label='n='+str(t[i]))
    plt.legend(loc="best")
    plt.title("Gráficas Ejercicio 2")
    plt.xlabel("X")
    plt.ylabel("Y")
    
# Apartado c

def funNodos_Cheby(n):
    x=[]
    for i in range(1,n+2):
        x.append(5*np.cos((2*(n-(i-1))+1)*np.pi/(2*n+2)))
    return x

nodCheby=np.array(funNodos_Cheby(8))

print(nodCheby)  

xR = np.linspace(-5,5,100)
x8 = np.linspace(-5,5,9)
PRunge_8 = PolNewton(x8,fRunge(x8))

PRunge_8_Ch = PolNewton(nodCheby,fRunge(nodCheby))
plt.plot(xR,fRunge(xR),xR,np.polyval(PRunge_8_Ch,xR),xR,np.polyval(PRunge_8,xR))
plt.legend(["Función", "Pol. inter Ch.", "Pol. Newton"])
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Nodos Chebyshev")


##########################
# EJERCICIO 3
##########################

def DifDivid_Hermite(x,y,dy):
    n=len(x)
    A=np.zeros([2*n,2*n])
    z=np.reshape([[x[i],x[i]] for i in range(n)],(1,2*n))
    yz=np.reshape([[y[i],y[i]] for i in range(n)],(1,2*n))
    dyz=np.reshape([[0,dy[i]] for i in range(n)],(1,2*n))
    for j in range(2*n):
        for i in range(j,2*n):
            if j==0:
                A[i,j] = yz[0,i]
            elif j==1 and i%2!=0:
                A[i,j] = dyz[0,i]
            else:
                A[i,j]=(A[i,j-1]-A[i-1,j-1])/(z[0,i]-z[0,i-j])
    return A

# Datos ejercicio 2.10
x=[0,np.pi/4]
y=[0,1]
dy=[1,2]
DifDivid_Hermite(x,y,dy)