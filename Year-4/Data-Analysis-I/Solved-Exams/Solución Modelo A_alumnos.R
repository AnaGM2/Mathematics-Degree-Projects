#### SOLUCIÓN EJERCICIO 15/10/2020

library(MASS)
head(petrol)
X=petrol[,-1]

## EJ 1

source('ACP.R')
ej1 = ACP(X, q=3)
# a)
ej1$Inercia[3,2]
# b)
ej1$princomp$sdev[2]^2
# c) 2 CP porque la media es 1 y hay 2 cuya varianza supera el 1.
ej1$princomp$sdev^2 
# Sí es adecuado porque IE2 es 0.8952, que es muy alta.
# d) 
ej1$mu[2]
#e) 
ej1$princomp$scores[15,2]
#f)
ej1$ro[15]
#g)
n=nrow(petrol)
var = apply(X,2,var)*(n-1)/n
M2=diag(1/sqrt(var))
M2.inv=diag(sqrt(var))
uk=M2.inv%*%ej1$princomp$loadings[,1]
#h) A partir de las correlaciones entre CP y vars orginales, que son:
ej1$R[,1]
# podemos decir que la 1ª CP tiene altas correlaciones positivas con SG, VP y negativas con 
# V10. Por lo tanto los crudos con altos valores para SG, VP y bajos para V10 tendrán 
# valores altos para la 1ª CP. 

## EJ 2
source('AC.R')
lab <- c(rep(c("lab1","lab2","lab3"), 8), rep("lab4",8))
tipo <- rep(c("I","II","III"), c(10,10,12))
Tabla <- table(lab,tipo)

# El test chi-cuadrado obtenido con: 
summary(Tabla)
# nos da un p.valor de 0.005029 por lo que podemos rechazar la hipótesis de independencia
# entre las dos variables y tiene sentido el AC.

# Con 
AC(Tabla)
# observamos que con 1 eje la IE=0.9784 y con 2 ejes IE=1. Podemos decir que con el primer
# eje es suficiente ya que explica las relaciones más importantes.
# Con 1 eje todas las categorías, tanto filas como columnas están bien representadas.
# Tanto el gráfico como las puntuaciones nos indican que lab4 se identifica con el tipo III
# y los laboratorios 1, 2 y 3 se reparten las muestras I y II.


## EJ 3
V = matrix(c(4,0,0.6,0,4,0.8,0.6,0.8,1),3,3)
M2 = diag(diag(V)^(-1/2))
S = M2%*%V%*%M2
vals = eigen(S)$values 
cumsum(vals/sum(vals))[2] # solución IE2 (modelo A)

v1 = eigen(S)$vectors[,1]
xi = c(1,3,4)
yi = xi%*%M2%*%v1 # solución proyección individuo (modelo B)


