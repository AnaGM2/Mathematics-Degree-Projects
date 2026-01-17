
############### EJERCICIO 1 ###############

v <- c(1,1,3,2,2,4,2,4,0,2,1,2,2,4,2,1,2,2,4,2)

round(mean(v),2)
round(var(v),2)
round(median(v),2)
round(sd(v),2)


############### EJERCICIO 2 ###############

CV <- function(x){sd(x)/mean(x)}

datos <- read.table("DATA.txt",header=T)

ALTURA <- datos$ALTURA
NOTA <- datos$NOTA
PESO <- datos$PESO

CV(ALTURA)
CV(NOTA)
CV(PESO)


############### EJERCICIO 3 ###############

# Matriz de varianzas-covarianzas
V <- var(datos)
V <- matrix(c(var(ALTURA),cov(NOTA,ALTURA),cov(PESO,ALTURA),cov(ALTURA,NOTA),var(NOTA),
              cov(PESO,NOTA),cov(ALTURA,PESO),cov(NOTA,PESO),var(PESO)),3,3)

solve(V)        # Inversa
sum(diag(V))    # Traza
det(V)          # Determinante


############### EJERCICIO 4 ###############

t.test(ALTURA,conf.level=0.9)

# Intervalo confianza nivel significación=10%: (1.670, 1.714)

############### EJERCICIO 5 ###############

cor(NOTA,ALTURA)
cor(PESO,ALTURA)
cor(NOTA,PESO)

# Peso correlacionada de forma positiva con altura


############### EJERCICIO 6 ###############

CALIF <- rep(1,40)
CALIF[datos$NOTA>=5]=2
CALIF[datos$NOTA>=7]=3
CALIF[datos$NOTA>=9]=4

CALIF<-factor(CALIF, labels=c("Suspenso","Aprobado","Notable","Sobresaliente"))

mean(ALTURA[CALIF=="Suspenso"])
mean(ALTURA[CALIF=="Aprobado"])
mean(ALTURA[CALIF=="Notable"])
mean(ALTURA[CALIF=="Sobresaliente"])

mean(NOTA[CALIF=="Suspenso"])
mean(NOTA[CALIF=="Aprobado"])
mean(NOTA[CALIF=="Notable"])
mean(NOTA[CALIF=="Sobresaliente"])

mean(PESO[CALIF=="Suspenso"])
mean(PESO[CALIF=="Aprobado"])
mean(PESO[CALIF=="Notable"])
mean(PESO[CALIF=="Sobresaliente"])


############### EJERCICIO 7 ###############

# Varianza
var(ALTURA)
var(NOTA)
var(PESO)

# Rango
max(ALTURA)-min(ALTURA)
max(NOTA)-min(NOTA)
max(PESO)-min(PESO)

# Coeficiente de variación
sd(ALTURA)/mean(ALTURA)
sd(NOTA)/mean(NOTA)
sd(PESO)/mean(PESO)


############### EJERCICIO 8 ###############

boxplot(ALTURA~CALIF, col=2, main="ALTURA")


############### EJERCICIO 9 ###############

cor(PESO,ALTURA)      # Coeficiente de correlación
cor(PESO,ALTURA)^2    # Coeficiente de determinación


############### EJERCICIO 10 ###############

boxplot(PESO, col=3, main="PESO")


############### EJERCICIO 11 ###############

SEXO<-c(rep("chica",20),rep("chico",20))

var.test(PESO~SEXO)
t.test(PESO~SEXO,var.equal=T,alternative="less")
# Rechazamos hipótesis nula
# Pesan más los chicos que las chicas