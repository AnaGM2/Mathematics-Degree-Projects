# -*- coding: utf-8 -*-
"""
Created on Thu May 12 12:17:55 2022

@author: gilpe
"""

import numpy as np
import matplotlib.pyplot as plt

def dy_5pts(f,x0,h):
    dy = (f(x0-2*h)-8*f(x0-h)+8*f(x0+h)-f(x0+2*h))/(12*h)
    return dy
    

##########################
# EJERCICIO 1
##########################

def biseccion(f,a,b,tol,maxiter):
    if f(a)*f(b)>0:
        print('El intervalo [a,b] no es adecuado')
    i=0
    while (i<maxiter) and abs(b-a)>=tol:
        p=(a+b)/2.0
        if f(p) == 0:
            return [p,i]
        else:
            if f(a)*f(p)>0:
                a=p
            else:
                b=p
        i=i+1
    return [p,i]

def f1(x):
    return np.exp(x)*np.sin(x)-x

Bis1 = biseccion(f1,6,8,10**(-8),100)
print('x = ', Bis1[0])
print('Iteraciones: ', Bis1[1])   


##########################
# EJERCICIO 2
##########################

def newton(f,a,b,maxiter,tol):
    x0=biseccion(f,a,b,0.001,4)[0]
    df = dy_5pts(f,x0,0.01)
    x1 = x0-(f(x0)/df)
    i=1
    while (i<maxiter) and abs(x1-x0)>tol:
        x0=x1
        df = dy_5pts(f,x0,0.01)
        x1 = x0-(f(x0)/df)
        i=i+1
    return x1,i

def f2(x):
    return np.exp(-x/10)*np.cos(x)

tol = 10**(-8)
x=np.linspace(0,15,150)
plt.plot(x,f2(x),label='Función')
plt.plot(x,0*x,label='Eje X')
plt.legend(loc='best')
plt.xlabel('Abscisas')
plt.ylabel('Ordenadas')
plt.title('Gráficas ejercicio 2')

solnewton1=newton(f2,0,2,50,tol)
print('x1 = ',solnewton1[0])
print('Iteraciones: ', solnewton1[1])
solnewton2=newton(f2,4,5,50,tol)
print('x2 = ',solnewton2[0])
print('Iteraciones: ', solnewton2[1])
solnewton3=newton(f2,5,8,50,tol)
print('x3 = ',solnewton3[0])
print('Iteraciones: ', solnewton3[1])
solnewton4=newton(f2,10.8,11,50,tol)
print('x4 = ',solnewton4[0])
print('Iteraciones: ', solnewton4[1])
solnewton5=newton(f2,14.1,14.4,50,tol)
print('x5 = ',solnewton5[0])
print('Iteraciones: ', solnewton5[1])


##########################
# EJERCICIO 3
##########################

def Newton(f,x0,tol,p,R):
    df = dy_5pts(f,x0,0.1)
    x1 = x0-(f(x0)/df)
    i=1
    while abs(x1-x0)>tol:
        i=i+1
        x0=x1
        df = dy_5pts(f,x0,0.1)
        x1 = x0-(f(x0)/df)
        e0=np.abs(x0-p)
        e1=np.abs(x1-p)
        A=e1/(e0**R)
    return [i,x1,x0,e1,A]

def f3(x):
    return x**3-3*x+2

# Apartado a

sol3a = Newton(f3,-2.4,10**(-5),-2,2)
print('Solución a): ', sol3a)

# Apartado b

sol3b = Newton(f3,1.2,10**(-5),1,1)
print('Solución b):', sol3b)

# Apartado c

print('Apartado a): A = ',sol3a[4])
print('Apartado b): A = ',sol3b[4])
