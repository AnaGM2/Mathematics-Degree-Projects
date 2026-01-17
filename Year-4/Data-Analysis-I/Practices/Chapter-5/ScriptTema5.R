######  TEMA 5: Análisis Cluster
######   María José Nueda Roldán

# EJEMPLO 1

	AFRICA = read.table(file="AFRICA.txt", header=TRUE, row.names=1)
	D = dist(AFRICA)
	hc = hclust(D, method="single")
	names(hc)
	hc$merge
	# En negativo: individuos
	# En positivo: grupos
	# C1: 5, 11
	# C2: 3, 9
	# C3: 4, C1
	hc$height

	plot(hc)  
	plot(hc,hang=-1)
	abline(h=600, col="blue")
	rect.hclust(hc, k=3, border="red")
	
	cut = cutree(hc, k=3)
	names(which(cut==1))
	names(which(cut==2))
	names(which(cut==3))
	table(cut)

	hcb = hclust(D, method="complete")
	plot(hcb,hang=-1)
	cutb = cutree(hcb, k=3)
	table(cut,cutb)
	
	set.seed(2020)
	KM1 = kmeans(AFRICA, 3)
	names(KM1)
	KM1$cluster
	table(cut, KM1$cluster)     # Coincide el resultado
	
	KM2 = kmeans(AFRICA, centers = AFRICA[1:3,])
	table(cut, KM2$cluster)     # No coincide el resultado
	table(KM1$cluster, KM2$cluster)
	
	# centers = 3
	# centers = matriz(k,p)
	# k = 3 (nº de clusters)
	# p (nº de variables)
	
# si queremos partir de la solución del hclust:
	cent.hc = apply(AFRICA, 2, function(x){tapply(x, cut, mean)})
	# Con tapply se calcula la media por grupos
	KM3 = kmeans(AFRICA, centers = cent.hc)
	table(cut, KM3$cluster)
	
# Se puede usar nstart para aplicar kmeans con diferentes valores
# semilla mostrando como solución la mejor
	KM4 = kmeans(AFRICA, 3, nstart = 25)
	# Lo hace 25 veces y se queda con el mejor
	table(cut, KM4$cluster)

## ¡¡IMPORTANTE!! para evitar que las unidades de medida den más peso 
##	a unas variables que a otras a la hora de calcular la matriz de distancias
## es recomendable estandarizar los datos 

	D=dist(scale(AFRICA))	
	# Volver a aplicar todo lo anterior con esta D


# EJEMPLO 2
	animals = read.csv("animals.csv", sep=";", row.names = 1)
	dis = dist(animals, method = "binary")
	hc2 = hclust(dis, method="average") #probando con diferentes method salen los mismos grupos
	plot(hc2,hang=-1)
	
# EJEMPLO 3. Simulaciones
sd=0.5
	SIMU = rbind(matrix(rnorm(40, sd = sd), ncol = 2),
	             matrix(rnorm(40, mean = 1, sd = sd), ncol = 2),
	             cbind(rnorm(20,mean=1,sd=sd),rnorm(20,sd=sd)))
	colnames(SIMU) <- c("VAR1", "VAR2")
	km<-kmeans(SIMU,3)
	plot(SIMU, col = km$cluster, pch=rep(c(1,2,3),each=20) )

	
############### EJERCICIO 1 ###############
	
pisos = read.table("Pisos12.txt",header = TRUE)
pisos

# Apartado a)

D= dist(pisos, method="binary")

# Apartado b)

hc1 <- hclust(D, method="average")
plot(hc1, hang=-1)
# Tomamos 3 clusters
rect.hclust(hc1, k=3, border="red")

# Apartado c)

hc2 <- hclust(D, method="complete")
plot(hc2, hang=-1)
# Tomamos 4 clusters
rect.hclust(hc2, k=4, border="red")

# Apartado d)

cut1 = cutree(hc1, k=3)
cut2 = cutree(hc2, k=4)
table(cut1,cut2)


############### EJERCICIO 2 ###############

# Apartado a)

Disi = read.table("disicoches.txt", header=TRUE)
Disi = as.dist(Disi)

hc3 <- hclust(Disi, method="average")
plot(hc3, hang=-1)
abline(h=3, col="blue")
# 5 clusters

# Apartado b)

X = read.table("caracoches.txt", header=TRUE)
Dist = dist(X)    # La solución está hecha sin escalar

hc4 <- hclust(Dist, method="average")
plot(hc4, hang=-1)

# Apartado c)

set.seed(1)
KM = kmeans(X, 4)

cut3 = cutree(hc3, k=4)
table(cut3, KM$cluster)

cut4 = cutree(hc4, k=4)
table(cut4, KM$cluster)
