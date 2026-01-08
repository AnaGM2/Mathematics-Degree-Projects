########################################
#PRÁCTICA 1
########################################


#EJERCICIO 1
a<-1
b<-pi
c<-"hola"
d<-TRUE
e<-FALSE
x<-c(1,2)
y<-c(1,2,"yo",3)
#APARTADO (i)
class(a)		#Numérico
class(b)		#Numérico
class(c)		#Carácter
class(d)		#Lógico
class(e)		#Lógico
class(x)		#Numérico
class(y)		#Carácter
#APARTADO (ii)
a+b		#Suma, 4.141593
b^a		#Potencia, 3.141593
a+d		#Suma 1 a a, 2
a+e		#Suma 0 a a, 1
x+b		#Suma componente a componente, (4.141593,5.141593)
x+d		#Suma 1 a cada componente del vector, (2,3)
y+a		#Error porque y no es numérico
y+b		#Error porque y no es numérico
a<a		#Falso porque a=a
a<=a		#Verdadero porque a=a, y pide que sea menor o igual
a<b		#Verdadero
a<x		#Con la primera componente es falso y con la segunda es verdadero


#EJERCICIO 2
x<-c(1,2,3,4,5,6)
y<-c(7,8)
z<-c(9,10,11,12)
x+x		#Suma componente a componente, (2,4,6,8,10,12)
x+y		#Como no tienen el mismo número de componentes, y se repite, (8,10,10,12,12,14)
x+z		#Aparece una advertencia ya que la longitud de x no es múltiplo de la de z, (10,12,14,16,14,16)
2*x		#Multiplica componente a componente, (2,4,6,8,10,12)
x^2		#Eleva componente a componente, (1,4,9,16,25,36)
x^y		#La primera componente de x la eleva a 7, la segunda a 8, la tercera a 7, la cuarta a 8..., (1,256,2187,65536,78125,1679616)
x*x		#Multiplica componente a componente, (1,4,9,16,25,36)
x*y		#Multiplica componente a componente y, como no tienen el mismo número de componentes, y se repite, (7,16,21,32,35,48)
x*z		#Aparece una advertencia ya que la longitud de x no es múltiplo de la de z, (9,20,33,48,45,60)
exp(x)	#Calcula e elevado a cada componente de x, (2.718282,7.389056,20.085537,54.598150,148.413159,403.428793)
length(x)	#Dice la longitud de x, que es 6
sum(x)	#Suma las componentes entre sí, 21
cumsum(x)	#En la primera componente pone 1, en la segunda pone 1+2, en la tercera 1+2+3, en la cuarta 1+2+3+4..., (1,3,6,10,15,21)


#EJERCICIO 3
a<-c(10:13)
b<-rep(0.5,12)
c<-c(a,b)
d<-a+b
e<-rep(a,3)
f<-rep(a,each=2)
g<-c(9:6)
h<-seq(from=1.35,to=1.8,length=4)
i<-seq(from=0,to=2,length=7)


#EJERCICIO 4
u<-seq(from=1,to=7.5,by=0.5)
length(u)				#Dice la longitud de u, que es 14
u[c(1,14)]				#Muestra la primera y la última componente, que son 1 y 7.5
u[1:3]				#Muestra las tres primeras componentes, que son 1, 1.5 y 2
u[seq(from=4,to=2,by=-1)]	#Muestra las componentes 2.5, 2 y 1.5
u[u>=3]				#Muestra las componentes mayores o iguales que 3, que son 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7 y 7.5
u[rep(c(1,2),3)]			#Muestra las dos primeras componentes 3 veces
u[seq(from=1,to=13,by=3)]	#Muestra las componentes de la 1 a la 13 de 3 en 3


#EJERCICIO 5
v<-c(2,-1,3,5,-6,-8)
#APARTADO (i)
sort(v)		#Ordena los números de menor a mayor, (-8,-6,-1,2,3,5)
order(v)		#Ordena las componentes de menor a mayor, (6,5,2,1,3,4)
rank(v)		#Da un vector con el rango de los valores de v, de manera que el -8, al ser el menor, sería un 1, el -6 un 2, el -1 un 3..., (4,3,5,6,2,1)
#APARTADO (ii)
v1<-c(v[6],v[2:4])
v2<-c(v[1],v[3:4])
v3<-c(v[seq(from=2,length=3,by=2)])


#EJERCICIO 6
chicos<-c("Jose","Luis","Alberto","Lucas")	#El objeto chicos es un vector de tipo carácter


#EJERCICIO 7
x<-c(1,2,3,4,5,6)
m1<-matrix(x,2,3)
m2<-matrix(x,3,2)
m3<-matrix(x,2,3,byrow=TRUE)
m4<-matrix(x,3,2,byrow=TRUE)


#EJERCICIO 8
v<-c(2,0,-6,8,1,-5)
A<-matrix(v,2,3,byrow=TRUE)
B<-matrix(v,3,2)
C<-matrix(v,2,3)
D<-matrix(v,3,2,byrow=TRUE)


#EJERCICIO 9
M<-matrix(c(2,0,-6,8,1,-5),2,3,byrow=TRUE)
m<-matrix(c(1,0,3),1,3)
n<-matrix(c(1,2),2,1)
#APARTADO (i)
R<-cbind(M,n)
S<-rbind(M,m)
#APARTADO (ii)
apply(R,1,sum)
#APARTADO (iii)
apply(S,1,mean)
#APARTADO (iv)
v<-R[1,]
#APARTADO (v)
w<-S[,2]
#APARTADO (vi)
x<-S[2,3]


#EJERCICIO 10
A<-matrix(c(-6:-1),2,3)
B<-matrix(c(10:21),3,4)
C<-matrix(c(6:1),2,3)
A*C			#Multiplica elemento a elemento
outer(A,B)		#Multiplica la matriz A por cada uno de los elementos de B, formándose 12 matrices diferentes
A+2			#Suma 2 a cada uno de los elementos de A
A%*%B			#Por cada elemento Cij de la matriz producto multiplica cada elemento de la fila i de la matriz A por cada elemento de la columna j de la matriz B y suma
exp(A)		#Calcula e elevado a cada elemento de A
A*B			#Da error porque tienen distintas dimensiones
A^2			#Eleva cada elemento de A al cuadrado
t(A)			#Hace la traspuesta de A
A[2,3]		#Muestra el elemento que se encuentra en la fila 2 y en la columna 3 de A
A[2,]			#Muestra la segunda fila de A
A[,1]			#Muestra la primera columna de A
A[,c(1,3)]		#Muestra la primera y la tercera columna de A
A[,c(-1)]		#Muestra todas las columnas de A menos la primera


#EJERCICIO 11
M<-matrix(c(1,1,3,-2,-2,0,1,2,1),3,3)
#APARTADO (a)
class(M)		#Es de tipo matriz
#APARTADO (b)
M[-3,-3]
#APARTADO (c)
A<-M[-3,-1]
class(A)		#Es de tipo matriz
#APARTADO (d)
b<-M[-3,3]
class(b)		#Es de tipo vector numérico
#APARTADO (e)
t(A)
#APARTADO (f)
solve(t(A),b)
#APARTADO (g)
b2<-matrix(c(b,3,4),2,2)
#APARTADO (h)
b+b2			#Se suma b a cada una de las columnas de b2


#EJERCICIO 12
data()		#Habre una lista de sets de datos que hay en el sistema
data(cars)		#Guarda el set de datos llamado cars para poder abrirlo
cars			#Abre un data.frame llamadon cars
#APARTADO (a)
class(cars)		#Es de tipo data.frame
#APARTADO (b)
colnames(cars)	#Contiene las variables speed y dist
#APARTADO (c)
nrow(cars)		#Contiene 50 filas
#Apartado (d)
cars[,2]		#Muestra los elementos de la segunda columna
cars$dist		#Muestra los elementos de la columna dist
cars[50,]		#Muestra los elementos de la fila 50
cars[1:5,]		#Muestra los elementos de la fila 1 a la 5


#EJERCICIO 13
u<-c(19,23,18,20,15,17,21,22,18,19,23,22,16,19,20,20,18,17,22,24)
v<-c(60,76,82,103,54,68,49,55,98,68,64,87,77,59,83,57,73,64,79,54)
w<-c(1.9,1.64,1.82,1.7,1.68,1.59,1.92,1.76,1.67,1.63,1.87,1.56,1.69,1.72,1.83,1.7,1.63,1.82,1.59,1.7)
#APARTADO (a)
datos1<-data.frame(u,v)
colnames(datos1)<-c("Edad","Peso")
#APARTADO (b)
datos2<-data.frame(u,w)
colnames(datos2)<-c("Edad","Altura")
#APARTADO (c)
datos1+datos2
#APARTADO (d)
datos1*datos2


#EJERCICIO 14
#Definimos la función que convierte de cm a m
f<-function(x){
x/100
}
#Comprobamos
f(250)


#EJERCICIO 15
#Definimos la función que convierte de cm a m si x es positiva
g<-function(x){
if(x>0){
y<-x/100
y
}else{
print("La cantidad de centímetros debe ser positiva")
}
}
#Comprobamos con un valor positivo
g(100)
#Comprobamos con valores no positivos
g(0)
g(-10)


#EJERCICIO 16
#Definimos la función
h<-function(x){
if(x>0){
y=x/100
paste("El argumento",x,"cm son",y,"metros")
}else{
print("La cantidad de centímetros debe ser positiva")
}
}
#Comprobamos
h(10.5)
h(-20)
