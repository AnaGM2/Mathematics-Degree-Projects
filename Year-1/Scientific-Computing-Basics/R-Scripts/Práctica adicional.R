########################################
#PRÁCTICA ADICIONAL
########################################


#EJERCICIO 1
f<-function(p,c){
n<-0
while(p>c){
 p<-p-(5*p)/100
 n<-n+1
}
cat('Habrá que esperar',n,'semanas y el precio final será de',p,'euros.\n')
}
f(200,140)


#EJERCICIO 2
g<-function(n){
impar<--1
suma<-0
v<-1:sum(1:n)
for(i in v){
 impar<-impar+2
 if(i>(length(v)-n)){
  suma<-suma+impar
 }
}
print(suma)
}
g(1)
g(2)
g(3)


#EJERCICIO 3
#APARTADO (a)
fib1<-function(m){
if(m%%1==0){
 if(m<1){
  print('ERROR')
 }
 if(m==1){
  return(0)
 }
 if(m==2){
  return(1)
 }
 if(m>2){
  return(fib1(m-1)+fib1(m-2))
 }
}
else{
 print('ERROR')
}
}
fib1(0)
fib1(-1)
fib1(1.4)
fib1(1)
fib1(2)
fib1(3)
fib1(4)
fib1(5)
fib1(6)
fib1(7)
fib1(8)
fib1(9)
fib1(10)
#APARTADO (b)
fib2<-function(m){
a<-1
v<-c()
if(m%%1==0){
 if(m<1){
  print('ERROR')
 }
 else{
  while(a<=m){
   num<-fib1(a+2)
   den<-fib1(a+1)
   x<-num/den
   v<-c(v,x)
   a<-a+1
  }
  paste(v)
 }
}
else{
 print('ERROR')
}
}
fib2(3)
#APARTADO (c)
fib3<-function(m){
plot(fib2(m),main='Sucesión')
}
fib3(20)
#Su límite es 1.6


#EJERCICIO 4
h<-function(x,y){
data(iris)
if(x==1){
 return(mean(iris[,y]))
}
if(x==2){
 return(median(iris[,y]))
}
if(x==3){
 return(sd(iris[,y]))
}
if(x==4) {
 return(sd(iris[,y])^2)
}
}
h(1,4)


#EJERCICIO 6
suma.cifras<-function(x){
s<-0
if(x%%1==0){
 if(x>0){
  while(x>0){
   r<-x%%10
   s<-s+r
   x<-x%/%10
  }
  return(s)
 }
 else{
  print('El número debe ser entero positivo')
 }
}
else{
 print('El número debe ser entero positivo')
}
}
suma.cifras(234)


#EJERCICIO 7
tablas.multiplicar<-function(n){
if(n%%1==0){
 if(n>0){
  x<-1
  while(x<=n){
   cat('Tabla del',x,':','\n',x*1,x*2,x*3,x*4,x*5,x*6,x*7,x*8,x*9,x*10,'\n')
   x<-x+1
  }
 }
 else{
  print('El número debe ser natural')
 }
}
else{
 print('El número debe ser natural')
}
}
tablas.multiplicar(5)


#EJERCICIO 8
números.romanos<-function(n){
if(n%%1==0){
 if(n>0){
  if(n<3000){
   as.roman(n)
  }
  else{
   print('El número debe ser natural entre 0 y 3000')
  } 
 }
 else{
  print('El número debe ser natural entre 0 y 3000')
 }
}
else{
 print('El número debe ser natural entre 0 y 3000')
}
}
números.romanos(29)


#EJERCICIO 9
divisores<-function(n){
if(n%%1==0){
 if(n>0){
  d<-1
  v<-c(d)
  while(d<=n){
   d<-d+1
   if(n%%d==0){
    v<-c(v,d)
   }
  }
  return(v)
 }
 else{
  print('El número debe ser natural')
 }
}
else{
 print('El número debe ser natural')
}
}
divisores(12)


#EJERCICIO 10
números.primos<-function(n){
q<-c(2)
r<-3
if(n%%1==0){
 if(n>0){
  repeat{
   for(i in 2:(r-1)){
    if(r%%i==0){
     r<-r+1
    }
    else{
     q<-c(q,r)
     r<-r+1
    }
   }
    if(length(q)==n){
     break
    }
  }
  print(q)
 }
 else{
  print('El número debe ser natural')
 }
}
else{
 print('El número debe ser natural')
}
}
números.primos(10)



números.primos2<-function(n){
q<-c(2)
r<-3
if(n%%1==0){
 if(n>0){
  while(length(q)<n){
     if(r%%c(2,3,5,7)!=0){
      q<-c(q,r)
      r<-r+1
     }
     else{
      r<-r+1
     }
  }
  print(q)
 }
 else{
  print('El número debe ser natural')
 }
}
else{
 print('El número debe ser natural')
}
}
números.primos2(10)


#NO FUNCIONA NINGUNA DE LAS DOS WJEWBFIHWEFYBEWFHEWUOFHEWFBERWFHE4WHF4EWBFIHYE4WBHRUE4WHD


