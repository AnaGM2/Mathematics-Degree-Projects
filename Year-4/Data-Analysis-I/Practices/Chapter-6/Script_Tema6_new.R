
### PRÁCTICA DE REGRESIÓN LINEAL
### María José Nueda 

#----------------------------------------------------------------------
#       EJEMPLO comercios			      
#----------------------------------------------------------------------

comercios = read.table("comercios.txt")
n = nrow(comercios)
p = ncol(comercios)-1

par(mfrow = c(1,2))
plot(comercios$POBLA, comercios$CIFRA, xlab="Población", ylab="Cifra de negocios",col=2)
plot(comercios$SUPER, comercios$CIFRA, xlab="Superficie del local", ylab="Cifra de negocios",col=2)
plot(comercios, col=2)

# Podríamos calcular los coeficientes del modelo,
# según lo visto en teoría, con:

X = as.matrix(cbind(1,comercios[,2:3]))
y = as.numeric(comercios[,1])
beta = solve(t(X)%*%X,t(X)%*%y)
beta
beta = as.numeric(beta) 

y.estim = as.numeric(X%*%beta)
e.estim = y-y.estim
summary(e.estim)

S2 = sum(e.estim*e.estim)/(n-(p+1))
VC.beta = S2*solve(t(X)%*%X)
e.stand = sqrt(diag(VC.beta))
e.stand

# Contraste significación individual 
# H0: betaj = 0  vs  alternativa bilateral (para j = 0, 1, 2)

j = 1                      
t.estad = beta[j+1]/e.stand[j+1]
t.pval = 1-(pt(abs(t.estad),n-p-1)-pt(-abs(t.estad),n-p-1))

# Contraste significación global

y.mean = mean(y)
SCE = sum(e.estim*e.estim)
SCR = sum((y.estim-y.mean)*(y.estim-y.mean))
SCT = sum((y-y.mean)*(y-y.mean))
F.estad = (SCR/p)/(SCE/(n-p-1))
F.pval = 1-pf(F.estad,p,n-p-1)

R2 = SCR/SCT
R2.adj = 1-(1-R2)*(n-1)/(n-p-1)

# Usamos mejor la función lm() que lo calcula todo:
reg = lm(CIFRA~POBLA+SUPER, data=comercios)

# Cuando hay muchas variables y se desea incluir todas se puede usar:
reg = lm(CIFRA~., data=comercios)
names(reg)
summary(reg)
names(summary(reg))

# Residuals = summary(e.estim)
# Estimate = beta
# Std. Error = e.stand
# Multiple R-squared = R2
# Adjusted R-squared = R2.adj
# F-statistic = F.estad
# p-value = F.pval
# t value[2] = t.estad
# Pr(>|t|)[2] = t.pval

# reg$coefficients = beta
# reg$residuals = e.estim
# reg$fitted.values = y.estim

# Predicciones:
predict(reg,interval="confidence") # para el valor medio, datos iniciales
predict(reg,interval="prediction") # para un valor futuro, datos iniciales
# predict(reg) = reg$fitted.values

# Para un nuevo valor:
x0 = data.frame(POBLA = 41, SUPER = 22)
predict(reg, x0, interval="confidence")
predict(reg, x0, interval="prediction")

# Intervalo de confianza para la predicción de un individuo que toma los valores de x0:
vx0 = c(1,41,22)
y.fit = beta[1]+beta[2]*vx0[2]+beta[3]*vx0[3]
t.crit = qt(0.975,n-p-1)
prod = 1 + vx0%*%solve(t(X)%*%X)%*%vx0
int.lwr = y.fit - t.crit*sqrt(S2*prod)
int.upr = y.fit + t.crit*sqrt(S2*prod)
c(int.lwr, int.upr)

# Intervalo de confianza para la predicción media de todos los individuos que toman
# los valores del vector x0: se puede hacer quitando el 1 de prod, es decir, con
# prod = vx0%*%solve(t(X)%*%X)%*%vx0

# DIAGNOSIS Y VALIDACIÓN DEL MODELO

# MULTICOLINEALIDAD

# Para calcular el R2 de cada variable explicativa con el resto,
# hay que utilizar el programa "Multicoli", en el que el input es una
# matriz que incluye las variables explicativas en las columnas.

source("Multicoli.R")
Multicoli(comercios[,-1]) 
#R2 de población frente a superficie
#R2 de superficie frente a población

# HETEROCEDASTICIDAD

#Gráficamente: 
plot(reg$fit, reg$res)

#Analíticamente:
res2 = reg$residuals^2
summary(lm(res2~POBLA+SUPER, data=comercios))
# No hay problemas de heterocedasticidad, pues p-valor = 0.1934 (es alto).
# La varianza se puede considerar constante.

# AUTOCORRELACIÓN 

plot(reg$res)
res = reg$res
n = 15
cor(res[-1],res[-n])
# Comparamos el 2º de res[-1] con el 1º de res[-n], el 3º de res[-1] con el 2º de res[-n]...

# MEDIDAS DE INFLUENCIA

p = 2
# Influencia a priori: leverage: están entre 1/n y 1
hatvalues(reg)

# Influencia a posteriori:
cooks.distance(reg)
qf(0.05,p+1,n-p-1,lower.tail=F)
# Ninguno supera el 3.49, son todos valores muy pequeños.

# VALORES ANÓMALOS

# residuos en valor absoluto que superen este valor, serán anómalos
abs(rstudent(reg)) 
qt(0.025, n-p-2, lower.tail=F)

# Normalidad de los residuos:
par(mfrow = c(1,2))
res = reg$residuals
hist(res)
qqnorm(res)
qqline(res)
# Es una muestra pequeña, por lo que no debería alarmarnos que algo se salga de lo normal.
shapiro.test(res)
# H0 : normal
# p-valor alto, no rechazo H0, acepto normalidad

# Gráfico global:
par(mfrow = c(2,2))
plot(reg)
# Residuals vs Fitted es aproximadamente plano (horizontal)
# Scale-Location es como Residuals vs Fitted pero estandarizado y sacando la raíz
# Los raros viendo el eje de las y en Residuals vs Leverage, no hay valores atípicos exagerados
# Los números que aparecen son los que se salen de lo normal


#----------------------------------------------------------------------
# step con datos EJERCICIO 1
#----------------------------------------------------------------------

data = read.table("EMPRESAS08.txt")
reg0 = lm(RESULTAD~., data=data)
summary(reg0)
# Ninguna de las variables salvo CASHFLOW es significativa,
# a pesar de que R2 es bueno, luego sospechamos que hay problemas.
Multicoli(data[,-1])
# Hay problemas de multicolinealidad.
# Los R2's son bastante altos, hay una relación lineal profunda entre variables
# significativas. Hay relaciones entre las variables muy altas.

### Función por pasos: step. Por defecto: backward, direction="forward".

?step 
# step(lm(),direction="backward"(por defecto)/"forward"/"both")

# Hacia adelante sin posibilidad de salida:

reg1 = lm(RESULTAD~1, data=data)
step.1 = step(reg1, scope=~PLANTILL+CASHFLOW+CAPITAL+RECPROP+VENTAS+INMOVILI+ACTIVOS,direction="forward")
# Si incluyo CASHFLOW el AIC=970.79 <- El mejor (más pequeño)
# Si incluyo RECPROP el AIC=1035.21
# Si no incluyo ninguno el AIC=1040.07
# Añado CASHFLOW
# Si incluyo ACTIVOS el AIC=892.56 <- El mejor (más pequeño)
# Añado ACTIVOS
# Si incluyo CAPITAL el AIC=890.38 <- El mejor (más pequeño)
# Añado CAPITAL
# Si no incluyo ninguno el AIC=890.38 <- El mejor (más pequeño)
# Me quedo como estoy y acabo

# Hacia atrás sin posibilidad de entrada:

step.2 = step(reg0)
# Si quito VENTAS el AIC=894.32 <- El mejor (más pequeño)
# Quito VENTAS

# Hacia adelante con posibilidad de salida:

reg1 = lm(RESULTAD~1, data=data)
step.3 = step(reg1, scope=~PLANTILL+CASHFLOW+CAPITAL+RECPROP+VENTAS+INMOVILI+ACTIVOS,direction="both")
# Se puede quitar alguna de las que quedan, no hacer nada o volver a añadir alguna
# de las que has quitado antes.

# Hacia atrás con posibilidad de entrada:

step.4 = step(reg0, direction="both")

### RESULTAD ~ CASHFLOW + CAPITAL + ACTIVOS

reg2 = lm(RESULTAD ~ CASHFLOW + CAPITAL + ACTIVOS, data=data)
summary(reg2)

data[,c(3,4,8)]
Multicoli(data[,c(3,4,8)])

# Apartado a)

X = as.matrix(data[,-1])
# Matriz de correlaciones
round(cor(X),3)

source("ACP.R")
ej1 = ACP(X,q=3)

acp = ACP(X)$princomp
names(acp)
summary(acp)
XN = acp$scores[,1:3]

data2 = data.frame(cbind(data[,1],XN))

reg3 = lm(V1 ~., data=data2)
summary(reg3)

Multicoli(data2[,-1])


#----------------------------------------------------------------------
# EJERCICIO 1
#----------------------------------------------------------------------	

# Apartado a) y b)

source("ACP.R")
data = read.table("EMPRESAS08.txt")
head(data)
# Quitamos la dependiente, que está en la primera columna
acp = ACP(data[,-1],q=3)
scores = acp$princomp$scores[,1:3]
acp$Inercia
acp$R
# Primera: con bienes materiales
# Segunda: con la plantilla, números de trabajadores y ventas
# Tercera: dinero limpio

mod = lm(data$RESULTAD~scores)
mod = lm(RESULTAD~scores,data=data)
summary(mod)
Multicoli(scores)

Multicoli(data[,c(3,4,8)])
# Me sigue dando R2 muy altos
summary(lm(RESULTAD~CASHFLOW+CAPITAL+ACTIVOS,data=data))
# Quito la menos significativa, que es capital
summary(lm(RESULTAD~CASHFLOW+ACTIVOS,data=data))
# Si me quedo con dos variables tengo un modelo más sencillo y R2 de 0.9372 (alta)
# y no es muy diferente a 0.9407
Multicoli(data[,c(3,8)])
# No hay multicolinealidad


#----------------------------------------------------------------------
# EJERCICIO 2
#----------------------------------------------------------------------	
data = read.table("SALARIOS.txt")

mod.a = lm(SALARIO~ANTIG, data)
summary(mod.a)

mod.b = lm(SALARIO~ANTIG+SEXO, data)
summary(mod.b)

mod.c = lm(SALARIO~ANTIG*SEXO, data)
summary(mod.c)

# No hay diferencias en la evolución de salario con el tiempo entre hombres y mujeres.

mod.d = lm(SALARIO~(ANTIG+ESTUDIOS)*SEXO, data)
summary(mod.d)

# No hay diferencias en la evolución de salario con los estudios entre hombres y mujeres.

# Salario = beta0 + beta1*Antig + beta2*Sexo + Epsilon

# H -> 0
# M -> 1

# E[Salario|Sexo=0] = beta0 + beta1*Antig (Referencia)
# E[Salario|Sexo=1] = (beta0 + beta2) + beta1*Antig

# Salario = beta0 + beta1*Antig + beta2*Sexo + beta3*Antig*Sexo + Epsilon

# E[Salario|Sexo=0] = beta0 + beta1*Antig (Referencia)
# E[Salario|Sexo=1] = (beta0 + beta2) + (beta1 + beta3)*Antig