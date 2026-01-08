# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:23:40 2020

@author: julio
"""

import numpy as np

(1,2,3)
[1,2,3]

# LISTAS

u = [1,2,3]
v = [0,1,2]

u+v
2*u

# ARRAYS

u = np.array([1,2,3])
v = np.array([0,1,2])

u+v
2*u

w = np.linspace(0,np.pi,100)

np.repeat(3,2)
np.repeat([1,2], 2)
np.repeat([1,2], [2, 3])

w = np.linspace(0,np.pi,100)

w[0]
w[1]
w[0],w[1]

w[0:3]
w[15:21]
w[:3]
w[98:]
w[:]
w[[0,99]]
w[-1]
w[2:5:2]
w[::-1]

np.arange(2,12,2)
np.arange(1,10)

np.random.rand(3)

np.random.randint(2,5,3)
np.random.randint(2,5,30)

np.zeros(5)
np.ones(5)

np.sin(w)
len(np.sin(w))
np.sum(w)

# MATRICES

A = np.array([[1,2,3],[3,4,5]])
np.repeat(A, 2)
np.repeat(A, 2,axis=0)
np.repeat(A, 2,axis=1)

A[0,0]

A[,0]  # NO VALE
A[:,0]
A[0,:]

np.zeros([2,2])
np.ones([2,2])
np.diag([1,2,3])
np.eye(3)

B = np.array([[0,2],[2,0]])

A+B

B = np.array([[0,2,-1],[2,0,-1]])

A+B

A*B

np.random.randint(2,5,size=(2,2))


C = np.random.randint(2,5,size=(2,5))
C.transpose()
C.T

np.triu(C)
np.tril(C)
np.diag(C)

np.linalg.inv(C)
np.linalg.matrix_rank(C)

