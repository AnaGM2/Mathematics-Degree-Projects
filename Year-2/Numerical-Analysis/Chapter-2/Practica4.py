# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:55:57 2022

@author: gilpe
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

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

def PolNewton(x,y):
    n=len(x)-1
    DD = np.diag(dif_divididas(x,y))
    monom=np.array([1])
    pol=np.array([0])
    for i in range(n+1):
        pol=np.polyadd(pol,DD[i]*monom)
        monom=np.polymul(monom,[1, -x[i]])
    return pol

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


##########################
# EJERCICIO 1
##########################

def PolHermite(x,y,dy):
    n=len(x)
    DD = np.diag(DifDivid_Hermite(x,y,dy))
    monom=np.array([1])
    pol=np.array([0])
    z=np.zeros(2*n)
    for i in range(2*n):
        z[i]=x[int(i/2)]
        pol=np.polyadd(pol, DD[i]*monom)
        monom=np.polymul(monom,np.array([1, -z[i]]))
    return pol

# Datos ejercicio 2.10
x=[0,np.pi/4]
y=[0,1]
dy=[1,2]
PolHermite(x,y,dy)


##########################
# EJERCICIO 2
##########################

def fun(x):
    return np.exp(-x)*np.sin(x**2)

def derfun(x):
    return -np.exp(-x)*np.sin(x**2) + 2*x*np.exp(-x)*np.cos(x**2)

x2=np.array([-2.8,-2.5,-1,-0.75,-0.2])
y2=fun(x2)
dy2=derfun(x2)

# Apartado a

PNewton = np.polyfit(x2,y2,4)
pN = PolNewton(x2,y2)
print(pN)

# Apartado b

pH = PolHermite(x2,y2,dy2)
print(pH)

# Apartado c

x3 = np.linspace(-3,0,100)

plt.plot(x3,fun(x3),x2,y2,'*r',x3,np.polyval(pN,x3),x3,np.polyval(pH,x3))
plt.legend(["Función", "Puntos", "Pol. Newton", "Pol. Hermite"],loc="best")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Ejercicio 2")

# Apartado d

xE = np.linspace(-3,0,10000)

E_Newton = abs(fun(xE)-np.polyval(pN,xE))
E_Max_Newton = max(E_Newton)

E_Hermite = abs(fun(xE)-np.polyval(pH,xE))
E_Max_Hermite = max(E_Hermite)


##########################
# EJERCICIO 3
##########################

# CS = CubicSpline(x,y,bc_type=__)
# bc_type='natural'
# bc_type=((1,f'(x0)),(1,f'(xn)))
# CS.c     coeficientes

x3=np.array([-3,-2,-1,0,1,2,3])
y3=np.arctan(x3)
dera=1/10
derb=1/10

# Apartado a

P6=PolNewton(x3,y3)
P6_1=np.polyfit(x3,y3,6)

# Apartado b

# Frontera fija
cs = CubicSpline(x3,y3,bc_type=((1,1/10),(1,1/10)))
# Mostrar valores
print(cs(-2.5))
# Ver los coeficientes
print(cs.c)

# Natural
csn = CubicSpline(x3,y3,bc_type='natural')
print(csn(-2.5))
print(csn.c)

# Apartado c

x = np.linspace(-3,3,100)

plt.plot(x,np.polyval(P6,x),x,cs(x),x,csn(x),x3,y3,'*')
plt.legend(["Pol. Newton", "Spline front. fija", "Spline natural","Puntos"],loc="best")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Ejercicio 3")

xE = np.linspace(-3,3,10000)

E_newton = max(abs(np.arctan(xE)-np.polyval(P6,xE)))
E_ff = max(abs(np.arctan(xE)-cs(xE)))
E_nat = max(abs(np.arctan(xE)-csn(xE)))


##########################
# EJERCICIO 4
##########################

# Apartado a

# Curva 1
x1 = np.array([1,2,5,6,7,8,10,13,17])
y1 = np.array([3,3.7,3.9,4.2,5.72,6.6,7.1,6.7,4.5])
pL1 = np.polyfit(x1,y1,8)

# Curva 2
x2 = np.array([17,20,23,24,25,27,27.7])
y2 = np.array([4.5,7,6.1,5.6,5.8,5,4.1])
pL2 = np.polyfit(x2,y2,6)

# Curva 3
x3 = np.array([27.7,28,29,30])
y3 = np.array([4.1,4.3,4.1,3])
pL3 = np.polyfit(x3,y3,3)

X1 = np.linspace(1,17,100)
X2 = np.linspace(17,27.7,100)
X3 = np.linspace(27.7,30,100)

plt.plot(X1,np.polyval(pL1,X1),X2,np.polyval(pL2,X2),X3,np.polyval(pL3,X3))
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Lagrange")

# Apartado b

cs1 = CubicSpline(x1,y1,bc_type=((1,1),(1,-0.67)))
cs2 = CubicSpline(x2,y2,bc_type=((1,3),(1,-4)))
cs3 = CubicSpline(x3,y3,bc_type=((1,0.33),(1,-1.5)))

plt.figure(figsize=(14,4))

plt.plot(X1,cs1(X1),X2,cs2(X2),X3,cs3(X3))
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Splines front. fija")
