# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 12:49:11 2020

@author: gilpe
"""

##################################
#PRÁCTICA 6
##################################


import numpy as np
import numpy.polynomial.polynomial as npp
import matplotlib.pyplot as plt


#EJERCICIO 1

#Primer método: potencias crecientes

P = npp.Polynomial([1,-2,1])
Q = npp.Polynomial([1,1])

npp.Polynomial(npp.polyadd(P,Q))
npp.Polynomial(npp.polysub(P,Q))
npp.Polynomial(npp.polymul(P,Q))
npp.Polynomial(npp.polydiv(P,Q))

x = np.linspace(-10,10,100)
plt.plot(x,P(x),x,Q(x))

#Segundo método: potencias decrecientes

P = np.array([1,-2,1])
Q = np.array([1,1])

np.polyadd(P,Q)
np.polysub(P,Q)
np.polymul(P,Q)
np.polydiv(P,Q)

x = np.linspace(-10,10,100)
plt.plot(x,np.polyval(P,x),x,np.polyval(Q,x))


#EJERCICIO 2

P = npp.Polynomial([6,-1,-8,1,1])

P.deriv(1)
P.deriv(4)

x = np.linspace(-10,10,100)
r = P.roots()
plt.plot(x,P(x),r,P(r),'*r')
