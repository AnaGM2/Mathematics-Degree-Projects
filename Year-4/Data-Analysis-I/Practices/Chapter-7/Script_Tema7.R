#########################################################################
##  PRÁCTICA DE ANÁLISIS DISCRIMINANTE
## María José Nueda Roldán
#########################################################################

#----------------------------------------------------------------------
#   EJEMPLO 1: Préstamos 2 grupos		      
#----------------------------------------------------------------------
	X = read.table("Préstamos.txt")
	X$Impago = as.factor(X$Impago)
	
#--------------CRITERIO GEOMéTRICO-------------

	X1 = X[X[,1]=="Si",2:3]
	X2 = X[,2:3][X[,1]=="No",]
	n = nrow(X)
	n1 = nrow(X1)
	n2 = nrow(X2)
	media1 = apply(X1, 2, mean)
	media2 = apply(X2, 2, mean)
	S1 = var(X1)
	S2 = var(X2)
	S = ((n1-1)*S1+(n2-1)*S2)/(n1+n2-2)
	a=t(media1-media2)%*%solve(S)%*%(media1+media2)/2
	b=-t(media1-media2)%*%solve(S)
	
	# H := (mu1-mu2)t * V-1 * mu_ - (mu1-m2)t * V-1 * x = 0
	# mu_ = (mu1 + mu2)/2
	# a + b*x = 0
	# a = -3.52, b=(1.035,-0.931)
	# H := -3.52 + 1.035*Patri - 0.931*Deudas = 0
	# Deudas = -(-3.52/-0.931) - (1.035/-0.931)*Patri
	# Deudas = -a/b[2] - b[1]/b[2]*Patri

# Se evalúa a cada individuo respecto de H:
	eva = apply(X[,2:3],1,function(x){a+as.matrix(b)%*%x})
	eva
	
# X1 Grupo 1 -> Impago
# X2 Grupo 2 -> Paga

# Para crear una variable que contenga el grupo donde se clasifica cada individuo:
     pred = rep("Si",16)
     pred[eva>0] = "No"

# Comparación de grupo original y grupo donde se clasifica con ADiscriminante:
    table(pred, X[,1])

#Gráficamente:	
	plot(X[,2:3],col=as.numeric(X[,1]),pch=20)
	abline(a=-a/(b[2]),b=-b[1]/b[2])
	
# Hay un error (el 13, en negro) que paga pero aparece en el grupo de los morosos
#	porque sus características se corresponden con las de los morosos.

#-----------------  VARIABLES DISCRIMINANTES CANóNICAS -----------------------#
library(MASS)
	z = lda(Impago~Patrimonio+Deudas, data=X)
	names(z)
	z$scaling       # Vectores propios de W-1*B
	# LD1 = -0.422*Patri + 0.38*Deudas
	z$svd           # Raíz cuadrada de los valores propios de W-1*B
	P = predict(z, X)
	names(P)
	#Grupo en el que se clasifica cada individuo:
	P$class
	#prob.de ser del grupo dado el valor de d obtenido
	P$posterior
	#puntuación discriminante (es como scores)
	P$x
	# Los positivos a un grupo y los negativos al otro
	# Podemos visualizar los resultados con:
	plot(z)
	# Hay un error, en el grupo No hay uno positivo
# Para ver si hay errores de clasificación podremos hacer una tabla:
	table(P$class, X$Impago)

	#-----------------------------------------------------------------------
	## CÁLCULO DE PROBABILIDADES A POSTERIORI
	#-----------------------------------------------------------------------
	
	MVNORM <- function(x, p, mu, V)
	{
	  x = as.numeric(x)
	  mu = as.numeric(mu)
	  V = as.matrix(V)
	  (2*pi)^(p/2)*det(V)^(-1/2)*exp(-1/2*t(x-mu)%*%solve(V)%*%(x-mu) )
	}
	
	POSTERIORI = NULL
	for (i in 1:nrow(X))
	{
	  f1=MVNORM(x=X[i,2:3],p=2,mu=media1, V=S)
	  f2=MVNORM(x=X[i,2:3],p=2,mu=media2, V=S)
	  p1 = f1/(f1+f2)
	  p2 = f2/(f1+f2)
	  POSTERIORI = rbind(POSTERIORI,c(p1,p2))
	}
	
	POSTERIORI
#----------------------------------------------------------------------
#      EJEMPLO 2: IRIS	      
#----------------------------------------------------------------------
	data(iris)
	X = iris[,1:4]
	grupo = iris[,5]
	n = nrow(X)
	X1 = X[grupo=="setosa",]
	X2 = X[grupo=="versicolor",]
	X3 = X[grupo=="virginica",]
	n1 = nrow(X1)
	n2 = nrow(X2)
	n3 = nrow(X3)

#--------------CRITERIO GEOMéTRICO-------------

	media1 = apply(X1,2,mean)
	media2 = apply(X2,2,mean)
	media3 = apply(X3,2,mean)

	S1 = var(X1)
	S2 = var(X2)
	S3 = var(X3)
	S = ((n1-1)*S1+(n2-1)*S2+(n3-1)*S3)/(n1+n2+n3-3)
		
# H12:
	a1=t(media1-media2)%*%solve(S)%*%(media1+media2)/2
	b1=-t(media1-media2)%*%solve(S)
	
# H13:
	a2=t(media1-media3)%*%solve(S)%*%(media1+media3)/2
	b2=-t(media1-media3)%*%solve(S)
	
# H23:
	a3=t(media2-media3)%*%solve(S)%*%(media2+media3)/2
	b3=-t(media2-media3)%*%solve(S)


# Se evalúa a cada individuo respecto de H12, H13 y H23:
	eva12 = apply(X,1,function(x){a1+b1%*%x})
	eva13 = apply(X,1,function(x){a2+b2%*%x})
	eva23  =  apply(X,1,function(x){a3+b3%*%x})
	
# Grupo 1: negativo para H12 y H13
# Grupo 2: positivo para H12 y negativo para H23
# Grupo 3: positivo para H13 y H23

class = rep("NA",150)
class[eva12<0 & eva13<0 ] = "setosa"
class[eva12>0 & eva23<0 ] = "versicolor"
class[eva13>0 & eva23>0 ] = "virginica"

table(grupo , class)
# Hay 3 errores

	plot(X, col=as.numeric(grupo), pch=20)

#-----------------  VARIABLES DISCRIMINANTES CANóNICAS -----------------------#

	z = lda(Species ~Sepal.Length+Sepal.Width+Petal.Length+Petal.Width, iris)
	P = predict(z,iris)
	P$x
	# R4 -----> R2
	# {sepal, petal,...} --> {LD1, LD2}
	table(P$class, iris$Species)    
	# Hay 2 que se han clasificado como verdes pero son rojas
	# Hay una que se ha clasificado como roja pero es verde

	plot(z) 
	plot(z, abbrev=TRUE)
		
	# otra forma de hacer el gráfico:
	plot(P$x, col=as.numeric(iris$Species),pch=20)
	legend("bottomright",c("Setosa","Versicolor","Virginica"),col=c(1,2,3),pch=20)

#----------------------------------------------------------------------
# Evaluación del error con Validación cruzada:
#----------------------------------------------------------------------
	n = nrow(iris)
	set.seed(1) #necesario para reproducir los mismos resultados
	train = sample(n, 100)
	lda.training = lda(Species~., iris, subset = train)

	data.test = iris[-train,]
	pred.test = predict(lda.training, data.test)
	table(pred.test$class, data.test$Species) 
	
	
############### EJERCICIO 1 ###############
	
data = read.table("escarabajos.txt")
X = data[2:3]
grupo = data[,1]
n = nrow(X)

X1 = X[grupo=="concinna",]
X2 = X[grupo=="heikertingeri",]
X3 = X[grupo=="heptapotamica",]

n1 = nrow(X1)
n2 = nrow(X2)
n3 = nrow(X3)

# Apartado a)

media1 = apply(X1,2,mean)
media2 = apply(X2,2,mean)
media3 = apply(X3,2,mean)

S1 = var(X1)
S2 = var(X2)
S3 = var(X3)
S = ((n1-1)*S1+(n2-1)*S2+(n3-1)*S3)/(n1+n2+n3-3)

# H12:
a1=t(media1-media2)%*%solve(S)%*%(media1+media2)/2
b1=-t(media1-media2)%*%solve(S)

# H13:
a2=t(media1-media3)%*%solve(S)%*%(media1+media3)/2
b2=-t(media1-media3)%*%solve(S)

# H23:
a3=t(media2-media3)%*%solve(S)%*%(media2+media3)/2
b3=-t(media2-media3)%*%solve(S)

# Se evalúa a cada individuo respecto de H12, H13 y H23:
eva12 = apply(X,1,function(x){a1+b1%*%x})
eva13 = apply(X,1,function(x){a2+b2%*%x})
eva23 = apply(X,1,function(x){a3+b3%*%x})

class = rep("NA",74)
class[eva12<0 & eva13<0 ] = "concinna"
class[eva12>0 & eva23<0 ] = "heikertingeri"
class[eva13>0 & eva23>0 ] = "heptapotamica"

table(grupo , class)

# Hiperplano que separa los grupos concinna y heptapotamica:
# H13 := 114.128 -0.446*LONGITUD -4.194*ANGULO = 0

# Apartado b)

library(MASS)
z = lda(TIPO~LONGITUD+ANGULO, data=data)
P = predict(z, data)
P$x

# Valor que toma el individuo 11 para la primera variable discriminante canónica:
round(P$x[11,1],3)

# Hay un error:
table(P$class, data$TIPO)  


############### EJERCICIO 2 ###############

data <- read.table("EMPRESAS08.txt")

#Podemos formar así el vector con el grupo:
grupo <- rep("Bene", 54)
grupo[data$RESULTAD<0] <- "Pérdida"
data2 <- data[,-1]
adis <-lda(grupo~., data=data2)
plot(adis)
P <-predict(adis)
table(P$class,grupo)


############### EJERCICIO 3 ###############

library(MASS)
X <- read.table("Préstamos.txt")
X$Impago = as.factor(X$Impago)

z = lda(Impago~Patrimonio+Deudas, data=X)
P = predict(z, X)

X1 = X[X[,1]=="Si",2:3]
X2 = X[,2:3][X[,1]=="No",]
n = nrow(X)
n1 = nrow(X1)
n2 = nrow(X2)

# Apartado a)

SCT = (n-1)*var(X[,2:3])
SCW = (n1-1)*var(X1)+(n2-1)*var(X2)
SCB = SCT - SCW

m1=apply(X1,2,mean)
m2=apply(X2,2,mean)
m=apply(X[,2:3],2,mean)

# W-1*B
eig <- eigen(solve(SCW/n)%*%SCB/n)
eig$values
# lambda1 = 1.715
eig$vectors
# v1 = (0.7433, 0.4472)

# Apartado b)

U <- chol(SCW/16)
u1<-solve(U)

# (U-1)*B*(U-1)
M<-t(u1)%*%(SCB/n)%*%u1
v<-eigen(M)$vectors[,1]
# lambda1 = 1.715
# v1 = (-0.7479, 0.6638)
v%*%v

# Apartado c)

a = u1%*%v
# a = (-0.4516, 0.4064)

# lda()
z$svd^2
# lambdaR = 24.018
aR = z$scaling
# aR = (-0.4225, 0.3802)

# BR = SCB/(k-1)
# WR = SCW/(n-k)
# a = aR*sqrt(n/(n-k)) = (-0.4225, 0.3802)*sqrt(16/14) = (-0.4516, 0.4064)
aR*sqrt(16/14)
# lambda = lambdaR*(k-1)/(n-k) = 24.018*1/14 = 1.715

ld1 = as.matrix(X[,c(2,3)])%*%z$scaling
ld1-mean(ld1)
P$x

