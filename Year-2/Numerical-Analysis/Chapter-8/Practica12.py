# -*- coding: utf-8 -*-
"""
Created on Thu May 19 12:16:26 2022

@author: gilpe
"""

import numpy as np
import matplotlib.pyplot as plt

def biseccion(f,a,b,tol,maxiter):
    if f(a)*f(b)>0:
        print('El intervalo [a,b] no es adecuado')
    i=0
    while(i<maxiter) and abs(b-a)>=tol:
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

def dy_5pts(f,x0,h):
    dy = (f(x0-2*h)-8*f(x0-h)+8*f(x0+h)-f(x0+2*h))/(12*h)
    return dy


##########################
# EJERCICIO 1
##########################

def secante(f,a,b,maxiter,tol):
    x0=biseccion(f,a,b,0.01,1)[0] 
    x1 = x0-(f(x0)/dy_5pts(f,x0,0.1))
    x=[x0,x1]
    for i in range(maxiter):
        new = x[i+1] - ((x[i]-x[i+1])*f(x[i+1]))/(f(x[i])-f(x[i+1]))
        x.append(new)
        if np.abs(x[-1]-x[-2])<tol:
            return x[-1], i+1
    return x[-1], i+1
    
def regula_falsi(f,a,b,maxiter,tol):
    x0=biseccion(f,a,b,0.01,1)[0] 
    x1 = x0-(f(x0)/dy_5pts(f,x0,0.1))
    x=[x0,x1]
    for i in range(maxiter):
        new = x[i+1] - ((x[i]-x[i+1])*f(x[i+1]))/(f(x[i])-f(x[i+1]))
        x.append(new)
        if np.abs(x[-1]-x[-2])<tol:
            return x[-1], i+1
        z = x.copy()
        if f(x[-2])*f(x[-1])<0:
            z[-1]=x[-1]
            z[-2]=x[-2]
        else:
            z[-1]=x[-1]
            z[-2]=x[-3]
        x=z.copy()
    return x[-1],i+1
                  
def f1(x):
    return np.exp(-x/10)*np.cos(x) 

x = np.linspace(0,15,150)
plt.plot(x,f1(x),label='Función')
plt.plot(x,0*x,label='Eje X')
plt.legend(loc='best')
plt.xlabel('Abscisas')
plt.ylabel('Ordenadas')
plt.title('Gráficas ejercicio 1')
    
print(secante(f1,1,3,50,10**(-6)))
print(secante(f1,4,6,50,10**(-6)))
print(secante(f1,7,9,50,10**(-6)))
print(secante(f1,9,11,50,10**(-6)))
print(secante(f1,14,15,50,10**(-6)))

print(regula_falsi(f1,1,3,50,10**(-6)))
print(regula_falsi(f1,4,6,50,10**(-6)))
print(regula_falsi(f1,7,9,50,10**(-6)))
print(regula_falsi(f1,9,11,50,10**(-6)))
print(regula_falsi(f1,14,15,50,10**(-6)))
    

##########################
# EJERCICIO 2
##########################

def Jac(F,x0,h):
    n = len(x0)
    J = np.zeros([n,n])
    for j in range(n):
        e=np.zeros(n)
        e[j]=1
        J[:,j]=(F(x0-2*h*e)-8*F(x0-h*e)+8*F(x0+h*e)-F(x0+2*h*e))/(12*h)
    return J 
    

##########################
# EJERCICIO 3
##########################

# J(x^k)(x^(k+1)-x^k) = -F(x^k)
# A = J(x^k), x = x^(k+1)-x^k, b = -F(x^k)
# Ax = b

def NewtonSist(F,x0,tol,norma,maxiter):
    J = Jac(F,x0,0.01)
    x1 = x0-np.linalg.solve(J,F(x0))
    i=1
    Seq=[x0,x1]
    while (i<maxiter) and np.linalg.norm(x1-x0,norma)>tol:
        i=i+1
        x0=x1
        J = Jac(F,x0,0.01)
        x1 = x0-np.linalg.solve(J,F(x0))
        Seq.append(x1)
    return x1, i
    
# Apartado a
    
def F3a(x):
    f1 = np.sin(x[0])+(x[1]**2)+np.log(x[2])-7
    f2 = 3*x[0]+2**x[1]-1/(x[2]**3)+1
    f3 = x[0]+x[1]+x[2]-5
    return np.array([f1,f2,f3])
    
x3a0 = np.array([2,3,4])
print('Solución: ',NewtonSist(F3a,x3a0,10**(-8),np.inf,50)[0])
print('Iteraciones: ',NewtonSist(F3a,x3a0,10**(-8),np.inf,50)[1])

# Apartado b

def F3b(x):
    f1 = -np.exp(x[0]**2)+8*x[0]*np.sin(x[1])
    f2 = x[0]+x[1]-1
    return np.array([f1,f2])

x3b10 = np.array([0,1])
print('Solución: ',NewtonSist(F3b,x3b10,10**(-8),np.inf,50)[0])
print('Iteraciones: ',NewtonSist(F3b,x3b10,10**(-8),np.inf,50)[1])

x3b20 = np.array([2,2])
print('Solución: ',NewtonSist(F3b,x3b20,10**(-8),np.inf,50)[0])
print('Iteraciones: ',NewtonSist(F3b,x3b20,10**(-8),np.inf,50)[1])
