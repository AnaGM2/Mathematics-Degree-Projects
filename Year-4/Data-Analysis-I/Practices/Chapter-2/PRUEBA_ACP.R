
############### EJERCICIO 1 ###############

# Al aplicar ACP con M = D(1/sigma^2)

V = matrix(c(25,-8,11.7,-8,4,0,11.7,0,36),3,3)

# Si tomamos q=1, calcula:

# a) La inercia explicada (proporción): 0.63

M = diag(diag(V)^(-1))
S = M^(1/2)%*%V%*%M^(1/2)
vals = eigen(S)$values
IE = max(vals)/sum(vals)
IE

# b) La proyección de un individuo cuyos valores centrados son (0,2,6): -0.33

xi = c(0,2,6)
w1 = eigen(S)$vectors[,1]

# Comprobación
S%*%w1
vals[1]*w1

yi1 = xi%*%M^(1/2)%*%w1
round(yi1,2)

# c) La calidad de representación del individuo del apartado anterior: 0.05

num = yi1^2
denom = xi%*%M%*%xi
ro = num/denom
round(ro,2)

# d) La correlación entre x3 y la componente principal: 0.43

# Rxy = D(1/sigma)*U*D(sqrt(lambda)) = D(1/sigma)*M^(-1/2)*W*D(sqrt(lambda)) = 
# = M^(1/2)*M^(-1/2)*W*D(sqrt(lambda)) = W*D(sqrt(lambda))

Rxy = w1 * sqrt(vals[1])
round(Rxy[3],2)

# e) La calidad de representación de la segunda variable: 0.76

mu21 = Rxy[2]^2
round(mu21,2)


############### EJERCICIO 2 ###############

DATA <- read.table("DATA.txt",header=T)

# Al aplicar un Análisis de Componentes Principales con 3 ejes se obtiene:

source("ACP.R")
ej2 = ACP(DATA,q=3)

# a) El porcentaje de inercia explicada es de: 85,03%

ej2$Inercia[3,2]

# b) Si tomamos un 0.7 para decidir la buena representación de variables e 
# individuos, podemos decir que hay 2 variables mal representadas y 12 individuos
# mal representados.

# Variables mal representadas:
sum(ej2$mu<0.7)

# Individuos mal representados:
sum(ej2$ro<0.7)

# c) La variable peor representada es sodium y su calidad de representación es 0.59

ej2$mu[ej2$mu==min(ej2$mu)]
round(min(ej2$mu),2)

# d) El individuo 29 tiene una calidad de representación de 0.92

round(ej2$ro[29],2)

# e) El valor que toma para la primera componente principal el individuo 29 es 6.39

round(ej2$princomp$scores[29,1],2)

# f) Si consideramos como importantes las correlaciones mayores a 0.5 (sin tener en
#  cuenta el signo), indica si son Verdaderas o Falsas las siguientes afirmaciones:

ej2$R

# 1. La 1ªCP se identifica en general con todas las variables, excepto con sugars: V

# 2. La 2ªCP detecta que en algunos cereales hay relación inversa entre el nivel 
# de fibra y los niveles de fat-sugar: F

# 3. La 3ªCP se identifica únicamente con los niveles de carbohidratos: F

