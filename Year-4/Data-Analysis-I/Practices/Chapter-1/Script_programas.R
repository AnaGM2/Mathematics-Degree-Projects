######################################################
######   ANÁLISIS DE DATOS. REPASO PROGRAMAS   #######
######   María J. Nueda Roldán
######   Septiembre 2017
  

#######################################################
### Ejemplo 1
#######################################################

ec.grado2 <- function(a, b, c)
{
# Este programa calcula las soluciones de una ecuación de segundo grado

	disc <- (b^2)-(4*a*c)
	sol1 <- (-b - sqrt(disc))/(2*a)
	sol2 <- (-b + sqrt(disc))/(2*a)

# Devolvemos un vector con las dos soluciones 
	SOL <- c(sol1,sol2)
	SOL
}


ec.grado2(1,3,-4)


#######################################################
### Ejemplo 2: Añadimos un gráfico
#######################################################

ec.grado2 <- function(a, b, c)
{
# Este programa calcula las soluciones de una ecuación de segundo grado

	disc <- (b^2)-(4*a*c)
	sol1 <- (-b - sqrt(disc))/(2*a)
	sol2 <- (-b + sqrt(disc))/(2*a)
	
	f1 <- function(x){a*x^2+b*x+c}
	plot(f1, sol1-1, sol2+1)

# Devolvemos un vector con las dos soluciones 

	SOL <- c(sol1,sol2)
	SOL
}

ec.grado2(1,3,-4)
ec.grado2(2,-2,1)

#######################################################
### Ejemplo 3: Corregimos posibles errores
#######################################################
ec.grado2 <- function(a, b, c)
{
# Este programa calcula las soluciones de una ecuación de segundo grado
	
	f1 <- function(x){a*x^2+b*x+c}
	vertice<- (-b/(2*a))
	disc <- (b^2)-(4*a*c)

if(disc<0){
	SOL <- c("NA","NA",vertice,f1(vertice))	
	plot(f1 , vertice-5, vertice+5 , main="Ecuación 2º grado")
	abline(h=0,v=vertice, col=2)
	
}
else{	
	sol1 <- (-b - sqrt(disc))/(2*a)
	sol2 <- (-b + sqrt(disc))/(2*a)
	SOL <- c(sol1, sol2,vertice,f1(vertice))		
	plot(f1 , sol1-2, sol2+2 , main="Ecuación 2º grado")
	abline(h=0,v=vertice, col=2)
}
# Devolvemos un vector con las dos soluciones 
	
	names(SOL) <- c("sol1","sol2","vértice","f(vértice)")
	SOL
}

ec.grado2(4,-3,-1)
ec.grado2(4,-3,1)

#######################################################
### Ejemplo 4: Programa que genera los n primeros números de la sucesión (2n+4)/n 
#######################################################
 
# Opción A: usando for() e inicializando todos los valores

suceA <- function(n)
{
  v <- NULL
  for( i in 1:n ){
    v[i] <- (2*i+4)/i
  }
  v
}

# Opción B: usando for() e inicializando solo el primer valor

suceB <- function(n)
{
  v <- (2*1+4)/1
  for( i in 2:n ){
    v <- c(v,(2*i+4)/i)
  }
  v
}

# Opción C: también se puede usar while()

suceC <- function(n)
{
  i<-1
  v <- NULL
  while( i<=n ){
    v <- c(v,(2*i+4)/i)
    i<-i+1
  }
  v
}

suceA(10)
suceB(10)
suceC(10)


#######################################################
### Ejemplo 5: Programa que centra matrices
#######################################################

center<-function(X)
{
	X<-as.matrix(X)
	n<-nrow(X)
	medias<-apply(X,2,mean)
	Xc<-X-(matrix(1,n,1)%*%medias)
	Xc
}

center(iris[,1:4])

#######################################################
### Ejemplo 6: Programa que estandariza matrices
#######################################################

stand<-function(X)
{
	X<-as.matrix(X)
	n<-nrow(X)
	medias<-apply(X,2,mean)
	des<-apply(X,2,sd)
	des<-sqrt(des^2*(n-1)/n)
	Xc<-X-(matrix(1,n,1)%*%medias)
	Xs<-Xc%*%diag(1/des)
	Xs
}

stand(iris[,1:4])

# NOTA: Si tenemos el programa en un archivo:
source("stand")
