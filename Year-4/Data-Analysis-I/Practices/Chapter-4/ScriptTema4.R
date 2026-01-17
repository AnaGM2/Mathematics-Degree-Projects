######  TEMA 4: Análisis de Escalas Multidimensionales
######   María José Nueda Roldán
library(MASS)

### EJEMPLO APUNTES DE TEORIA -------------------------

d = matrix(c(0,3,sqrt(10),1,3,0,1,sqrt(10),sqrt(10),1,0,3,1,sqrt(10),3,0),4,4,byrow=T)	
d = as.dist(d)

# Método métrico o clásico, nos da la configuración de puntos:
emd.0 = cmdscale(d)
plot(emd.0)

# Al solicitar valores propios y sigma el resultado es una lista:
emd.0 = cmdscale(d, eig = TRUE, x.ret = TRUE)
names(emd.0)
emd.0$points
plot(emd.0$points)

# Calidad de la representación:
round(emd.0$eig^2/sum(emd.0$eig^2),4)

### EJEMPLO RECTÁNGULOS  -------------------------

medidas = read.table("medidas.txt")
medidas
disi.recta = read.table("disirecta.txt")
disi.recta = as.dist(disi.recta)
disi.recta

#Método métrico:
emd.1 = cmdscale(disi.recta, eig=TRUE)
plot(emd.1$points, type = "n")
text(emd.1$points, labels = c(1:9))
cor(medidas,emd.1$points)
cumsum(emd.1$eig^2 / sum(emd.1$eig^2))

# Método no métrico:
emd.2 = isoMDS(disi.recta)
plot(emd.2$points, type = "n")
text(emd.2$points, labels =c(1:9),col=2)

## Diagrama de Shepard
she = Shepard(disi.recta, emd.2$points)
plot(she)
cor(she$x, she$y)

## Interpretación del resultado
cor(medidas, emd.2$points)

## Análisis a partir de las distancias euclídeas de medidas:
d.medidas = dist(medidas)
emd.3 = cmdscale(d.medidas)
plot(emd.3, type = "n")
text(emd.3, labels = c(1:9))
cor(medidas,emd.3)

# Solución clásica (métrica):
# tau_q = (lamda_1^2+lambda_2^2) / (sum(lambda^2))
# stress
# cor(delta_ij, d_ij) (Shepard)

# Solución no métrica:
# stress
# cor(delta_ij, d_ij) (Shepard)

### EJEMPLO ANIMALS  -------------------------
animals = read.csv("animals.csv", sep=";", row.names = 1)
animals
dis = dist(animals, method = "binary")
emd.1 = cmdscale(dis, eig=TRUE)
plot(emd.1$points, type = "n")
text(emd.1$points, labels = rownames(animals))
cumsum(emd.1$eig^2 / sum(emd.1$eig^2))


############### EJERCICIO 1 ###############

D = read.table("disicoches.txt")
D = as.dist(D)
carac = read.table("caracoches.txt",header=TRUE,row.names=1)
head(carac)

# Apartado a)

#Método métrico:
emd.1 = cmdscale(D, eig=TRUE)
plot(emd.1$points, type = "n")
text(emd.1$points, labels = rownames(carac))
cumsum(emd.1$eig^2 / sum(emd.1$eig^2))
# Calidad de representación: 0.9655698

# Apartado b)

# Método no métrico:
emd.2 = isoMDS(D)
plot(emd.2$points, type = "n")
text(emd.2$points, labels =rownames(carac), col=2)

# Comprobación:
plot(emd.1$points, type = "n")
text(emd.1$points, labels = rownames(carac))
text(emd.2$points, labels =rownames(carac), col=2)
# Lo mejora un poco, aunque no cambia demasiado.

# Diagrama de Shepard
par(mfrow=c(1,2))
she = Shepard(D, emd.1$points)
plot(she,main="Método métrico")
cor(she$x, she$y)

she = Shepard(D, emd.2$points)
plot(she,main="Método no métrico")
cor(she$x, she$y)

# Apartado c)

plot(emd.1$points, type = "n")
text(emd.1$points, labels = rownames(carac))
text(emd.2$points, labels =rownames(carac), col=2)
# Carrera
# Opel-car

# Apartado d)

cor(carac,emd.1$points)

# Primer eje altas correlaciones con potencia y precio
# A la derecha más potencia y más caros

# Segundo eje negativamente con tamaño
# Arriba más pequeños

# El consumo aparece repartido entre los dos ejes

cor(carac,emd.2$points)

cor(carac)

# Potencia con precio
# Consumo con tamaño y potencia

emd.1$eig^2/sum(emd.1$eig^2)


############### EJERCICIO 2 ###############

emd.1 = cmdscale(eurodist, eig=TRUE)
cumsum(emd.1$eig^2 / sum(emd.1$eig^2))
plot(emd.1$points, type="n")
text(emd.1$points, labels = rownames(as.matrix(eurodist)))

emd.2 = isoMDS(eurodist)
text(emd.2$points, labels = rownames(as.matrix(eurodist)),col=2)

