##########################
# PROBLEMAS PROPUESTOS 2.1
##########################


# MUESTRA

X = c(785,921,812,638,844,926,977,1095,1080,1045,1145,952,935,848,725,796,995,894,687,852,846,751,925,1108,921,848,688,766,1016,925,850,872,1020,960,699,810,658,756,715,754,720,652,867,925,1080,1154,1025,659,745,686,965,1058,954,836,854,720,864,900,865,952)


# TABLA DE FRECUENCIAS

T = table(X)


# TAMAÑO DE LA MUESTRA

n = length(X)
n = sum(T)


# FRECUENCIA RELATIVA INDIVIDUAL

f = T/n


# FRECUENCIA ABSOLUTA ACUMULADA 

N = cumsum(T)


# FRECUENCIA RELATIVA ACUMULADA

F = cumsum(f)
F = N/n


# RANGO

range(X)


# HISTOGRAMA

hist(X)


# SUMARIO (Mínimo, Cuartil inferior, Media, Cuartil superior, Máximo)

summary(X)


# MEDIA

mean(X)


# MEDIANA

median(X)


# VARIANZA

var(X)


# DESVIACIÓN TÍPICA

sd(X)
sqrt(var(X))


# RECORRIDO INTERCUARTÍLICO

IQR(X)


# PERCENTILES "quantile(X,probs=k/100)"

quantile(X,probs=25/100)	#Cuartil inferior
quantile(X,probs=75/100)	#Cuartil superior
quantile(X,probs=90/100)	#Percentil de orden 90


# COEFICIENTE DE SIMETRÍA

B1 = (sum(X-mean(X))^3)/((n-1)*(sd(X))^3)


# COEFICIENTE DE CURTOSIS


B2 = (sum(X-mean(X))^4)/((n-1)*(sd(X))^4)
