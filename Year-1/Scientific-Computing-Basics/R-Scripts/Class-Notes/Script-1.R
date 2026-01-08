#############################################
# PROGRAMAS DE CALCULO CIENTIFICO Y PROCESAMIENTO DE TEXTOS
#############################################

#############################################
# Primeras pruebas
#############################################

x<-10
x=10
y<-2
z<-x*y
N<-"nombre"

ls()

##Vectores: 

v<-c(2,4,6,8,10)
Nombre<-c("Jose","Pepe","Alex")

v1<-c(1:10)
v2<-rep(2,5)
v3<-c(v,v1,v2)
v4<-rep(c(1,2),4)
v5<-rep(c(1,2),each=4)		
sec1<-seq(from=2,length=5,by=2)
sec2<-seq(from=2,to=4,length=5)

ls()

##Matrix:

A<-matrix(c(1,2,3,4,5,6),2,3) 
A2<-matrix(c(1,2,3,4,5,6),2,3,byrow=TRUE)
B<-matrix(2,2,3)
fix(A)

##Data.frame:

X <- data.frame(c(1,2,3,4), c("uno", "dos", "tres", "cuatro"))
data()
data(iris)
fix(iris)


##Lista de objetos:

L<-list(v,A,X)

################################################
#  Atributos de los objetos
################################################

class(v)
class(iris)
class(A)
ls.str()

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

DATA<-read.table("DATA.txt",header=T,dec=",")
fix(DATA)               
class(DATA)

#También se puede cargar un archivo de EXCEL en formato csv


###############################################
# EXPORTAR DATOS
###############################################

write.table(A,file="A.txt")

##############################################
# Operaciones con vectores
##############################################

v
v1
v2

length(v)
length(v1)
length(v2)
v+v2
v+v1
2+v
v*v2 

sqrt(v)
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
A
A2
B

dim(A)
dim(A2)
dim(B)

t(A)
A+A2
A*A2
A%*%A2 #error
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




