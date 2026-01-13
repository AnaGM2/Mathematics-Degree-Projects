############################
# PROBLEMAS PROPUESTOS 3.34
############################


# MUESTRA

Xo=rbind(c(748,74,31,9),c(821,60,25,10),c(786,51,22,6),c(720,66,16,5),c(672,50,15,7))

# NOMBRE DE LAS COLUMNAS

colnames(Xo)=(c("0","1","2",">2"))

# NOMBRE DE LAS FILAS

rownames(Xo)=(c("<30","30-40","40-50","50-60",">60"))

# TRANSFORMAR EN TABLA

T=as.table(Xo)

# SUMARIO (Chisq es el coeficiente de contingencia)

summary(T)

# COEFICIENTE DE CONTINGENCIA

c=summary(T)$statistic

# V DE CRAMER

t=min(dim(T)-1)
n=sum(T)
V=sqrt(c/(t*n))

# TABLA DE LAS FRECUENCIAS ESPERADAS

Xe=chisq.test(T)
Xe$expected



############################
# PROBLEMAS PROPUESTOS 3.56
############################


# VARIABLES

I=c(1960,1040,2150,2640,2820,2320,2270,3980,3440,4170,2580,1840,2200,1720,1100)
T=c(78,68,89,121,129,103,108,135,147,131,125,113,78,83,74)
R=c(328,78,281,392,263,299,239,334,366,352,356,178,268,156,115)
A=c(329,237,368,435,465,368,400,603,575,675,411,356,350,282,185)

# SUMARIO

summary(I)

# MEDIA

mean(I)

# VARIANZA

var(I)

# COVARIANZA

cov(I,T)

# MEDIA, VARIANZA Y COVARIANZA

mean(I);var(I);mean(T);var(T);mean(R);var(R);mean(A);var(A);cov(I,T);cov(I,R);cov(I,A)

# El que mayor covarianza tenga será el que esté más relacionado (gastos de alimentación)

# REPRESENTACIÓN PUNTOS

plot(I,T)
plot(I,R)
plot(I,A)

# COEFICIENTE DE CORRELACIÓN LINEAL

cor(I,T);cor(I,R);cor(I,A)

# COEFICIENTE DE DETERMINACIÓN

cor(I,T)^2;cor(I,R)^2;cor(I,A)^2

#RECTA DE REGRESIÓN LINEAL

lm(I~A)

I=6.706A-284.623

lm(A~I)

A=0.1451I+52.1353

# REPRESENTACIÓN RECTA

plot(I~A);abline(lm(I~A))
plot(I~R);abline(lm(I~R))
plot(I~T);abline(lm(I~T))

# PREDICCIONES

x=data.frame(A=450);predict(lm(I~A),x)

x=data.frame(I=1000);predict(lm(A~I),x)
