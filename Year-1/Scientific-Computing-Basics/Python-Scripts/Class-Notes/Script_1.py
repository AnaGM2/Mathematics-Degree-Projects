# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 13:48:03 2020

@author: julio
"""

#############################################
# PROGRAMAS DE CÁLCULO CIENTÍFICO Y PROCESAMIENTO DE TEXTOS
#############################################

#############################################
# Tipos de objetos básicos
#############################################

3
type(3) # Entero
3.5
type(3.5) # Coma flotante (real) - Punto decimal
3,5
type((3,5)) # Tupla - Entre paréntesis
.3
[3,5]
type([3,5]) # Lista - Entre corchetes
1+2j
type(1+2j) # Complejo - j unidad imaginaria
"hola"# Cadena de caracteres
'hola'
type('hola')


#############################################
# Python como una calculadora - Operaciones con valores numéricos
#############################################

# Operaciones básicas:

3+2.5
3-2.5
3*2.5
3/2.5
3**2.5
3**(-1)

# Uso de paréntesis:

1/(3+2.5)
5+8/7-2
(5+8)/(7-2)

# Otras operaciones:

5//2 # Cociente de una división
5%2 # Resto de una división
divmod(5,2) # Cociente y resto de una división
round(4.5321,1) # Redondeos
round(4.5321,2)
round(4.5321,-1)
round(453.21,-1)
round(453.21,-2)
abs(-3) # Valor absoluto
max(4,5,-2,8,3.5,-10) # Máximo
min(4,5,-2,8,3.5,-10) # Mínimo

# Raíces:

sqrt(4)
4**(1/2)
4**(1/3)

# EN LOS ORDENADORES DE LA UA NO ESTÁ INSTALADO
# NUMPY, HAY QUE INSTALARLO CADA VEZ QUE QUIERAS
# USARLO. Para ello:
# anaconda prompt
# pip install numpy

import numpy as np

np.sqrt(4)

import math

math.sqrt(4)

# Exponenciales y logaritmos:

np.exp(1)
np.log(100)
np.log10(100)

# Funciones trigonométricas:

np.sin(np.pi)
np.cos(np.pi)
np.tan(np.pi)

# Definición de objetos:

x=3
y=3.5
z=x*y
x=2
z
z=3,5
a=[3,5]
b="hola"

buenos dias=4
5x=2
x5=2

x=2*x

# Uso de los objetos:

a=2
b=3

2*a-4*b



