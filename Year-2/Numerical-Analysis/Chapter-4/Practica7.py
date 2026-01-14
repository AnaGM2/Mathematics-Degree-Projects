# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 12:08:24 2022

@author: gilpe
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci


##########################
# EJERCICIO 1
##########################

def df(f,x0,h,puntos):
    if puntos == 3:
        return 1/(2*h)*(f(x0+h)-f(x0-h))
    if puntos == 5:
        return 1/(12*h)*(f(x0-2*h)-8*f(x0-h)+8*f(x0+h)-f(x0+2*h))
    
    
##########################
# EJERCICIO 2
##########################

def trapecio(f,a,b):
    h = b-a
    return h/2*(f(a)+f(b))

def Simpson(f,a,b):
    h = (b-a)/2
    return h/3*(f(a)+4*f(a+h)+f(b))

def Simpson38(f,a,b):
    h = (b-a)/3
    return 3*h/8*(f(a)+3*f(a+h)+3*f(a+2*h)+f(b))

# Aproximamos la integral dada:

def f2(x):
    return x*np.sin(x)

print("Aproximación por regla del trapecio: ",trapecio(f2,0,np.pi/4))
print("Aproximación por regla de Simpson: ",Simpson(f2,0,np.pi/4))
print("Aproximación por regla de Simpson 3/8: ",Simpson38(f2,0,np.pi/4))


##########################
# EJERCICIO 3
##########################

# Apartado a

def f3(x):
    return np.sin(2*x)+x

TrapS = trapecio(f3,1,3)
print("Aproximación por regla del trapecio: ",TrapS)

def trapecio_compuesta(f,a,b,n):    # n subintervalos, n+1 puntos
    xi = np.linspace(a,b,n+1)
    h = (b-a)/n
    return h/2*(2*sum(f(xi))-f(a)-f(b))

TrapC = trapecio_compuesta(f3,1,3,4)
print("Aproximación por regla del trapecio compuesta: ",TrapC)

SimpS = Simpson(f3,1,3)
print("Aproximación por regla de Simpson: ",SimpS)

def simpson_compuesta(f,a,b,n):     # n subintervalos, n+1 puntos
    if n % 2 == 0:
        x = np.linspace(a,b,n+1)
        h = (b-a)/n
        suma = 0
        for i in range(1,int(n/2)+1):
            suma += h/3*(f(x[2*i-2]) + 4*f(x[2*i-1]) + f(x[2*i]))
        return suma
    else:
        print('El número de subintervalos n debe ser par.')

SimpC = simpson_compuesta(f3,1,3,4)
print("Aproximación por regla de Simpson compuesta: ",SimpC)

# Apartado b

VExacto = sci.quad(lambda x: f3(x),1,3)[0]

ETrapS = abs(VExacto-TrapS)
print("Error por regla del trapecio: ",ETrapS)

ETrapC = abs(VExacto-TrapC)
print("Error por regla del trapecio compuesta: ",ETrapC)

ESimpS = abs(VExacto-SimpS)
print("Error por regla de Simpson: ",ESimpS)

ESimpC = abs(VExacto-SimpC)
print("Error por regla de Simpson compuesta: ",ESimpC)

# Apartado c

x = np.linspace(1,3,100)
xTrapS = np.array([1,3])
xSimpS = np.linspace(1,3,3)
xComp = np.linspace(1,3,5)

plt.plot(x,f3(x),"b",xTrapS,f3(xTrapS),"g",xSimpS,f3(xSimpS),"r",xComp,f3(xComp),"m")
plt.legend(["Función","Trapecio","Simpson","Trapecio y Simpson compuestas"],loc="best")
plt.fill_between(x, 0, f3(x), facecolor='b', alpha = 0.7)
plt.fill_between(xTrapS, 0, f3(xTrapS), facecolor='g', alpha = 0.4)
plt.fill_between(xSimpS, 0, f3(xSimpS), facecolor='r', alpha = 0.3)
plt.fill_between(xComp, 0, f3(xComp), facecolor='m', alpha = 0.2)
plt.title("Gráfica áreas ejercicio 3")
plt.xlabel('X')
plt.ylabel('Y')


##########################
# EJERCICIO 4
##########################

# Apartado a

x4 = np.array([0,0.12,0.22,0.32,0.36,0.4,0.44,0.54,0.64,0.7])
y4 = np.array([0.2,1.309729,1.305241,1.743393,2.074903,2.456,2.842985,3.507297,3.181929,2.363])

plt.plot(x4,y4,"or")
plt.title("Datos ejercicio 4")
plt.xlabel('X')
plt.ylabel('Y')

# Apartado b

def trapecio_compuesta_puntos(x,fx):
    suma = 0
    for i in range(len(x)-1):
        suma += (x[i+1]-x[i])/2*(fx[i]+fx[i+1])
    return suma

TrapC4 = trapecio_compuesta_puntos(x4,y4)
print("Aproximación por regla del trapecio compuesta: ",TrapC4)
    
# Apartado c

def trapecio_puntos(x,fx):
    h = x[1]-x[0]
    return h/2*(fx[0]+fx[1])

def Simpson_puntos(x,fx):
    h = x[1]-x[0]
    return h/3*(fx[0]+4*fx[1]+fx[2])

def Simpson38_puntos(x,fx):
    h = x[1]-x[0]
    return 3*h/8*(fx[0]+3*fx[1]+3*fx[2]+fx[3])

int1 = trapecio_puntos(x4[:2],y4[:2])
int2 = Simpson_puntos(x4[1:4],y4[1:4])
int3 = Simpson38_puntos(x4[3:7],y4[3:7])
int4 = Simpson_puntos(x4[6:9],y4[6:9])
int5 = trapecio_puntos(x4[8:],y4[8:])

Aprox = int1+int2+int3+int4+int5
print("Aproximación por trapecio, Simpson y Simpson 3/8: ",Aprox)

# Apartado d

plt.plot(x4,y4)
plt.fill_between(x4, 0, y4, facecolor='b', alpha = 0.45)
plt.title("Gráfica área ejercicio 4")
plt.xlabel('X')
plt.ylabel('Y')


##########################
# EJERCICIO 5
##########################

T = np.array([0,6,12,18,24,30,36,42,48,54,60,66,72,78,84])
V = np.array([37.2,40.2,44.4,46.8,44.1,39.9,36.3,32.7,29.7,25.5,23.4,26.7,31.2,34.8,36.9])

def simpson_compuesta_puntos(x,fx):
    h = x[1]-x[0]
    sum = 0
    for i in range(1,int((len(x)-1)/2)+1):
        sum += h/3*(fx[2*i-2] + 4*fx[2*i-1] + fx[2*i])
    return sum

long = simpson_compuesta_puntos(T,V)
print("La pista tiene una longitud de", long, "m.")
