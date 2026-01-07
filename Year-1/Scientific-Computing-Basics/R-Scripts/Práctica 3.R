########################################
#PRÁCTICA 3
########################################


#EJERCICIO 1
f<-function(a,b){
a+b
}
f(1,-2)


#EJERCICIO 2
suma<-function(a,b){
sum<-a+b
cat("La suma de",a,"y",b,"vale",sum,"\n")
}
suma(3,5)


#EJERCICIO 3
g<-function(a,b){
suma<-a+b
potencia<-a^b
cat(suma,",",potencia,"\n")
}
g(2,3)


#EJERCICIO 4
h<-function(a,b){
potencia<-a^b
división<-(a^b)/(a-b)
if(a!=b){
 cat(potencia,",",división,"\n")
}
else{
 print("Los números no pueden ser iguales.")
}
}
h(3,3)
h(1,3)


#EJERCICIO 5
i<-function(o,a,b){
opción.1<-a+b
opción.2<-a*b
opción.3<-a^b
if(o==1){
 cat(opción.1,"\n")
}
else if(o==2){
 cat(opción.2,"\n")
}
else if(o==3){
 cat(opción.3,"\n")
}
else{
 cat("Error","\n")
}
}
i(1,2,3)
i(2,2,3)
i(3,2,3)
i(4,2,3)


#EJERCICIO 6
mayores.que<-function(x,v){
w<-which(v>x)
length(w)
}
mayores.que(3,c(3,6,8,0,1,6,-1,10))


#EJERCICIO 7
j<-function(A,k){
if(k<=ncol(A)){
 sum(A[,k])
}
else{
 cat("Error","\n")
}
}
j(matrix(c(2,3,4,5,4,2,5,6,7,3,5,6),3,4),2)
j(matrix(c(2,3,4,5,4,2,5,6,7,3,5,6),3,4),10)


#EJERCICIO 8
sumas.acumuladas<-function(k){
if(k>=1){
 x<-1
 z<-3
 while(length(x)<k){
  x<-c(x,length(x)+1)
  y<-sum(2*x[]+1)
  z<-c(z,y)
 }
 cat(z,"\n")
}
else{
 cat("Error","\n")
}
}
sumas.acumuladas(3)


#EJERCICIO 9
factorial<-function(x){
if(x%%1==0){
 if(x>=0){
  y<-1
  for(i in 1:x){
   y=y*i
  }
  cat(y,"\n")
 }
 else{
  cat("Error","\n")
 }
}
else{
 cat("Error","\n")
}
}
factorial(6)
factorial(-1)
factorial(1.4)


#EJERCICIO 10
k<-function(x,M){
n<-1
s<-0
v<-c()
while(s<M){
 s<-s+x[n]
 v<-c(v,x[n])
 n<-n+1
 if(n>length(x)){
  break
 }
}
print(s)
print(v)
}
k(c(1,3,2,39,3,15,2),35)


#EJERCICIO 11
migrafico<-function(x,y){
f<-function(n){sin(n)}
plot(f,-4,4,col=x,xlab="x",ylab="sin",main=paste("migrafico(sin,",x,",",y,")"))
abline(h=y)
}
migrafico(4,-0.5)
migrafico(3,0)


#EJERCICIO 12
#Sin bucles
sin.bucles<-function(n){
v<-1:n
x<-(1+(1/v))^v
return(x)
}
sin.bucles(4)
#Con el bucle for
con.for<-function(n){
v<-1:n
w<-c()
for(i in v){
 x<-(1+(1/i))^i
  w<-c(w,x)
}
return(w)
}
con.for(4)
#Con el bucle while
con.while<-function(n){
v<-1:n
w<-c()
while(length(w)<n){
 x<-(1+(1/v))^v
 w<-c(w,x)
}
return(w)
}
con.while(4)