# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 09:40:50 2020

@author: gilpe
"""

##################################
#PRÁCTICA 2
##################################


import numpy as np


#EJERCICIO 1
#Apartado (a)
u = np.arange(1,101,3)
#Apartado (b)
v = np.arange(-8,9)
#Apartado (c)
w = np.arange(0,30,2)
#Apartado (d)
u[7]                    #Da el elemento de la posición 7 de u
u[0]                    #Da el elemento de la posición 0 de u
v[3:12]                 #Da los elementos de la posición 3 a la 11 de v
w[np.arange(2,10,2)]    #Da los elementos de la posición 2 a la 9 de 2 en 2 de w


#EJERCICIO 2
t = np.arange(0,10)
#Apartado (a)
x = t*np.sin(t)
#Apartado (b)
y = (t-1)/(t+1)
#Apartado (c)
z = (np.sin(t**2))/t**2


#EJERCICIO 3
A = np.random.randint(-6,7,size=(10,8))
np.linalg.matrix_rank(A)
sum(np.diag(A))
A.transpose()


#EJERCICIO 4
B = A[0:8,:]
np.linalg.det(B)
np.linalg.inv(B)


#EJERCICIO 5
C = np.insert(A[:,0:7],7,A[:,0:7].sum(1),1)
#El primer elemento es la matriz a la que se le va a añadir una nueva columna
#El segundo elemento indica la posición en la que se va a añadir
#El tercer elemento es el vector que se va a añadir
#El cuarto elemento indica si se añade como fila (0) o como columna (1)
np.linalg.matrix_rank(C)
#El rango de C es menor que el de A porque la última columna de C es combinación lineal de las demás


#EJERCICIO 6
D = A[0:7,0:7]
D1 = np.diag(np.diag(D))
D2 = np.concatenate((np.zeros((2,8)),np.array([np.insert(A[1,7:8],\
  1,np.zeros(7)),np.insert(A[2,6:8],2,np.zeros(6)),np.insert(A[3,5:8],\
  3,np.zeros((5))),np.insert(A[4,4:8],4,np.zeros((4))),np.insert(A[5,3:8],\
  5,np.zeros((3))),np.insert(A[6,2:8],6,np.zeros((2))),np.insert(A[7,1:8],\
  7,np.zeros((1))),A[0,:]])),0)
D2 = np.tril(A)
D3 = np.concatenate((np.array([A[0,:],np.insert(A[1,1:8],0,0),np.insert(A[2,2:8],\
  0,[0,0]),np.insert(A[3,3:8],0,np.zeros((3))),np.insert(A[4,4:8],0,np.zeros((4))),\
  np.insert(A[5,5:8],0,np.zeros((5))),np.insert(A[6,6:8],0,np.zeros((6))),\
  np.insert(A[7,7:8],0,np.zeros((7)))]),np.zeros((2,8))),0)
D3 = np.triu(A,1)


#EJERCICIO 7
v = np.random.randint(-10,11,size=20)
np.array([x for x in v if x>=0])
np.array([x for x in v if x<0])


#EJERCICIO 8
k = np.arange(1,51)
sum(np.sin((2*np.pi*k)/50))


#EJERCICIO 9
A = np.array([[0,2,3],[1,-1,-3]])
B = np.array([[-1,3,7,4,0],[0,1,0,2,1],[-1,3,0,8,4],[0,-5,6,0,-3]])
A[1,2]
#Da el elemento que se encuentra en la segunda fila y tercera columna
A[:,1]
#Da la segunda columna
A[0,:]
#Da la primera fila
B[0,0]
#Da el elemento que se encuentra en la primera fila y primera columna
B[:,[0,2,4]]
#Da la primera, la tercera y la quinta columna
B[1:3,:]
#Da la segunda y la tercera fila
B[:,2:4]
#Da la tercera y la cuarta columna


#EJERCICIO 10
A = np.array([[1,-2,0],[-2,3,0],[0,2,-3]])
B = np.array([[7,-2,0],[5,-1,4],[1,-1,0]])
C = np.array([[1,-2,3],[9,0,6]])
#Apartado (a)
A+B
#Apartado (b)
np.dot(A,B)==np.dot(B,A)
np.dot(A,C)==np.dot(C,A)
np.dot(B,C)==np.dot(C,B)
#Apartado (c)
(A+B).T==A.T+B.T
#Apartado (d)
np.dot(A,B).T==np.dot(A.T,B.T)      #No
np.dot(A,B).T==np.dot(B.T,A.T)      #Sí
np.dot(A.T,B.T)==np.dot(B.T,A.T)    #No
#Apartado (e)
np.linalg.det(np.dot(A,B))==np.linalg.det(A)*np.linalg.det(B)   #No
#Apartado (f)
np.linalg.inv(A)
np.linalg.inv(B)
np.linalg.inv(C)


#EJERCICIO 11
np.ones([4,6])
#Hace una matriz de 4 filas y 6 columnas cuyos elementos son 1
np.zeros([5,2])
#Hace una matriz de 5 filas y 2 columnas cuyos elementos son 0
np.diag([1,-2,3,-4,5,-6,7,-8])
#Hace una matriz diagonal con esos números
np.eye(6)
#Hace una matriz identidad de dimensión 6