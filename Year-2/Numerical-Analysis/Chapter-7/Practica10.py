# -*- coding: utf-8 -*-
"""
Created on Thu May  5 12:15:28 2022

@author: gilpe
"""

import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

def Jacobi(A,b,x0,norma,error,k):
    D = np.diag(np.diag(A))
    L = -np.tril(A-D)
    U = -np.triu(A-D)
    M = D
    N = L+U
    B = np.dot(la.inv(M),N)
    c = np.dot(la.inv(M),b)
    val = la.eig(B)[0]  # Da los valores propios y los vectores propios.
    ro = max(abs(val))
    if ro >= 1:
        print("El método no es convergente")
        return[x0,0,ro]
    i=1
    while True:
        if i>=k:
            print("El método no es convergente en", k, "iteraciones")
            return[x0,0,ro]
        x1=np.dot(B,x0)+c
        if la.norm(x1-x0,norma)<error:
            return[x1,i,ro]
        i=i+1
        x0=x1.copy()
        
def Gauss_seidel(A,b,x0,norma,error,k):
    D = np.diag(np.diag(A))
    L = -np.tril(A-D)
    U = -np.triu(A-D)
    M = D-L
    N = U
    B = np.dot(la.inv(M),N)
    c = np.dot(la.inv(M),b)
    val = la.eig(B)[0]  # Da los valores propios y los vectores propios.
    ro = max(abs(val))
    if ro >= 1:
        print("El método no es convergente")
        return[x0,0,ro]
    i=1
    while True:
        if i>=k:
            print("El método no es convergente en", k, "iteraciones")
            return[x0,0,ro]
        x1=np.dot(B,x0)+c
        if la.norm(x1-x0,norma)<error:
            return[x1,i,ro]
        i=i+1
        x0=x1.copy()


##########################
# EJERCICIO 1
##########################

def Sor(A,b,x0,norma,error,k,w):
    D = np.diag(np.diag(A))
    L = -np.tril(A-D)
    U = -np.triu(A-D)
    M = D-w*L
    N = (1-w)*D+w*U
    B = np.dot(la.inv(M),N)
    c = np.dot(la.inv(M),w*b)
    val = la.eig(B)[0]  # Da los valores propios y los vectores propios.
    ro = max(abs(val))
    if ro >= 1:
        print("El método no es convergente")
        return[x0,0,ro]
    i=1
    while True:
        if i>=k:
            print("El método no es convergente en", k, "iteraciones")
            return[x0,0,ro]
        x1=np.dot(B,x0)+c
        if la.norm(x1-x0,norma)<error:
            return[x1,i,ro]
        i=i+1
        x0=x1.copy()
        
# Ejemplo
        
A3a = np.array([[4,-1,0,-1,0,0],[-1,4,-1,0,-1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]],dtype=float)
b3a = np.array([0,5,0,6,-2,6],dtype=float)
x03a = np.zeros(6)
w=1.25

Sor1 = Sor(A3a,b3a,x03a,np.inf,10**(-6),100,w)

print("Solución:",Sor1[0])
print("Número de iteraciones:",Sor1[1])
print("Radio espectral:",Sor1[2])


##########################
# EJERCICIO 2
##########################

def Jacobi_iter(A,b,x0,norma,error,k):
    D = np.diag(np.diag(A))
    L = -np.tril(A-D)
    U = -np.triu(A-D)
    M = D
    N = L+U
    B = np.dot(la.inv(M),N)
    val = la.eig(B)[0]  
    ro = max(abs(val))
    if ro >= 1:
        print("El método no es convergente")
        return [x0,0,ro]
    numiter=1
    x1=x0.copy()
    while numiter<k:
        x = np.zeros([len(x1),1])
        for i in range(len(x1)):
            suma = 0
            for j in range(len(x1)):
                if j != i:
                    suma += A[i,j]*x1[j]
            x[i]=(b[i]-suma)/A[i,i]
        if la.norm(x-x1,norma)<error:
            aprox = x.copy()
            return [aprox,numiter,ro]
        numiter += 1
        x1=x.copy()
    print("El método no es convergente en", k, "iteraciones")
    return [x0,0,ro]
   
def Gauss_seidel_iter(A,b,x0,norma,error,k):
    D = np.diag(np.diag(A))
    L = -np.tril(A-D)
    U = -np.triu(A-D)
    M = D-L
    N = U
    B = np.dot(la.inv(M),N)
    val = la.eig(B)[0]  
    ro = max(abs(val))
    if ro >= 1:
        print("El método no es convergente")
        return [x0,0,ro]
    numiter=1
    x1=x0.copy()
    while numiter<k:
        x = np.zeros(len(x1))
        for i in range(len(x1)):
            suma = 0
            for j in range(i):
                suma += A[i,j]*x[j]
            for j in range(i+1,len(x1)):
                suma += A[i,j]*x1[j]
            x[i]=(b[i]-suma)/A[i,i]
        if la.norm(x-x1,norma)<error:
            aprox = x.copy()
            return [aprox,numiter,ro]
        numiter += 1
        x1=x.copy()
    print("El método no es convergente en", k, "iteraciones")
    return [x0,0,ro]
         
# Ejemplo

A3a = np.array([[4,-1,0,-1,0,0],[-1,4,-1,0,-1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]],dtype=float)
b3a = np.array([0,5,0,6,-2,6],dtype=float)
x03a = np.zeros(6)

J3a = Jacobi_iter(A3a,b3a,x03a,np.inf,10**(-6),100)
G3a = Gauss_seidel_iter(A3a,b3a,x03a,np.inf,10**(-6),100)

print("Jacobi:",J3a[0])
print("Número de iteraciones:",J3a[1])
print("Radio espectral:",J3a[2])

print("Gauss-Seidel:",G3a[0])
print("Número de iteraciones:",G3a[1])
print("Radio espectral:",G3a[2])

        
##########################
# EJERCICIO 3
##########################       

def Matriz(n):
    A = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            if i <= j:
                A[i,j] = (i+1)*(n-j)
            else:
                A[i,j] = A[j,i]
    return A

A4b=Matriz(9)
b4b=np.array(range(1,10))
x04 = np.zeros(9)
sol_exacta = la.solve(A4b,b4b)
print(sol_exacta)

[x4bJ,i4bJ,ro4bJ] = Jacobi(A4b,b4b,x04,np.inf,10**(-3),100)
print("Jacobi:",x4bJ)
print("Número de iteraciones:",i4bJ)
print("Radio espectral:",ro4bJ)

[x4bG,i4bG,ro4bG] = Gauss_seidel(A4b,b4b,x04,np.inf,10**(-3),100)
print("Gauss-Seidel:",x4bG)
print("Número de iteraciones:",i4bG)
print("Radio espectral:",ro4bG)

x1 = np.linspace(0.1,1.9,1000)
ite = []           
for w in x1:
    [x4bS,i4bS,ro4bS] = Sor(A4b,b4b,x04,np.inf,10**(-3),150,w)
    ite.append(i4bS)

k=np.argmin(ite)
w_opt=x1[k] 

x2 = np.linspace(0.1,1.9,19)
ite = []           
for w in x2:
    [x4bS,i4bS,ro4bS] = Sor(A4b,b4b,x04,np.inf,10**(-3),150,w)
    ite.append(i4bS) 

plt.plot(x2,ite,'*b',label='Iteraciones')
plt.legend(loc='best')
plt.xticks(x2)
plt.xlabel('Factor de relajación')
plt.ylabel('Iteraciones')
plt.title('Gráficas ejercicio 3')
         

##########################
# EJERCICIO 4
##########################

# Apartado a

# T1 = 1/4(100+50+T2+T3)
# T2 = 1/4(T1+50+0+T4)
# T3 = 1/4(50+T1+T4+T5)
# T4 = 1/4(T3+T2+50+T6)
# T5 = 1/4(100+T3+T6+50)
# T6 = 1/4(T5+T4+0+50)

# 4T1 -T2 -T3             = 150
# -T1+4T2     -T4         = 50
# -T1    +4T3 -T4 -T5     = 50
#     -T2 -T3+4T4     -T6 = 50
#         -T3    +4T5 -T6 = 150
#             -T4 -T5+4T6 = 50

A = np.array([[4,-1,-1,0,0,0],[-1,4,0,-1,0,0],[-1,0,4,-1,-1,0],[0,-1,-1,4,0,-1],[0,0,-1,0,4,-1],[0,0,0,-1,-1,4]],dtype=float)
b = np.array([150,50,50,50,150,50],dtype=float)

sol_exacta = np.linalg.solve(A,b)
print('Solución exacta: ',sol_exacta)

# Apartado b

T0 = 50*np.ones(6)
Jac4 = Jacobi(A,b,T0,np.inf,0.01,100)
errorJac = la.norm(sol_exacta-Jac4[0],np.inf)

print('Solución Jacobi: ', Jac4[0])
print("Número de iteraciones:",Jac4[1])
print("Radio espectral:",Jac4[2])
print('Máxima variación: ', errorJac)

# Apartado c

GS4 = Gauss_seidel(A,b,T0,np.inf,0.01, 100)
errorGS = la.norm(sol_exacta-GS4[0],np.inf)

print("Solución Gauss-Seidel:",GS4[0])
print("Número de iteraciones:",GS4[1])
print("Radio espectral:",GS4[2])
print('Máxima variación: ', errorGS)

# Apartado d

x4 = np.linspace(0.1,1.9,1000)
ite4 = []           
for w in x4:
    [x4S,i4S,ro4S] = Sor(A,b,T0,np.inf,0.01,100,w)
    ite4.append(i4S)

k=np.argmin(ite4)
w_opt=x4[k] 

Sor4 = Sor(A,b,T0,np.inf,0.01,100,w_opt)
errorSor = la.norm(sol_exacta-Sor4[0],np.inf)

print("Solución SOR:",Sor4[0])
print("Número de iteraciones:",Sor4[1])
print("Radio espectral:",Sor4[2])
print('Máxima variación: ', errorSor)