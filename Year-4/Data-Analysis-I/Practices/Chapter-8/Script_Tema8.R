###############################################################
### ANÁLISIS DE LA VARIANZA
### María José Nueda
###############################################################

#----------------------------------------------------------------------
#  EJEMPLO 1: ANOVA DE 1 FACTOR
#----------------------------------------------------------------------

# H0: mu1 = mu2 = mu3 = ... = muk = mu
# H1: Existe j / muj != mu

# Introducir datos:
	RESISTENCIA = c(1251,1275,1310,1235,1250,1152,1155,1105,1098,1144, 985,998,1003, 991, 998)
	DETERGENTE = rep(c("A","B","C"),each=5)

# Análisis de la varianza:
	resul = aov(RESISTENCIA~DETERGENTE)
	summary(resul)
	# Grados de libertad, suma de cuadrados, media de cuadrados, valor de la F
	
# ¡¡IMPORTANTE!! Si los grupos se definen con números hay que definirlos
# como factor para evitar que haga el ANOVA de RL
# DETERGENTE = factor(rep(c(1,2,3),each=5))

# Pruebas de normalidad de los datos usando: shapiro.test() y qqnorm()  
# Para aplicar estos comandos para cada una de nuestras muestras se usa tapply()_
	tapply(RESISTENCIA,DETERGENTE,shapiro.test)
	par(mfrow=c(1,3))
	tapply(RESISTENCIA,DETERGENTE, f<-function(x){qqnorm(x);qqline(x)})

# Utilizando los residuos:
	shapiro.test(resul$residuals)
	qqnorm(resul$residuals)
	qqline(resul$residuals)	
	
# Test de igualdad de varianzas:
	bartlett.test(RESISTENCIA,DETERGENTE)
	# p-value = 0.05015
	# No es lo suficientemente pequeño para rechazar la igualdad de varianzas

# Podemos analizar las diferencias existentes entre las medias gráficamente, 
# o mediante comparaciones múltiples (con contrastes o bien con IC) 
# ajustando los niveles de significación.
	boxplot(RESISTENCIA~DETERGENTE,col="grey",xlab="DETERGENTE",ylab="ABRASION")
	pairwise.t.test(RESISTENCIA,DETERGENTE,p.adjust.method ="bonfe")
	TukeyHSD(resul)
	
pairwise.t.test(RESISTENCIA,DETERGENTE,p.adjust.method ="none")

# H0: mu1 = mu2
# H1: mu1 != mu2
# p-value = 1.1e-6 (sin ajuste)
# p-value = 3.3e-6 (ajustado por bonferroni (multiplicando "sin ajuste" por 3))
	
# H0: mu1 = mu3
# H1: mu1 != mu3
# p-value = 4.3e-10 (sin ajuste) más pequeño
# La diferencia más grande está entre el grupo 1 y el grupo 3 (mirar gráfico)
# p-value = 1.3e-9 (ajustado por bonferroni)
	
# H0: mu2 = mu3
# H1: mu2 != mu3
# p-value = 9.1e-7 (sin ajuste)
# p-value = 2.7e-6 (ajustado por bonferroni)

# k = 3 grupos
# l = k sobre 2 = 3 sobre 2 = 3 comparaciones dobles
# 1 comparación triple
# 3 + 3 + 1 = 7 test

# k = 4 grupos
# dobles: 4 sobre 2 = 4!/(2!*2!) = (4*3)/2 = 6
# triples: 6
# cuádruples: 1
# 4 + 6 + 6 + 1 = 17 test
# triples, cuádruples... suelen ser no significativos y no se suelen estudiar


#----------------------------------------------------------------------
# EJEMPLO EXTRA
#----------------------------------------------------------------------

f = factor(rep(c("A","B"),rep(10,2)))

y = rnorm(20)
t.test(y-f)
t.test(y-f)$p.value

PVALUES = NULL
for (i in 1:100)
{
 y = rnorm(20)
 tabla = summary(aov(y-f))
 PVALUES= c(PVALUES,t.test(y-f)$p.value)
}
sum(PVALUES<0.05)
sum(p.adjust(PVALUES,method= "bonferroni")<0.05)
sum(p.adjust(PVALUES,method= "fdr")<0.05)

# alphag = 1-P(ningún error) = 1-(1-alpha)^3 = 1-0.95^3 = 0.1426
1-0.95^3
# (1-alpha)^3 = 1 - alphag
# 1- alpha = sqrt3(1-alphag)
# alpha = 1 - sqrt3(1-alphag) = 0.01695
1-0.95^(1/3)
# alphag = 1-P(ningún error) = 1-(1-alpha)^3 = 1-(1-3*alpha-...(muy pequeños)) = 3*alpha
# alpha = alphag/3 = 0.05/3 = 0.0167


#----------------------------------------------------------------------
# EJEMPLO 2: MANOVA UN FACTOR
#----------------------------------------------------------------------

	data(iris)
# Considerando una única variable: Sepal.Length
	resul = aov(iris$Sepal.Length~iris$Species)
	summary(resul)
	# Sale significativa
	boxplot(iris$Sepal.Length~iris$Species,col="grey")
	pairwise.t.test(iris$Sepal.Length,iris$Species,p.adjust.method="bonfe")

# H0: mu1 = mu2 = mu3 = mu
# H1: Existe j / muj != mu
# muj pertenece a R4
# mu1 = (mu11, mu12, mu13, mu14)
	
# Con 4 variables:
	Y = as.matrix(iris[,1:4])
	resul2 = manova(Y ~ iris$Species)
	
# Esto no lo vamos a analizar porque no entra MANOVA en teoría
	
# Contraste Multivariante (por defecto saca Pillai)
	summary(resul2)

# Para obtener otros contrastes se indicará en test (ver ?summary.manova las opciones)
	summary(resul2, test="Wilks")

# Contrastes variable a variable:
	summary.aov(resul2)
	
# El menor p-valor es el de Petal.Lenght, porque la F es más grande, después
# Petal.Width, después Sepal.Length y por último Sepal.Width.
# Todas las diferencias son muy significativas.
# La que tiene F más grande es la que tiene mayor capacidad de discriminar/diferenciar
# entre grupos.

# Comparación de medias de grupos usando funciones discriminantes canónicas
	library(MASS)
	z = lda(iris$Species~., iris)
	p = predict(z,iris)
	Y= p$x
	
	resul3 = manova(Y ~ iris$Species)
	summary.aov(resul3) 
	pairwise.t.test(p$x[,1],iris$Species,p.adjust.method="bonfe")
	# Todas las diferencias por pares son significativas
	pairwise.t.test(p$x[,2],iris$Species,p.adjust.method="bonfe")
	# Entre setosa y virginica no hay diferencias significativas
	
# gráficamente:
	par(mfrow = c(1,3)) 	
	plot(p$x,col = as.numeric(iris$Species))
	boxplot(p$x[,1]~iris$Species)
	# En el boxplot con LD1 se aprecia lo mismo que en el primer gráfico (de puntos)
	boxplot(p$x[,2]~iris$Species)
	# Entre setosa y virginica no hay diferencias significativas porque las cajas 
	# se solapan en gran parte con LD2 (segundo boxplot)

	
###############################################################
### EJEMPLO 3: DOS FACTORES Y UNA VARIABLE:
###############################################################

	S.INF = read.table("S_INF.txt",header=TRUE)
# Hay que indicar que las variables son cualitativas para que considere factores
	S.INF$FICHEROS = as.factor(S.INF$FICHEROS)
	S.INF$BUFFERS = as.factor(S.INF$BUFFERS)
	# Cuando sale Levels es factor
	
	ej2 = aov(TIEMPO~FICHEROS*BUFFERS, data=S.INF)
	summary(ej2)
	# Todo es muy significativo (FICHEROS, BUFFERS y la interacción)

# Comparaciones múltiples:
TukeyHSD(ej2)

# Gráficamente;
par(mfrow=c(1,2))
boxplot(S.INF$TIEMPO~S.INF$FICHEROS)
# Hay diferencia de todos con todos de ficheros (se puede ver con los p-valores también)
boxplot(S.INF$TIEMPO~S.INF$BUFFERS)
# No hay diferencia entre 20 y 30 (se solapan), pero sí entre 10 y 20, 10 y 30
par(mfrow=c(1,2))
interaction.plot(S.INF$FICHEROS,  S.INF$BUFFERS ,S.INF$TIEMPO,  col=c(1,2,3))
# Queremos estudiar la variable TIEMPO, que lo ponemos en tercera posición para
# representarlo en el eje Y
# Hay diferencias significativas porque las rectas no son paralelas
interaction.plot(S.INF$BUFFERS, S.INF$FICHEROS, S.INF$TIEMPO,  col=c(1,2,3))

# Sistema 1: con 10 buffers tarda 2.5, con 20 tarda menos y con 30 menos
# Sistema 2: disminuye también
# Sistema 3: explota, hay interacción

boxplot(S.INF$TIEMPO~S.INF$FICHEROS:S.INF$BUFFERS)

# Si queremos ver en el gráfico todos los valores y los valores medios:
 S.INF = read.table("S_INF.txt",header=TRUE)
 plot(S.INF$FICHEROS,  S.INF$TIEMPO,col=as.numeric(S.INF$BUFFERS)/10, xlim=c(1,3.5), xaxt="n")
 interaction.plot( S.INF$FICHEROS,  S.INF$BUFFERS ,S.INF$TIEMPO,  col=c(1,2,3), add=TRUE)
# Los puntos están muy pegados a la recta, no hay solapes
# Por eso sale significativo
 
# Si las rectas son paralelas sale no significativa la interacción
