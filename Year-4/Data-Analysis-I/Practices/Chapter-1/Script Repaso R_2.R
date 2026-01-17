################################################################
######   ANÁLISIS DE DATOS I. REPASO ESTADISTICA CON R - DATA.txt
######   María J. Nueda Roldán
######   Septiembre 2015
################################################################

	datos<-read.table("DATA.txt",header=T)
	datos
	head(datos)
	tail(datos)
	dim(datos)
	names(datos)
	SEXO<-c(rep("chica",20),rep("chico",20))

#############      ESTADÍSTICA DESCRIPTIVA        ############## 

# Para analizar una variable concreta de esta matriz de datos utilizaremos $, ej: datos2$ALTURA.
	mean(datos$NOTA)
	median(datos$NOTA)
	var(datos$NOTA)
	sd(datos$NOTA)
      IQR(datos$NOTA)
  	quantile(datos$NOTA)
	quantile(datos$NOTA,probs=0.8)

# Para analizar varias variables a la vez
	summary(datos)
	apply(datos, 2, mean)
	apply(datos, 2, var)
	cov(datos$ALTURA,datos$PESO)
	cor(datos$ALTURA,datos$PESO)
	var(datos)
	cor(datos)
	plot(datos)

#  ------------------------- GRÁFICOS  -------------------------

#Variable continua
	hist(datos$NOTA)
	hist(datos$NOTA,xlab="Nota",ylab="Frecuencia",main="Histograma",col="grey")
	stem(datos$NOTA)
	boxplot(datos$NOTA)

#Variable discreta. Creamos la variable CALIF:
CALIF <- rep(1,40)
CALIF[datos$NOTA>=5]=2
CALIF[datos$NOTA>=7]=3
CALIF[datos$NOTA>=9]=4

	barplot(table(CALIF))
	barplot(table(CALIF), names.arg=c("Suspenso","Aprobado","Notable","Sobresaliente"))
CALIF<-factor(CALIF, labels=c("Suspenso","Aprobado","Notable","Sobresaliente"))
	barplot(table(CALIF))
par(mfrow=c(2,2))	
	pie(table(CALIF))
	barplot(table(SEXO,CALIF),beside=T,col=c(3,4))
	 legend("topright",c("chico","chica"),fill=c(3,4))
	barplot(table(SEXO,CALIF),col=c(3,4))
	barplot(t(table(SEXO,CALIF)),beside=T,col=c(3,4,5,6))
	legend("topright",c("Apro","Not","Susp","Sob"),fill=c(3,4,5,6))

# Distinguiendo por sexo:
	par(mfrow=c(1,3))
	boxplot(datos$NOTA~SEXO, col=2, main="NOTA")
	boxplot(datos$ALTURA~SEXO,col=2,main="ALTURA")
	boxplot(datos$PESO~SEXO,col=2,main="PESO")


## NOTA: si hay variables discretas en un data.frame:
datos2<-cbind(datos,SEXO,CALIF)
summary(datos2) #para las variables alfanuméricas hace un recuento de datos por categorias
cov(datos2) #dará error porque datos2 tiene variables de tipo carácter 


############          INFERENCIA ESTADÍSTICA        ############ 

# Inferencia sobre una muestra. I.C. y test t de Student.

t.test(datos2$NOTA)       # Ofrece I.C. al 95% y contraste de hipótesis bilateral H0=0
t.test(datos2$NOTA, mu=6) # Ahora H0=6

# Inferencia sobre dos muestras independientes.
t.test(datos2$ALTURA~datos2$SEXO,var.equal=T,conf.level=0.9)

# Test de igualdad de varianzas
var.test(datos2$ALTURA~datos2$SEXO)


##########   PRUEBAS DE NORMALIDAD   ##########

# Normal Q-Q Plot
	qqnorm(datos$ALTURA)
	qqline(datos$ALTURA)

# Test para contrastar normalidad: shapiro.test 

	shapiro.test(datos$ALTURA)
	