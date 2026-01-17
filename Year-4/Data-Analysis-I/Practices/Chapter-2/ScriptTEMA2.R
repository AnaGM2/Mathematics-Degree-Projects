######  TEMA 2: Análisis de Componentes Principales
######   María José Nueda Roldán


##### EJEMPLO 1  ---------------------------

	X = matrix(c(8,4,6,10,8,0,1,6,8,4,2,3,0,5,7,7,5,6),6,3)
	p = ncol(X)
	n = nrow(X)
	medias = apply(X,2,mean)
	Xc = X-(matrix(1,n,1)%*%medias)
	source('stand.R') # para cargar el programa stand
	stand(X)

# Cálculos a partir de la matriz V (tomando M = I)	
	V = t(Xc)%*%Xc/(n) # o bien V = cov(Xc)*(n-1)/n
	vals1 = eigen(V)
	apply(vals1$vectors,2,function(x){sum(x^2)})  # son unitarios
	
# Cálculos a partir de la matriz S (M = D(1/var))
	S = cor(Xc)
	vals2 = eigen(S)
# S también se puede calcular con:
	des = apply(X,2,sd)*sqrt((n-1)/n)
	D= diag(1/des)
	D%*%V%*%D

# Función de R: princomp()
	?princomp
	acp1 = princomp(X) # por defecto cor = FALSE
	names(acp1)
	acp2 = princomp(X, cor = TRUE)

# Se puede comprobar que coinciden:
	vals1$values 
	acp1$sdev^2
	
	Xc%*%vals1$vectors          # Y = XMU
	acp1$scores
	
	vals2$values 
	acp2$sdev^2
	
	stand(X)%*%vals2$vectors    # stand(X) = XD(1/des)
	acp2$scores
	
#### EJEMPLO 2  a) ---------------------------

	NOTAS <- read.table("NOTAS.txt",header=T)
	
# Matriz de correlaciones
	round(cor(NOTAS), 3)

# Análisis a partir de S
	acp <- princomp(NOTAS, cor=TRUE)

# Desviación típica de cada componente
	acp$sdev

# Varianza = Valores propios	
	acp$sdev^2

# Abrir programa ACP y ver detalles.
	source("ACP.R")
# Lo ejecutamos con NOTAS e interpretamos los resultados:
	
	ej2 = ACP(NOTAS, q=2)
	names(ej2)
	ej2$princomp$sdev
	ej2$Inercia
	ej2$R
	ej2$mu
	ej2$ro
	sum(ej2$ro>0.7)
	which(ej2$ro>0.7)


############# EJERCICIO 1 #############

# Apartado a)

Y = ej2$princomp$scores[,1:2]

# Medias 0
round(apply(Y,2,mean))

# Varianzas lamda1,...,lambdaq
apply(Y,2,var)*7/8
ej2$princomp$sdev^2

# Covarianzas 0
round(cov(Y),5)

# Apartado b)

S= cor(NOTAS)
vals = eigen(S)

stand(NOTAS)%*%vals$vectors
ej2$princomp$scores

# Apartado c)

sum(ej2$princomp$sdev^2)
ej2b = princomp(NOTAS)
sum(ej2b$sdev^2)
sum(apply(NOTAS,2,var)*7/8)


############# EJERCICIO 2 #############

source("ACP.R")
X= read.table("NIÑOS.txt", header=TRUE)
head(X)

# Apartado a)

ej2 = ACP(X, q=3)
round(ej2$Inercia, 3)
# media(lambda) = sum(lambda_k)/p = p/p = 1
ej2$princomp$sdev^2

# Apartado b)

round(ej2$R, 3)
# cor(X, ej2$princomp$scores[,c(1:3)])
# IE -> 46%, 22%, 19%
round(cor(X),2)

# Apartado c)

ej2$mu
# No, PCR no está bien representada

# Apartado d)

ej2$ro
sum(ej2$ro<0.7)
which(ej2$ro<0.7)
ej2$ro[ej2$ro<0.7]

# Apartado e)

# Tienen una componente 1 alta, por lo que son niños grandes
# Mirando la componente 2, la madre tomará valores medianos
ej2$ro[31]
ej2$ro[38]
ej2$ro[66]
ej2$ro[7]
# Está un poco por debajo de la media de la componente, pero no está bien representado
# No podemos afirmar que sea un niño mediano
ej2$ro[99]


############# EJERCICIO 3 #############

ACP(X,q=1)


############# EJERCICIO 4 #############

V = matrix(c(1,0,-0.8,0,4,0.6,-0.8,0.6,4),3,3)
M2=diag(diag(V)^(-1/2))
S=M2%*%V%*%M2
vals=eigen(S)$values
cumsum(vals/sum(vals))[2]
