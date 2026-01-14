# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:13:41 2022

@author: gilpe
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci


np.random.seed(0)   # Fijamos semilla


##########################
# EJERCICIO 1
##########################

np.vander([2,3,4])

# x -----> (b-a)x+a
x1 = np.sort(9*np.random.rand(6)-5)
y1 = 8*np.random.rand(6)-2

def PolLagrange(x,y):
    A = np.vander(x)
    return np.dot(np.linalg.inv(A),y)

# En potencias decrecientes
P1 = np.polyfit(x1,y1,len(x1)-1)    
P_1 = PolLagrange(x1,y1)


##########################
# EJERCICIO 2
##########################

def f2(x):
    return np.exp(x)*np.cos(3*x)

x2 = np.array([-1.5,-1,-0.75,0,0.5,1,1.5,2,2.5,2.7])

P2 = np.polyfit(x2,f2(x2),len(x2)-1)
P_2 = PolLagrange(x2,f2(x2))

X2 = np.linspace(-2,3,100)
plt.plot(x2,f2(x2),'*g',label="Nodos")
plt.plot(X2,f2(X2),'r',label="$exp(x)cos(3x)$")
plt.plot(X2,np.polyval(P_2,X2),label="Pol. interpolador")
plt.legend(loc="best")
plt.title("Gráficas ejercicio 2")
plt.xlabel("X")
plt.ylabel("Y")


##########################
# EJERCICIO 3
##########################

def f3(x):
    return np.cos(x)**5

def E(x):
    return np.abs(f3(x)-np.polyval(P3,x))

X3 = np.linspace(0,2,100)

for n in [6,10,12]:
    x3 = np.linspace(0,2,n+1)
    P3 = PolLagrange(x3,f3(x3))

    plt.plot(X3,E(X3),label="n="+str(n))
plt.legend(loc="best")
plt.title("Gráficas ejercicio 3")
plt.xlabel("X")
plt.ylabel("Y")


##########################
# EJERCICIO 4
##########################

def erf(x):
    return (2/np.sqrt(np.pi))*(sci.quad(lambda y:np.exp(-y**2),0,x))[0]

# Apartado a

x4 = np.array([0.2*i for i in range(6)])
y4 = np.round(np.array([erf(x4[i]) for i in range(6)]),4)

tabla = np.array([x4,y4])

# Apartado b

P1=np.polyfit(x4[1:3],y4[1:3],1)
VP1=np.polyval(P1,1./3)
print(VP1)
P2A=np.polyfit(x4[0:3],y4[0:3],2)
VP2A=np.polyval(P2A,1./3)
print(VP2A)
P2B=np.polyfit(x4[1:4],y4[1:4],2)
VP2B=np.polyval(P2B,1./3)
print(VP2B)
VExact=erf(1./3)
print(VExact)

print(abs(VExact-VP2A))
print(abs(VExact-VP2B))


##########################
# EJERCICIO 5
##########################

def dif_divididas(x,y):
    n=len(x)-1
    A = np.zeros((n+1,n+1))
    for i in range(len(x)):
        A[i,0] = y[i]
    for j in range(1,n+1):
        for i in range(j,n+1):
            A[i,j] = (A[i][j-1] - A[i-1][j-1]) / (x[i]-x[i-j])
    return A

# Datos ejercicio 2.7
x_5=np.array([0,1,2,4])
y_5=np.array([1,5,10,24])

dif_divididas(x_5,y_5)
