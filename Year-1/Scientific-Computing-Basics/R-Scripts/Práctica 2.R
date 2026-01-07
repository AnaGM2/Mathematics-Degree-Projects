########################################
#PRÁCTICA 2
########################################


#EJERCICIO 1
x<-1:10
y<-x^2
#APARTADO (a)
plot(x)														
#En el eje x aparecen números del 1 al 10 y en el eje y aparecen los valores del vector x
#APARTADO (b)
plot(y,pch=2)													
#En el eje x aparecen números del 1 al 10 y en el eje y aparecen los valores de y. El pch hace que los puntos tengan forma de triángulo
#APARTADO (c)
plot(x,y,pch=3)													
#En el eje x aparece x y en el eje y aparece y, y los puntos tienen la forma del más
#APARTADO (d)
plot(x,y,type="l")												
#En lugar de puntos aparece una línea
#APARTADO (e)
plot(x,y,type="o",col=3,lty=1)										
#Aparecen los puntos y la línea a la vez, y el color es verde
#APARTADO (f)
plot(x,y,type="p",col=4,lty=2,lwd=1)									
#Aparecen puntos azules
#APARTADO (g)
plot(x,y,type="s",col=5,lty=3,lwd=2,main="")								
#Aparecen unas escaleras azules discontinuas de mayor grosor
#APARTADO (h)
plot(x,y,type="h",col=6,lty=4,lwd=3,main="Gráfica",xlab="",ylab="")				
#Aparecen líneas verticales rosas, discontinuas y de mayor grosor, además de el nombre de la gráfica
#APARTADO (i)
plot(x,y,type="l",col=7,lty=5,lwd=4,main="Gráfica",xlab="Sucesión x",ylab="Sucesión y")	
#Los ejes tienen nombre
#pch= sirve para cambiar la forma de los puntos
#type= sirve para cambiar el tipo (puntos, líneas...)
#col= sirve para cambiar el color
#lty= sirve para cambiar el tipo de línea
#lwd= sirve para cambiar el grosor de la línea
#main= sirve para poner un nombre a la gráfica
#xlab= sirve para cambiar el nombre del eje x
#ylab= sirve para cambiar el nombre del eje y


#EJERCICIO 2
x<--4:4
y<-exp(x)
par(mfrow=c(1,2))
plot(x,y,type="b",lty=2,col=3,lwd=3,main="Gráfica de e^x",ylab="e^x")
plot(x,y,type="h",col="red",lwd=3,main="Gráfica de e^x",ylab="e^x")


#EJERCICIO 3
f<-function(x) log(x)/x
#APARTADO (a)
plot(f)																
#Se crea la gráfica de f
#APARTADO (b)
plot(f,type="b")															
#La gráfica está formada por líneas y puntos
#APARTADO (c)
plot(f,type="o",col=2,lty=2)													
#La gráfica es roja y las líneas son discontinuas
#APARTADO (d)
plot(f,type="p",col=4,lty=3,lwd=4)												
#R utiliza el dominio entre 0 y 1
#APARTADO (e)
plot(f,type="l",col=8,lty=6,lwd=5,main="Gráfica",xlab="x",ylab="f(x)",xlim=c(0,5))				
#Ahora el dominio es entre 0 y 5
#APARTADO (f)
plot(f,type="l",col=9,lty=7,lwd=6,main="Gráfica",xlab="x",ylab="f(x)",xlim=c(0,5),ylim=c(-20,20))	
#Toma los valores de y entre -20 y 20


#EJERCICIO 4
f<-function(x){sin(x)+cos(x)}
plot(f,0,6,lwd=4,col="cyan",main="sin(x)+cos(x)",ylab="y")
plot(f,-6,6,lwd=2,col="blue",lty=2,ylim=c(-2,2),main="sin(x)+cos(x)",ylab="y")
abline(h=0)		#Crea una línea horizontal en y=0
abline(v=1)		#Crea una línea vertical en x=1


#EJERCICIO 5
x<-seq(0,2*pi,length=100)
plot(cos)
plot(cos(x))
plot(x,cos(x))
#APARTADO (a)
#La primera gráfica representa el coseno entre el 0 y el 1 con una línea
#La segunda gráfica representa el coseno de x con 100 puntos con una separación de 1 entre cada punto
#La tercera gráfica representa el coseno de x entre 0 y 2*pi con 100 puntos
#APARTADO (b)
plot(cos,0,2*pi)
#APARTADO (c)
#La más adecuada es la tercera, ya que es la única que representa la función coseno en el intervalo dado


#EJERCICIO 6
#APARTADO (a)
x<-1:100
#APARTADO (b)
plot(1/x)


#EJERCICIO 7
x<-seq(from=0,to=1,length=50)		#Crea un vector con 50 elementos que van del 0 al 1 en intervalos iguales
y<-x^2					#Eleva el anterior vector al cuadrado
par(mfrow=c(1,2))				#Hace que las dos gráficas siguientes se sitúen una al lado de la otra
plot(x,y,type="l",col=2,lty=4,lwd=3,main="Gráfica")
plot(x,y,type="l",col=3,lty=7,lwd=6,main="Gráfica")
x<-seq(from=pi,to=2*pi,length=50)
f<-x*sin(x)
g<-sin(x)/x
par(mfrow=c(1,2))
plot(x,f,type="l",col=2,lty=4,lwd=3,main="Gráfica")
plot(x,g,type="l",col=3,lty=7,lwd=6,main="Gráfica")


#EJERCICIO 8
x<-seq(from=0,to=1,length=50)
y<-x^2
z<-x^3
plot(x,y,type="l",col=2,lty=4,lwd=3,main="Gráfica")
lines(x,z,type="l",col=3,lty=7,lwd=6,main="Gráfica")		#Hace que ambas gráficas aparezcan juntas una encima de la otra con los elementos de la primera
x<-seq(from=pi,to=2*pi,length=50)
f<-x*sin(x)
g<-sin(x)/x
plot(x,f,type="l",col=2,lty=4,lwd=3,main="xsin(x)",ylab="y")
lines(x,g,type="l",col=3,lty=7,lwd=6,main="sin(x)/x")


#EJERCICIO 9
x<-seq(from=0,to=1,length=50)
y<-x^2
z<-x^3
plot(x,y,type="l",col=2,lty=4,lwd=3,main="Gráfica")
par(new=TRUE)								#Hace que las gráficas se superpongan una encima de la otra y sus elementos se mezclen 
plot(x,y,type="l",col=3,lty=7,lwd=6,main="Gráfica")
x<-seq(from=pi,to=2*pi,length=50)
f<-x*sin(x)
g<-sin(x)/x
plot(x,f,type="l",col=2,lty=4,lwd=3,main="Gráfica",ylab="y")
par(new=TRUE)
plot(x,g,type="l",col=3,lty=7,lwd=6,main="Gráfica",ylab="y")


#EJERCICIO 10
f<-function(u){1+(1-u)^2}
plot(f,-10,10,ylim=c(-20,20),ylab="y")


#EJERCICIO 11
g1<-function(u){1+(1-u)^3}
g2<-function(u){1+(1-u)^-3}
#APARTADO (a)
plot(g1,-10,10,ylim=c(-20,20),ylab="g")
plot(g2,-10,10,ylim=c(-20,20),ylab="g")
#APARTADO (b)
par(mfrow=c(1,2))
plot(g1,-10,10,ylim=c(-20,20),ylab="g")
plot(g2,-10,10,ylim=c(-20,20),ylab="g")
#APARTADO (c)
plot(g1,-10,10,ylim=c(-20,20),ylab="g",col="red")
par(new=TRUE)
plot(g2,-10,10,ylim=c(-20,20),ylab="g",col="green")
#APARTADO (d)
legend("topleft",legend=c("a=3","a=-3"),col=c("red","green"),lty=c(1,1))


#EJERCICIO 12
f<-function(x){x/(x-1)}
plot(f,0,2)
abline(v=1)


#EJERCICIO 13
f<-function(x){2*exp(-2*x)}
plot(f,0,10)
abline(h=1)
title("Función de densidad de una distribución exponencial")


#EJERCICIO 14
f1<-function(x){
if(x>=5){
print("x es mayor que 5")}
else{
print("x es menor que 5")}}
#APARTADO (a)
f1(1)
f1(6)
#APARTADO (b)
f2<-function(x){
if(x>0){
print("El valor de x es positivo")}
if(x==0){
print("x=0")}
if(x<0){
print("El valor de x es negativo")}}
f2(1)
f2(0)
f2(-1)


#EJERCICIO 15
ejemplo=function(x){
suma=sum(x)
resultado=ifelse(suma<100,TRUE,FALSE)
return(resultado)
}
#APARTADO (a)
ejemplo(-100)
ejemplo(c(0,99,30))
ejemplo(1)
ejemplo(100)
#APARTADO (b)
f<-function(x){
suma<-sum(x)
resultado<-ifelse(suma<50,TRUE,FALSE)
return(resultado)
}
f(c(2,1))
f(c(20,81))
f(c(16,36))
g<-function(x){
suma<-sum(x)
if(suma<50){
return(TRUE)}
else{
return(FALSE)}
}
g(c(1,30))
g(c(47,18))


#EJERCICIO 16
x1<-rep(c(1,2),20)
x2<-1:40
vectores<-function(x){
if(x==1){
print(x1*x2)}
if(x==2){
print(t(x1)%*%x2)}
if(x==3){
print(x1%*%t(x2))}
}
vectores(1)
vectores(2)
vectores(3)


#EJERCICIO 17
x<-c(1:5)
for(i in 1:length(x)){
cat('El cuadrado de',i,'es:',i^2,'\n')
}
x=1
while(x<=10){
cat('El cuadrado de',x,'es:',x^2,'\n')
x=x+1
}
#APARTADO (a)
#La primera muestra el cuadrado de los números del 1 al 5
#la segunda muestra el cuadrado de los números del 1 al 10
#APARTADO (b)
x<-c(2,7,1,19,4,0)
for (i in x){
cat('El cuadrado de',i,'es:',i^2,'\n')
}
#APARTADO (c)
x=48
while(x>1){
cat('El cuadrado de',x-1,'es:',(x-1)^2,'\n')
x=x-1
}