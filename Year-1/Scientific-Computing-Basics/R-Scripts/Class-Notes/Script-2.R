#############################################
# PROGRAMAS DE CÃLCULO CIENTÃFICO Y PROCESAMIENTO DE TEXTOS
#############################################

#############################################
# GrÃ¡ficos  
#############################################

#### Ejemplo 1:
u<-c(2,4,6,8,10)
plot(u)
v<-c(1,2,3,2,1)
plot(u,v)
plot(u,v,col=2)
plot(u,v,col=2,pch=5)
plot(u,v,col=2,pch=5,type="l")
plot(u,v,col=2,pch=5,main="Mi gr?fico",xlab="Abscisas",ylab="Ordenadas")

# AÃ±adimos detalles:
plot(u,v)
lines(u,v,col=2)
title("Mi gráfico")
abline(h=2,col=3)
abline(v=6,col=4)

# Varios grÃ¡ficos en uno:
par(mfrow=c(1,2))
plot(u,v,col=4,main="Puntos azules")
plot(u,v,col=2,type="l",main="Lineas rojas")

### Ejemplo 2:
DATA<-read.table("DATA.txt",header=T,dec=",")
colnames(DATA)
plot(DATA$ALTURA)
plot(DATA$ALTURA,DATA$PESO,xlab="ALTURA",ylab="PESO")
plot(DATA)

### RepresentaciÃ³n grÃ¡fica de una funciÃ³n matem?tica existente en R
plot(sin, -pi, 2*pi)
plot(log,0,10)

### RepresentaciÃ³n grÃ¡fica de una funciÃ³n matemÃ¡tica creada por nosotros
f1<-function(x){-x^2}
plot(f1,0,10)
plot(f1,-10,10)

x<-seq(from=0,to=2*pi,length=100)
plot(x,sin(x))
plot(x,sin(x),type="l")
plot(x,sin(x),type="b")


# Otra funciÃ³n para construir grÃ¡ficas es curve:

curve(sin,xlim=c(0,2*pi))
curve(sin,xlim=c(0,2*pi),col=2,main="sin(x)",xlab="Variable independiente")

# Cuatro gráficos juntos:

par(mfrow=c(2,2))
curve(sin,xlim=c(0,2*pi))
curve(f1,xlim=c(0,10))
curve(cos,xlim=c(0,2*pi))
curve(exp,xlim=c(0,10))

par(mfrow=c(2,2))
plot(v,u,col=2,type="b",main="Lineas rojas")
plot(DATA$ALTURA,DATA$PESO,xlab="ALTURA",ylab="PESO",main="RelaciÃ³n Altura-Peso")
plot(sin, -pi, 2*pi,col=6,main="seno(x)")
plot(f1,-10,10,col="Blue",main="-x^2")


# Cuatro gráficos juntos en un archivo png:
png("grafico.png")   
par(mfrow=c(2,2))
plot(v,u,col=2,type="b",main="Lineas rojas")
plot(DATA$ALTURA,DATA$PESO,xlab="ALTURA",ylab="PESO",main="RelaciÃ³n Altura-Peso")
plot(sin, -pi, 2*pi,col=6,main="seno(x)")
plot(f1,-10,10,col="Blue",main="-x^2")
dev.off()


# AtenciÃ³n a este cÃ³digo, Â¿nos podrÃ­a servir para pintar una funciÃ³n a trozos?

x<-seq(from=0,to=2*pi,length=100)
plot(x,sin(x),type="l")
par(new=TRUE)
plot(x,cos(x),type="l")

curve(sin,xlim=c(0,2*pi))
par(new=TRUE)
curve(cos,xlim=c(0,2*pi))

#############################################
# ProgramaciÃ³n  
#############################################

f<-function(variables){
  instrucciones
}

if y else

for

while

sample(1:10,1)

sumandos<-function(v){
n<-length(v)
suma<-0
k<-0
while(suma<100){
i<-sample(1:n,1)
print(i)
suma<-suma+v[i]
k<-k+1
}
return(k)
}

sumandos(c(1,2,3))




