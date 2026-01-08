# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 08:37:46 2020

@author: gilpe
"""


import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as npp



#EJERCICIO 1.2

v = (False,True,True,False,False)

v.count(False)
#False aparece 3 veces.

#No se puede sustituir el primer elemento porque las tuplas son inmutables,
#es decir, no se pueden añadir ni eliminar elementos.

v.index(True)
#True aparece por primera vez en la posición 1.

#Creamos las matrices con la función randint del módulo random de numpy.
A = np.random.randint(0,70,(2,4))
B = np.random.randint(0,70,(2,4))

C = np.concatenate((A,B),0)
#Para pegarlas como filas debemos usar un 0 en el concatenate.

#Para obtener la traspuesta usamos:
C.T

#Para obtener la diagonal principal usamos diag.
np.diag(C.T)



#EJERCICIO 2.1

#Creamos un vector con 100 valores entre 0 y 5pi.
x = np.linspace(0,5*np.pi,100)

#Establecemos cada una de las funciones.
y1 = np.cos(x)
y2 = np.cos(x/2)
y3 = np.cos(x/3)

#Para cambiar el tamaño del gráfico usamos:
plt.figure(figsize=(10,8))

#Con la libreria matplotlib hacemos la gráfica.
plt.plot(x,y1,':k',x,y2,'--g',x,y3,'*c')
#Lo que aparece entre comillas establece el color y el trazo.

#Para añadir una recta y cambiar su color usamos:
plt.axhline(0,c='r')

#Establecemos los límites pedidos del eje Y.
plt.ylim(-2,2)

#Añadimos un título.
plt.title('Gráficas')

#Añadimos etiquetas en los ejes.
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

#Añadimos una leyenda.
plt.legend(('cos(x)','cos(x/2)','cos(x/3)'), loc='best')



#EJERCICIO 3.1

#Construimos el primer polinomio en potencias crecientes y obtenemos sus raíces.
P = npp.Polynomial([3,-1,-3,1])
P.roots()

#Construimos el segundo polinomio a partir de sus raíces, que son:
raíces = np.array([1,-1])
Q = npp.Polynomial(npp.polyfromroots(raíces))

#Veamos si P(x) es divisible por Q(x).
#Creamos un array con estos polinomios en potencias decrecientes y dividimos.
P1 = np.array([1,-3,-1,3])
Q1 = np.array([1,0,-1])
np.polydiv(P1,Q1)
#Sí es divisible.

#Calculamos R(x).
R = np.polysub(np.polymul(P,Q),P**2)
#R(x) = -x^6+7x^5-10x^4-14x^3+23x^2+7x-12

#Calculamos la derivada.
R = npp.Polynomial([-12,7,23,-14,-10,7,-1])
R.deriv(m=1)
# La derivada es -5x^5+35x^4-40x^3-42x^2+46x+7

#Hacemos la representación gráfica.
x = np.linspace(-10,10,100)
plt.plot(x,P(x),'k',np.roots(P1),P(np.roots(P1)),'or')



#EJERCICIO 4.2

def sucesión(a,epsilon):
    #Establecemos la condición que se debe cumplir para que se pueda operar.
    if a>0 and a!=1 and epsilon>0:
        x = 1 #Valor inicial de x.
        #Usamos un while que calculará e imprimirá el siguiente término de la sucesión
        #mientras la diferencia entre los términos y la raíz cúbica de a sea mayor o igual que epsilon.
        while abs(x-np.cbrt(a))>=epsilon:
            x = (1/3)*(2*x+a/x**2)
            print(x)
    else:
        print('El número a debe ser un real positivo distinto de 1 y epsilon debe ser positivo.')

#Damos valores y vemos los límites.
sucesión(8,0.000000000000001)   #Límite=2    
sucesión(27,0.00000000000001)   #Límite=3
