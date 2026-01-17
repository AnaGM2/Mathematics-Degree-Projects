
############### EJERCICIO 1 ###############

source("ACP.R")
X = read.table("NIÑOS.txt", header=TRUE)
ej1 = ACP(X)

# La puntuación del niño 3 con respecto a la segunda componente principal es:
ej1$princomp$scores[3,2]


############### EJERCICIO 2 ###############

# El objeto "R" es una de las salidas del programa ACP.R que nos sirve para:
# Interpretar las componentes principales.
# Representar a las variables originales en la nueva dimensión.


############### EJERCICIO 3 ###############

round(ej1$R, 3)

ej1$ro[6]
ej1$ro[21]

ej1$ro[20]
ej1$ro[53]
# Los niños 20 y 53 deben ser de los más pequeños


############### EJERCICIO 4 ###############

acp1 = princomp(X)
acp2 = princomp(X, cor=TRUE)

acp1$loadings
acp2$loadings

apply(acp1$loadings,2,function(x){sum(x^2)})
apply(acp2$loadings,2,function(x){sum(x^2)})

# El objeto "loadings" es una de las salidas de la función "princomp" que son:
# Vectores propios unitarios (ONO) de S o de V.


############### EJERCICIO 5 ###############

ej5 = ACP(X, q=3)
round(ej5$R, 3)

# La 1ª componente está relacionada con las variables que describen al niño.


############### EJERCICIO 6 ###############

round(ej5$Inercia[0:3,], 3)

# Explicamos más del 80% de la inercia o variabilidad total.


############### EJERCICIO 7 ###############

princomp(X)               # Sobre V (matriz de covarianzas)
princomp(X, cor=TRUE)     # Sobre S (matriz de correlaciones)

# Se puede escoger la matriz de correlaciones o la matriz de covarianzas.


############### EJERCICIO 8 ###############

ej5$ro
sum(ej5$ro<0.75)  # Niños mal representados


############### EJERCICIO 9 ###############

round(ej1$R, 3)

ej1$ro[66]
ej1$ro[38]

# Los casos 66 y 38 están asociados a niños grandes.


############### EJERCICIO 10 ###############

round(ej5$R, 3)

# La 3ª componente identifica a madres que tienen correlación negativa entre
# PESO-TALLA y PAS-PAD.


############### EJERCICIO 11 ###############

ej5$mu
sum(ej5$mu<0.7)   # Variables mal representadas


############### EJERCICIO 12 ###############

# El programa ACP.R calcula las correlaciones entre variables originales y
# componentes principales: a partir del objeto "loadings" de la función princomp.

# R = acp$loadings[, 1:q]%*%diag(acp$sdev[1:q])


############### EJERCICIO 13 ###############

ej1$princomp$sdev^2

# Hay 3 valores propios mayores que 1.


############### EJERCICIO 14 ###############

ej1$ro[99]

# No podemos decir nada sobre el niño 99.


############### EJERCICIO 15 ###############

# El programa ACP.R aplica un Análisis de Componentes Principales a partir de:
# La matriz de correlaciones.

# acp = princomp(X, cor=T)