
############### EJERCICIO 1 ###############

Disi = read.table("disicoches.txt", header=TRUE)
Disi = as.dist(Disi)

hc1 <- hclust(Disi, method="average")
hc1$merge
hc1$height
plot(hc1, hang=-1)

# La primera unión que se produce es:
# Hay 4 uniones de 2 coches cada una que se producen a la vez.


############### EJERCICIO 2 ###############

# Dados unos argumentos de entrada concretos siempre da la misma solución: Jerárquico

# Una vez formados todos los grupos permite hacer cambios de grupo para intentar
# lograr una solución mejor: No-jerárquico

# Ofrece como resultado el detalle de las uniones entre individuos para formar 
# los grupos: Jerárquico


############### EJERCICIO 3 ###############

plot(hc1, hang=-1)
abline(h=3,col="blue")

# 5 grupos


############### EJERCICIO 4 ###############

X = read.table("caracoches.txt", header=TRUE)
Dist = dist(X)

set.seed(1)
KM = kmeans(X, 4)

cut1 = cutree(hc1, k=4)
table(cut1,KM$cluster)
# No coinciden

hc2 <- hclust(Dist, method="average")
cut2 = cutree(hc2, k=4)
table(cut2,KM$cluster)
# Coinciden


############### EJERCICIO 5 ###############

pisos = read.table("Pisos12.txt", header = TRUE)
D = dist(pisos, method="binary")

hc3 <- hclust(D, method="average")
plot(hc3, hang=-1)
rect.hclust(hc3, k=3, border="red")
# 3 grupos

hc4 <- hclust(D, method="complete")
plot(hc4, hang=-1)
rect.hclust(hc4, k=4, border="red")
# 4 grupos


############### EJERCICIO 6 ###############

plot(hc3, hang=-1)
rect.hclust(hc3, k=4, border="red")

# El piso 8 forma un grupo él sólo.


############### EJERCICIO 7 ###############

pisos
D

# 1-2
a = 3
b = 2
c = 2
d = 5
n = a+b+c+d

# La fórmula de la distancia binaria que usa R es:

# Sokal y Michener: No
(a+d)/n

# Sí
1-a/(a+b+c)

# No
a/(a+b+c)


############### EJERCICIO 8 ###############

DistEst = dist(scale(X))

hc5 <- hclust(DistEst, method="average")

cut4 = cutree(hc2, k=3)
cut5 = cutree(hc5, k=3)

table(cut4,cut5)
# No coinciden

par(mfrow=c(1,2))
plot(hc2, hang=-1)
rect.hclust(hc2, k=3, border="red")
plot(hc5, hang=-1)
rect.hclust(hc5, k=3, border="red")

X
max(X$precio)

# En ambos casos el coche más caro es el que más se diferencia del resto, pero 
# con el primer caso es más llamativa la diferencia.


############### EJERCICIO 9 ###############

# Para poder aplicar la función kmeans es necesario:
# Una de las dos: especificar el número concreto de clusters deseado O dar una
# matriz con los centroides iniciales.


############### EJERCICIO 10 ###############

D

# La distancia entre los pisos 1 y 3 es de: 0.75