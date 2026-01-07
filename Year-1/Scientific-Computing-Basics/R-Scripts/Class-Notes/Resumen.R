#VECTORES

#Vector numérico
v<-c(1,2,3)

#Vector carácter
n<-c("hola","adios")

#Vector con números del 1 al 10
w<-c(1:10)

#Repite el 2; 10 veces
r<-rep(2,10)

#Repite el 1, 2, 3; 6 veces
z<-rep(c(1,2,3),6)

#Repite el 1, 2, 3; 4 veces cada uno
q<-rep(c(1,2,3),each=4)

#Del 0 al 10 de 2 en 2
s<-seq(from=0,to=10,by=2)

#Del 2 al 10 dividido en 6 partes iguales
t<-seq(from=2,to=10,length=6)

#Para saber el tamaño de un vector
length(r)

#Para saber el elemento de la posición 4 de w
w[4]

#Para saber los elementos de las posiciones 4, 5 y 6 de w
w[c(4,5,6)]
w[4:6]

#Para saber si dos vectores son iguales
v==w


#MATRICES

#Matriz de 2 filas y 4 columnas
A<-matrix(c(1,2,3,4,5,6,7,8),2,4)

#Matrix de 2 filas y 4 columnas con los números ordenados
B<-matrix(c(1,2,3,4,5,6,7,8),2,4,byrow=TRUE)

#Matriz de 2 filas y 3 columnas compuesta por el número 9
C<-matrix(9,2,3)

#Matriz de 5 filas y 2 columnas compuesta por las letras a y b
D<-matrix(c("a","b"),5,2)

#Para editar la matriz A
fix(A)

#Para saber las dimensiones de una matriz
dim(A)

#Para saber el número de filas de una matriz
nrow(A)

#Para saber el número de columnas de una matriz
ncol(A)

#Inversa de una matriz
E<-matrix(c(4,5,2,6),2,2)
solve(E)


#DATA.FRAME

#Data.frame formado por 2 números
F<-data.frame(1,2)

#Data.frame formado por 2 vectores
X<-data.frame(c(1,2,3,4),c(5,6,7,8))

#Editar data.frame
fix(X)

#Lista de sets de datos que hay en el sistema
data()

#Abrir datos del sistema
iris
swiss

#Editar datos del sistema
fix(iris)

#Para saber las dimensiones de un data.frame
dim(iris)

#Para saber el número de filas de un data.frame
nrow(iris)

#Para saber el número de columnas de un data.frame
ncol(iris)

#Para saber el nombre de las columnas
colnames(iris)

#Para saber el nombre de las filas
rownames(iris)

#Para cambiar el nombre de las columnas
colnames(X)<-c("HOLA","ADIÓS")

#Muestra la primera columna en vertical
iris[,1]

#Muestra la primera fila
iris[1,]

#Muestra las tres primeras columnas
iris[,1:3]

#Muestra las tres primeras filas
iris[1:3,]

#Muestra una columna en horizontal
X$HOLA


#LISTAS

#Lista con números y letras
L<-list("Uno",2,"Tres",4)


#FUNCIONES

#Función con dos variables
f<-function(x,y){x^y}

#Dar valores y resolver
f(2,3)


#OTROS

#Para saber el tipo de objeto
mode(v)
class(n)

#Lista de objetos guardados
ls()


#PROGRAMACIÓN
diHola<-function(){
"hola"
}
diHola()


#FUNCIÓN A TROZOS
trozos<-function(x){
ifelse((x<=-1),-x+2,
ifelse((x>=0 & x<3),x^2-1,
ifelse((x>4),-1,NA)))
}
plot(trozos,xlim=c(-7,6),ylim=c(-1,8))


a <- function(x){ 
  ifelse(( x < 1),x^2-1,ifelse((1<x & x<2),x^3-5, ifelse((x>2.1),5 - 2*x, NA))) 
} 
plot(a,xlim=c(-3,5), ylim = c(-4, 7), col = "red") 
abline(v = 0, h = 0)

