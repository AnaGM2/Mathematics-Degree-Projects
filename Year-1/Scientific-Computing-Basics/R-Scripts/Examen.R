#EJERCICIO 1
a <- seq(from=0,to=4,length=7)
b <- rep(c(0.5,0),3)
A <- matrix(c(3,-2,1,2,3,-2,4,-1,1),3,3,byrow=TRUE)
B <- matrix(c(2,-1,3,0,1,2,-2,2,3),3,3,byrow=TRUE)
#La primera operación es la multiplicación elemento a elemento de ambas matrices
A*B
#La segunda operación es la suma de las matrices
A+B
#La última operación es la multiplicación típica de matrices
A%*%B




#EJERCICIO 2
data(quakes)

#Apartado a)

#Definimos una función que calcule la media que se pide
profundidad.500 <- function(){
x <- quakes[,3]
v <- c()
y <- which(x>=500)
for(i in y){
 z <- quakes[i,4]
 v <- c(v,z)
}
mean(v)
}

#La siguiente instrucción calcula la media
profundidad.500()

#Apartado b)

#Definimos una función que calcule la media pedida
estación.33 <- function(){
x <- quakes[,5]
v <- c()
y <- which(x==33)
for(i in y){
 z <- quakes[i,4]
 v <- c(v,z)
}
mean(v)
}

#La media la obtenemos con la siguiente instrucción
estación.33()




#EJERCICIO 3

#Creamos la función que representará la figura
gráfica <- function(){
plot(sin,0,6,xlab="",ylab="",main="Seno y Coseno",col="green",lwd=3,lty=2)
par(new=TRUE)
plot(cos,0,6,xlab="",ylab="",col="blue")
}

#Obtenemos la figura con la siguiente instrucción
gráfica()



#EJERCICIO 4

#Primera función
cuenta <- function(u,v){
w <- c()
x <- c()
for(i in u){
 for(j in v){
  m <- i*j
  w <- c(w,m)
 }
}
for(k in w){
 if(k<0){
  x <- c(x,k)
 }
}
x
}

#Damos valores
cuenta(c(-1,0,2),c(2,-1))
cuenta(c(2,3),c(1,-2))
cuenta(c(-1,2,3,-2),c(1,2))

#Segunda función
cuenta2 <- function(u,v,k){
w <- c()
x <- c()
for(i in u){
 for(j in v){
  m <- i*j
  w <- c(w,m)
 }
}
for(p in w){
 if(p<k){
  x <- c(x,p)
 }
}
x
}

#Damos valores
cuenta2(c(-1,0,2),c(2,-1),3)
cuenta2(c(-1,-4,-2),c(3,-1),2)
