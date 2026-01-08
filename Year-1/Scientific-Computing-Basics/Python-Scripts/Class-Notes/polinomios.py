# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:37:01 2020

@author: USUARIO
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as npp

# Para trabajar con polinomios hay varias opciones. Veamos dos de ellas:
   
# Definimos P(x)=3x^2-2x+1

def polinomio(x):
    return 3*x**2-2*x+1

# Definimos P(x)=3x^2-2x+1 y Q(x)=2x+1

# En potencias crecientes (P(x)=1-2x+3x^2)

P=npp.Polynomial([1,-2,3])
Q=npp.Polynomial([1,2])

npp.Polynomial(npp.polyadd(P,Q))
npp.Polynomial(npp.polysub(P,Q))
npp.Polynomial(npp.polymul(P,Q))
npp.Polynomial(npp.polydiv(P,Q))

P.degree()
P.roots()
Q.roots()
P.deriv(m=1)

# Una ventaja de este enfoque:
# Sabemos que un polinomio de grado n tiene n raíces y que si sabemos
# sus raíces podemos obtener el polinomio como (x-x0)(x-x1)...(x-xn)

raices = np.array([0,1])
npp.polyfromroots(raices) 
# El resultado es array([ 0., -1.,  1.]), es decir, los coeficientes del
# polinomio en potencias crecientes.

#Gráficas

P(0)
P(1)

x1=np.linspace(-10,10,100)
P(x1)
plt.plot(x1,P(x1),x1,Q(x1))
plt.title("Gráfica de polinomios")
plt.xlabel("X")
plt.ylabel("Y")

# Definimos P(x)=3x^2-2x+1 y Q(x)=2x+1

# En potencias decrecientes

P1=np.array([3,-2,1])
Q1=np.array([2,1])
np.polyadd(P1,Q1)
np.polysub(P1,Q1)
np.polymul(P1,Q1)
np.polydiv(P1,Q1)

np.roots(P1)
np.roots(Q1)


np.polyval(P1,0)
np.polyval(P1,x1)

#Gráficas

x1=np.linspace(-10,10,100)
plt.plot(x1,np.polyval(P1,x1),x1,np.polyval(Q1,x1))
plt.title("Gráfica de polinomios")
plt.xlabel("X")
plt.ylabel("Y")

# En resumen, podemos utilizar cualquiera de estos dos enfoques, pero
# hay que tener en cuenta cómo debemos indicar los coeficientes y cómo
# aparecen los resultado (por ejemplo, con npp.polyfromroots)