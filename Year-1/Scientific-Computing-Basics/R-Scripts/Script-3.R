#############################################
# PROGRAMAS DE CÁLCULO CIENTÍFICO Y PROCESAMIENTO DE TEXTOS
#############################################

#############################################
# FUNCIONES SIMPLES
#############################################

area.cuadrado<-function(lado)
{
lado*lado
}

area.cuadrado(2)
area.cuadrado(10.5)
area.cuadrado(1:10)

#############################################

farenheit<-function(cent)
{
(5/9)*(cent-32)
}

farenheit(-10)
farenheit(68)

#############################################

prog1<-function(x)
	{
	f1 <- function(x){-x^2}
	plot(f1,min(x),max(x))
	X<-data.frame(x,f1(x))
	X
	}

z<-c(-10,-5,0,5,10)
prog1(z)

#############################################

prog2<-function(v,X)
{
# Este programa pre-multiplica un vector v de tamaño n por una matriz X 
# de con n filas.
	n<-length(v)
	v<-matrix(v,1,n)
	prod<-v%*%X
	prod
}

v<-c(1,2,3,4) 
A<-matrix(c(1,2,3),4,3,byrow=T)
prog2(v,A)


#############################################
# BUCLES
#############################################

#############################################
# IF
#############################################

acceso<-function(edad)
{
if (edad < 18)
 print("No puedes acceder.")
else
 print("Bienvenido.")
}

acceso(16)
acceso(18)

#############################################

area.cuadrado2<-function(lado)
{
if (lado < 0)
 print("El lado debe ser un valor positivo.")
else
lado*lado
}

area.cuadrado2(2)
area.cuadrado2(10.5)
area.cuadrado2(-2)

#############################################

areaoperimetro<-function(lado,valor=1)
{
if(lado < 0)
print("El lado debe ser un valor positivo.")
else{
if(valor==1) lado*lado
else 4*lado
}
}

areaoperimetro(2)
areaoperimetro(2,2)

#############################################

areaoperimetro2<-function(lado,valor=1)
{
if (lado < 0)
 print("El lado debe ser un valor positivo.")
else{
if (valor==1){
 resultado<-paste("El área vale: ",lado*lado,"cm cuadrados")
 resultado
}
else
{
 resultado<-paste("El perimetro vale: ",4*lado,"cm")
 resultado
}
}
}

areaoperimetro2(2)
areaoperimetro2(2,2)

#############################################

prog3<-function(v,X,pre=TRUE)
{
# Este programa pre-multiplica(pre=TRUE) o post-multiplica(pre=FALSE) un vector v de tamaño n por una matriz X 
# de con n filas (o n columnas, si se trata de post-multiplicación)
	n<-length(v)
	if(pre) 
		{
		v<-matrix(v,1,n)
		prod<-v%*%X
		prod
	}
	else
	{
	v<-matrix(v,n,1)
		prod<-X%*%v
		prod
	}

}

prog3(v,A)
u<-c(2,2,2)
prog3(u,A,pre=FALSE)

#############################################
# FOR
#############################################

sucesion1 <- function(n)
{
v <- rep(NA, n)
for( j in 1:n ){
v[j] <- (2*j+4)/j
}
v
}

sucesion1(10)

#############################################

sucesion2 <- function(n)
{
v <- NULL
for( j in 1:n ){
comp <- (2*j+4)/j
v<-cbind(v,comp)
}
plot(v[1,],xlab="Coordenada",ylab="Sucesión")
v
}

sucesion2(10)

#############################################

En algunas ocasiones, se puede evitar el uso de FOR:

sucesion3 <- function(n)
{
v <- 1:n
(2*v+4)/v
}

sucesion3(10)

#############################################

otrasucesion <- function(n)
{
v <- rep(NA, n-1)
v[1] <- 1
v[2] <- 2
for( j in 3:(n-1) ){
v[j] <- v[j-1] + 2/v[j-1]
}
v
}

otrasucesion(10)

#############################################

otrasucesion2 <- function(n)
{
v <- rep(NA, n-1)
v[1] <- 1
v[2] <- 2
for( j in 3:(n-1) ){
v[j] <- v[j-1] + 2/v[j-1]
}
plot(v)
}

otrasucesion2(10)


#############################################
# WHILE
#############################################

sumar <- function(n)
{
i<-1
suma<-0
while(i<=n){
suma<-suma+i
i<-i+1
}
suma
}

sumar1 <- function(i,n)
{
suma<-0
while(suma<=n){
suma<-suma+i
}
suma-i
}


sumar1(3,10)

#############################################

sumar2 <- function(n)
{
i<-1
vec<-NULL
suma<-0
while(i<=n){
suma<-suma+i
vec<-cbind(vec,suma)
i<-i+1
}
vec
}

sumar2(10)
sumar2(25)
