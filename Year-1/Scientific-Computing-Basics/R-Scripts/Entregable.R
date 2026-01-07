#####################
#NÚMEROS AMIGOS
#####################

#La siguiente función servirá para determinar si dos números dados son amigos.

#Dos números naturales, n y m, son amigos si la suma de los divisores de n
#(sin contar el propio n) es igual a m, y la suma de los divisores de m
#(sin contar el propio m) es igual a n.

#Además, un número natural es perfecto cuando es amigo de sí mismo, es decir,
#cuando la suma de sus divisores sin él mismo es igual al propio número.


números.amigos <- function(n,m){

#Establecemos una condición que determine si los números dados son naturales,
#y en caso de no serlo, pedirá otros números que sí lo sean.

  if(n%%1==0 & n>0 & m%%1==0 & m>0){
    d <- 1
    v <- c()

#Este bucle while dividirá n por todos los números naturales menores que él, y
#en caso de obtener un número natural como resultado, el divisor se guardará
#en el vector v.

    while(d<n){
      if(n%%d==0){
        v <- c(v,d)
      }
      d <- d+1
    }

#Una vez obtenidos los divisores de n, los sumamos y comprobamos si el
#resultado es igual a m. En caso afirmativo, habrá otro bucle while que,
#de la misma forma que el anterior, obtendrá los divisores de m, y en caso
#negativo, la función dará un mensaje informando de que los números dados
#no son amigos.

    s <- sum(v)
    if(s==m){
      d <- 1
      w <- c()
      while(d<m){
        if(m%%d==0){
          w <- c(w,d)
        }
        d <- d+1
      }

#Una vez obtenidos los divisores de m, se sumarán y se comprobará si el
#resultado es igual a n. En caso de no serlo, los números no serán amigos.
#Sin embargo, en caso de serlo, la función comprobará si n y m son iguales,
#pues de ser así, la función informará que el número dado es perfecto, y
#en caso de no serlo, informará que los números n y m son amigos.

      t <- sum(w)
      if(t==n & n!=m){
        cat('Los números',n,'y',m,'son amigos, pues los divisores de',n,'son:\n',
          v,'\n','Cuya suma es igual a',s,', y los divisores de',m,'son:\n',
          w,'\n','Cuya suma es igual a',t,'.\n')
      }else
      if(t==n & n==m){
        cat('El número',n,'es perfecto, es decir, es amigo de sí mismo,\n',
          'pues los divisores de',n,'son:\n',
          v,'\n','Cuya suma es igual a',s,'.\n')
      }
      else{
        cat('Los números',n,'y',m,'no son amigos.','\n')
      }
    }
    else{
      cat('Los números',n,'y',m,'no son amigos.','\n')
    }
  }
  else{
    cat('Los números dados deben ser naturales.','\n')
  }
}


#Probemos algunos ejemplos.

#Si ponemos números que no sean naturales, la función nos pedirá que sí lo
#sean:
números.amigos(2.2,-4)

#En caso de probar con números que no sean amigos, la función nos informará
#de ello:
números.amigos(23,81)

#Si probamos con números que sí lo sean, obtendremos una explicación de por
#qué lo son:
números.amigos(220,284)
números.amigos(1184,1210)

#Por último, si n es igual a m y el número es amigo de sí mismo, la función
#nos explicará que el número dado es perfecto:
números.amigos(6,6)






#######################
#DATA.FRAME ROCAS
#######################

#La siguiente función utilizará la información contenida en el data.frame rock.
#En este data.frame podemos encontrar datos acerca del área, el perímetro, la
#forma y la permeabilidad de 48 rocas.


rocas <- function(área,perímetro,forma,permeabilidad){
  a <- c()
  b <- c()
  c <- c()
  d <- c()
  e <- c()
  f <- c()
  g <- c()
  h <- c()

#Las siguientes instrucciones crearán 4 gráficos en los que se representará
#la información acerca del área, el perímetro, la forma y la permeabilidad
#de cada una de las muestras de roca tomadas. Además, aparecerá una
#línea horizontal que marque el valor que hemos dado a cada uno de estos
#parámetros, de manera que podremos observar cuántas muestras están por
#encima y por debajo de los valores dados.

  par(mfrow=c(2,2))
  plot(rock[,1],col='blue',main='Área de las rocas',xlab='Muestra',ylab='Área',pch=20)
  abline(h=área,col=2)
  plot(rock[,2],col=3,main='Perímetro de las rocas',xlab='Muestra',ylab='Perímetro',pch=20)
  abline(h=perímetro,col=2)
  plot(rock[,3],col='brown',main='Forma de las rocas',xlab='Muestra',ylab='Forma (Perímetro/Área^1/2)',pch=20)
  abline(h=forma,col=2)
  plot(rock[,4],main='Permeabilidad de las rocas',xlab='Muestra',ylab='Permeabilidad (mD)',pch=20)
  abline(h=permeabilidad,col=2)

#Los siguientes bucles for almacenarán en un vector las muestras que tengan un
#área (respectivamente, perímetro, forma y permeabilidad) inferior o igual a
#la dada por nosotros, y en otro vector las que la tengan superior. 

  for(i in rock[,1]){
    if(i<=área){
      a <- c(a,i)
    }
    else{
      b <- c(b,i)
    } 
  }
  for(j in rock[,2]){
    if(j<=perímetro){
      c <- c(c,j)
    }
    else{
      d <- c(d,j)
    } 
  }
   for(k in rock[,3]){
    if(k<=forma){
      e <- c(e,k)
    }
    else{
      f <- c(f,k)
    } 
  }
  for(l in rock[,4]){
    if(l<=permeabilidad){
      g <- c(g,l)
    }
    else{
      h <- c(h,l)
    } 
  }

#Por último, la función nos dará un mensaje informándonos acerca del número de
#rocas que tengan un área, perímetro, forma y permeabilidad superior e
#inferior o igual a la dada, calculándo la longitud de los vectores creados
#anteriormente. También nos informará acerca de la media de las muestras
#contenidas en el data.frame para cada una de las características.

   cat('En la primera gráfica observamos',length(b),'rocas con un área superior a',área,'\n',
     'y',length(a),'rocas con un área inferior o igual.\n',
     'Además, la media de las áreas es de',mean(rock[,1]),'.\n',
     'En la segunda gráfica observamos',length(d),'rocas con un perímetro superior a',perímetro,'\n',
     'y',length(c),'rocas con un perímetro inferior o igual.\n',
     'La media de los perímetros es de',mean(rock[,2]),'.\n',
     'En la tercera gráfica observamos',length(f),'rocas con una forma superior a',forma,'\n',
     'y',length(e),'rocas con una forma inferior o igual.\n',
     'La media de las formas es de',mean(rock[,3]),'.\n',
     'En la cuarta gráfica observamos',length(h),'rocas con una permeabilidad superior a',permeabilidad,'\n',
     'y',length(g),'rocas con una permeabilidad inferior o igual.\n',
     'La media de permeabilidad es de',mean(rock[,4]),'.\n')
}


#Veamos algunos ejemplos.

#Establecemos un área de 3000, un perímetro de 1000, una forma de 0.2 y una
#permeabilidad de 870:
rocas(3000,1000,0.2,870)

#Establecemos un área de 10000, un perímetro de 3500, una forma de 0.4 y una
#permeabilidad de 1200:
rocas(10000,3500,0.4,1200)

#Para que la línea horizontal aparezca en las gráficas, deberá tomar valores
#de área comprendidos entre 0 y 12212, que es él máximo valor que toma el
#área en el data.frame. Lo mismo ocurrirá con el perímetro, que deberá tomar
#valores entre 0 y 4864.22, la forma entre 0 y 0.464125 y la permeabilidad 
#entre 0 y 1300. En el siguiente ejemplo no aparecerán las lineas:
rocas(13000,6000,0.5,1400)






#############################
#ÁNGULOS DE UN TRIÁNGULO
#############################

#La siguiente función determinará los ángulos de un triángulo a partir de la
#longitud de sus lados. En primer lugar, tendrá en cuenta si existe un 
#triángulo con las dimensiones dadas. Para ello, la suma de sus lados de dos
#en dos deberá ser mayor al lado restante.


triángulo <- function(a,b,c){

#Establecemos la condición que determinará si existe el triángulo dado.

  if(a+b>c & a+c>b & b+c>a){
    
#Aplicando el teorema del coseno y pasando de radianes a grados obtendremos 
#el ángulo A, cuyo lado opuesto es el lado a.

    A <- acos((b^2+c^2-a^2)/(2*b*c))
    A <- (A*180)/pi
   
#Para obtener el ángulo B, con lado opuesto b, volveremos a aplicar el teorema
#del coseno y convertiremos los radianes en grados.

    B <- acos((a^2+c^2-b^2)/(2*a*c))
    B <- (B*180)/pi

#Por último, para obtener el ángulo C, cuyo lado opuesto es el c, debemos
#tener en cuenta que la suma de los ángulos de un triángulo es igual a 180,
#por lo que C será 180-A-B

    C <- 180-A-B

#A continuación calcularemos el perímetro sumando la longitud de todos sus
#lados.

    p <- a+b+c

    cat('Los ángulos del triángulo son de',A,'º,',B,'º y',C,'º 
y su perímetro es de',p,'unidades.')
  }
  else{
    print('No existe un triángulo con las dimensiones dadas.')
  }
}


#Veamos algunos ejemplos.

#Consideremos un triángulo equilátero. Sus ángulos serán de 60º.
triángulo(10,10,10)

#A continuación consideremos un triángulo isósceles.
triángulo(15,15,20)

#Veamos un triángulo rectángulo.
triángulo(1,1,sqrt(2))

#Por último, veamos un caso en el que no exista un triángulo con las
#dimensiones pedidas.
triángulo(10,12,1)

