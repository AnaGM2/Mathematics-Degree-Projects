# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:41:40 2024

@author: gilpe
"""

import numpy as np

b=20
g=5
p=53
m = int(np.sqrt(p))
m


def pasos_bebe(b, g, p):
    m = int(np.sqrt(p))
    B = []
    for r in range(m):
        B.append(((b * pow(g, -r, p)) % p, r))
    return B

B = pasos_bebe(b,g,p)
B


c = g**m % p
c

def pasos_gigante(g,p,B):
    m = int(np.sqrt(p))
    c = g**m % p
    q = 1
    bg_r = [x[0] for x in B]
    while (c**q % p) not in bg_r:
        q += 1
    for x in B:
        if x[0] == c**q % p:
            r = x[1]
            print(q)
    x = q*m + r
    return x

pasos_gigante(g,p,B)



y = 1029366015284
e = 65537
n = 4029290161843

pow(y,e,n)




from sympy import factorint

B = [2,3,5,7,11]

p = 229


S = [z for z in range(1,p)]


def f(x,n):
    return x**2 - n

def B_suaves(B,S,n):
    suaves_B = []
    for x in S:
        Px = f(x,n)
        for q in B:
            if Px % q == 0:
                while Px % q == 0:
                    Px = Px // q
        if Px == 1:
            suaves_B.append(x)
    return suaves_B

suaves = B_suaves(B,S,p)
suaves


def devuelve_es(suaves,Base):
    es=[]
    for i in suaves:
        e=np.zeros(len(Base))
        n=factorint(i)
        if 2 in n:
            e[1]=n[2]
        for j in range(2,len(Base)):
            if Base[j] in n:
                e[j]=n[Base[j]]
        es=es+[e]
    return es

devuelve_es(suaves,B)



def descomposicion(n, base):
    descomp = []
    for p in base:
        freq = 0
        q2, r = divmod(n, p)
        if r == 0:
            while r == 0:
                q = q2
                freq += 1
                q2, r = divmod(q, p)
            n = q
        descomp.append(freq)
    if n == 1:
        mensaje = 'Hecho'
    else:
        mensaje = 'No hecho'
    return [descomp, mensaje]

for n in S:
    descomposicion(n,B)