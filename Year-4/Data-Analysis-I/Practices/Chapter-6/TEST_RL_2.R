
############### EJERCICIO 1 ###############

datos=read.table("datos.txt", header=TRUE)

reg = lm(y~., data=datos)

# 1) Modelo estimado: y.estim = 28.64 - 0.81x1 + 0.57x2 + 1.16x3

round(reg$coefficients,2)

# 2) alpha = 0.05

summary(reg)

# x1: Sí
# x2: No
# x3: Sí

# 3) R2 del modelo eliminando una a una las variables que no sean estadísticamente
# significativas hasta lograr un modelo con todas las variables significativas: 0.35

# Quito la menos significativa, que es x2:

summary(lm(y~x1+x3, data=datos))

# 4) Influyentes a posteriori todos los casos que tienen un valor superior a 1 para
# el estadístico que mide la influencia a posteriori: 1

sum(cooks.distance(reg) > 1)

# 5) No hay problemas de heterocedasticidad (p-valor=0.8384 es alto)

res2 = reg$residuals^2
summary(lm(res2~x1+x2+x3, data=datos))


############### EJERCICIO 2 ###############

# Modelo de regresión lineal para predecir BD a partir del resto de variables 
# morfológicas (FL, RW, CL y CW) sin que haya problemas de multicolinealidad.

crabs=read.table("crabs2.txt", header=TRUE)
head(crabs)

source("Multicoli.R")
Multicoli(crabs[,2:5])
# Hay multicolinealidad

reg0 = lm(BD~FL+RW+CL+CW, data=crabs)

step1 = step(reg0, direction="both")

reg2 = lm(BD~FL+CL+CW, data=crabs)
summary(reg2)

Multicoli(crabs[,c(2,4,5)])
# Sigue habiendo multicolinealidad

reg1 = lm(BD~1, data=crabs)
summary(reg1)

step2 = step(reg1,scope=~FL+RW+CL+CW, direction="both")

reg3 = lm(BD~FL, data=crabs)
summary(reg3)

# No hay multicolinealidad por tomar una única variable

# 1) Coeficiente R2: 0.98

# 2) Variables escogidas: FL
