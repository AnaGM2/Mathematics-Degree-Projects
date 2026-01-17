#############################################
# INTRODUCCIÓN A R
# MARÍA J. NUEDA ROLDÁN
# FEBRERO 2011
#############################################

#############################################
# Primeras pruebas
#############################################

x<-10
y<-2
z<-x*y
N<-"nombre"
ls()

##Vectores: 

v<-c(2,4,6,8,10)
Nombre<-c("María","Pepe","Alex")

v1<-c(1:10)
v2<-rep(2,5)
v3<-c(v,v1,v2)
v4<-rep(c(1,2),4)
v5<-rep(c(1,2),each=4)		
sec<-seq(from=2,length=5,by=2)

ls()

## matrix:

A<-matrix(c(1,2,3,4,5,6),2,3) 
A2<-matrix(c(1,2,3,4,5,6),2,3,byrow=TRUE)
B<-matrix(2,2,3)
fix(A)

## data.frame:

X <- data.frame(c(1,2,3,4), c("uno", "dos", "tres", "cuatro"))
data()
data(iris)
fix(iris)

## lista de objetos:

L<-list(v,A,X)

################################################
#  Atributos de los objetos
################################################

class(v)
class(iris)
class(A)

length(v)
dim(iris)
nrow(iris)
ncol(iris)

colnames(iris) 
rownames(iris) 
colnames(A)<-c("a","b","c")
rownames(A)<-c("fila1","fila2")
 
iris[,1]  
iris$Sepal.Length 
iris[2,]  
iris[1:3,] 

###############################################
# IMPORTAR DATOS
###############################################

DATA<-read.table("DATA.txt") # no lee bien los datos

DATA<-read.table("DATA.txt",header=T)
fix(DATA)               
class(DATA)

###############################################
# EXPORTAR DATOS
###############################################

write.table(A,file="A.txt")

##############################################
# Operaciones con vectores
##############################################
length(v)
length(v1)
length(v2)
v+v2
v+v1
2+v
v*v2 

sum(v)
cumsum(v)
prod(v)
cumprod(v)
mean(v)
sort(v)
order(v)
?sin
sin(v)

#############################################
# Operaciones con matrices
#############################################
dim(A)
dim(A2)
dim(B)

t(A)
A+A2
A*A2
A%*%A2 #dará error
A%*%t(A2)

#############################################
# Sistema de ecuaciones: Dx=d
#############################################
D<-matrix(c(3,5,1,-1),2,2)
d<-c(11,13)
solve(D,d)

#############################################
# Otras operaciones con matrices 
#############################################
cbind(A,B)
rbind(A,B)

apply(A,1,sum)
apply(A,2,sum)

#############################################

iris2<-iris[,1:4]
mean(iris2[,1])
apply(iris2,1,mean)
apply(iris2,2,mean)
apply(iris2,2,function(x){sd(x)/mean(x)})
tapply(iris2[,1],iris$Species,mean)
apply(iris2,2,function(x){tapply(x,iris$Species,mean)})

#############################################

#############################################
# Gráficos  
#############################################

#### Ejemplo 1:
v<-c(2,4,6,8,10)
plot(v)
u<-c(1,2,3,2,1)
plot(v,u)
plot(v,u,col=2)
plot(v,u,col=2,pch=5)
plot(v,u,col=2,pch=5,type="b")
plot(v,u,col=2,pch=5,main="Mi gráfico",xlab="Abscisas",ylab="Ordenadas")

# Añadimos detalles:
plot(v,u)
lines(v,u,col=2)
title("Mi gráfico")
abline(h=2,col=3)
abline(v=6,col=4)

# Varios gráficos en uno:
par(mfrow=c(1,2))
plot(v,u,col=4,main="Puntos azules")
plot(v,u,col=2,type="l",main="Lineas rojas")

### Ejemplo 2:
datos<-read.table("DATA.txt",header=T)
colnames(datos)
plot(datos$ALTURA)
plot(datos$ALTURA,datos$PESO,xlab="ALTURA",ylab="PESO")
plot(datos)

### Representación gráfica de una función matemática existente en R
plot(sin, -pi, 2*pi)
plot(log,0,10)
### Representación gráfica de una función matemática creada por nosotros
f1<-function(x){-x^2}
plot(f1,0,10)
plot(f1,-10,10)

# 4 gráficos juntos en un archivo pdf:
pdf("grafico.pdf")   
par(mfrow=c(2,2))
plot(v,u,col=2,type="b",main="Lineas rojas")
plot(datos$ALTURA,datos$PESO,xlab="ALTURA",ylab="PESO",main="Relación Altura-Peso")
plot(sin, -pi, 2*pi,col=6,main="seno(x)")
plot(f1,-10,10,col="Blue",main="-x^2")
dev.off()

#############################################