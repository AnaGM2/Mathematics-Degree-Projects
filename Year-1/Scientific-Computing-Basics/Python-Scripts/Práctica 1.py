# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:34:16 2020

@author: gilpe
"""

##################################
#PRÁCTICA 1
##################################


import cmath as cm
import numpy as np


#EJERCICIO 1
2+3+4+2
2+3*4+2
(2+3)*4+2
(2+3)*(4+2)
2*3+4*2
1/2*(2+3*4**2)


#EJERCICIO 2
2+3*6/2
(4/2)**5
(4/2)**(5+1)
(-3)**2
(4+6)/(2+3)
(12+15+20)/(4+3+5)
(3+1/4)-(2+1/6)
(1/2)/(1/4+1/3)
(5/3-1)*(7/2-2)
(3/4+1/2)/(5/3+1/6)
2/3/(5/(3/7+1)-3*(1/2-1/4))
4/9*(1/5/(2/9+5/8)**6-3*(3/5-2/15)**4)


#EJERCICIO 3
2/cm.sqrt(5)-cm.sqrt(3)*(4-cm.sqrt(7))
3*cm.sqrt(2)-5*cm.sqrt(8)+7*cm.sqrt(32)
cm.sqrt(8/27)+cm.sqrt(31/75)
cm.sqrt((2*cm.sqrt(7)+1)/(1-2*cm.sqrt(7)))
(cm.sqrt(27)-2*cm.sqrt(3)+5*cm.sqrt(18))/(15+cm.sqrt(3))
16**(1/3)
5**(7/8)
(2**(1/3)-5*17**(1/4))/(2*16**(1/5)-9*17**(1/3))


#EJERCICIO 4
numero-bajas = 6+2
#Incorrecta por el guion
numero_bajas} = 6+2
#Incorrecta por la llave
numero bajas = 6+2
#Incorrecta por el espacio
numero_bajas_= 6+2
#Correcta
8colores = 6*8
#Incorrecta por el 8
i = 1
#Correcta
A1234_5678 = i
#Correcta
A1234_5678 = A1234_5678*2
#Correcta
B-52 = 0
#Incorrecta por el guion
B_52 = 0
#Correcta


#EJERCICIO 5
#Apartado A
x = 5
x = 2*x
y = x**2
x = y/x
#Apartado B
x = 5
y = 3
x = x**y
y = y**x
z = (x-y)/(x+y)


#EJERCICIO 6
2**5/(2**5-1)
(1-(1/2**5))**(-1)
3*((np.sqrt(5)-1)/(np.sqrt(5)+1)**2)-1
np.pi*((np.pi)**(1/3)-1)**2
np.exp(3)
np.log(np.exp(3))
np.log10(10**5)
10**5
np.exp(np.pi*np.sqrt(163))
np.sin(np.pi/6)**2+np.cos(np.pi/6)**2


#EJERCICIO 7
np.roots([1,-5,6])
np.roots([1,-2,5])
np.roots([1,-6,10])
np.roots([2,-1/2,13/18])
np.roots([9,18/15,34/25])
np.roots([2/5,-1/3,1/15])


#EJERCICIO 8
np.log(5*10+16)-np.sqrt(10-3)
np.log(5*(-2)+16)-np.sqrt(-2-3)
np.log(5*(2/3)+16)-np.sqrt((2/3)-3)
np.log(5*(5/7)+16)-np.sqrt((5/7)-3)
np.log(5*np.sin(np.pi/2)+16)-np.sqrt(np.sin(np.pi/2)-3)
np.log(5*np.cos(np.pi/3)+16)-np.sqrt(np.cos(np.pi/3)-3)


#EJERCICIO 9
np.sqrt(np.log10(3*3+5*(-2))/np.log10(3**2-2*(-2)))
np.sqrt(np.log10(3*(-5)+5*3**(-5))/np.log10(-5)**2-2*3**(-5))
np.sqrt(np.log10(3*4/9+5*np.exp(4/9))/np.log10((4/9)**2-2*np.exp(4/9)))
np.sqrt(np.log10(3*np.sqrt(3)+5*np.log(np.sqrt(3)))/np.log10(np.sqrt(3)**2-2*np.log(np.sqrt(3))))
np.sqrt(np.log10(3*np.log(5)+5*np.exp(np.sqrt(np.log(5))))/np.log10(np.log(5)**2-2*np.exp(np.sqrt(np.log(5)))))
np.sqrt(np.log10(3*np.sin(np.pi/6)+5*np.cos(np.sin(np.pi/6))**3)/np.log10(np.sin(np.pi/6)**2-2*np.cos(np.sin(np.pi/6))**3))
