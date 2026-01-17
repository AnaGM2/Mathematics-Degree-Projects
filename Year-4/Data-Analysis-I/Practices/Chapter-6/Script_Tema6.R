### PRÁCTICA DE REGRESIÓN LINEAL
### María José Nueda 

#----------------------------------------------------------------------
#       EJEMPLO comercios			      
#----------------------------------------------------------------------

	comercios = read.table("comercios.txt")
	
	par(mfrow = c(1,2))
	plot(comercios$POBLA, comercios$CIFRA, xlab="Poblaci?n", ylab="Cifra de negocios",col=2)
	plot(comercios$SUPER, comercios$CIFRA, xlab="Superficie del local", ylab="Cifra de negocios",col=2)

# Podríamos calcular los coeficientes del modelo con:
	X = as.matrix(cbind(1,comercios[,2:3]))
	y = as.numeric(comercios[,1])
	solve(t(X)%*%X,t(X)%*%y)

# Usamos mejor la función lm() que lo calcula todo:
	reg = lm(CIFRA~POBLA+SUPER, data=comercios)
# Cuando hay muchas variables y se desea incluir todas se puede usar:
	reg = lm(CIFRA~., data=comercios)
	names(reg)
	summary(reg)

# Predicciones:
	predict(reg,interval="confidence") #para el valor medio, datos iniciales
	predict(reg,interval="prediction") #para un valor futuro, datos iniciales
	#Para un nuevo valor:
	x0 = data.frame(POBLA = 41, SUPER = 22)
	predict(reg, x0, interval="confidence")

# Diagnósticos de multicolinealidad
	# Para calcular el R2 de cada variable explicativa con el resto,
	# hay que utilizar el programa Multicoli, en el que el input es una
	# matriz que incluye las variables explicativas en las columnas:
	source("Multicoli.R")
	Multicoli(comercios[,-1]) 

# Heteroscedasticidad:
	#Gráficamente: 
	  plot(reg$fit, reg$res)

	#Analíticamente:
    res2 = reg$residuals^2
	  summary(lm(res2~POBLA+SUPER, data=comercios))

# Autocorrelación
	plot(reg$res)
	res = reg$res
	n = 15
	cor(res[-1],res[-n])
	
# Medidas de influencia
	p = 2
	# Influencia a priori: leverage: están entre 1/n y 1
	hatvalues(reg)

	# Influencia a posteriori:
	cooks.distance(reg)
	qf(0.05,p+1,n-p-1,lower.tail=F)
	
# Valores anómalos
# residuos en valor absoluto que superen este valor, ser?n an?malos
	abs(rstudent(reg)) 
	qt(0.025, n-p-2, lower.tail=F)

# Normalidad de los residuos:
par(mfrow = c(1,2))
	res = reg$residuals
	hist(res)
	qqnorm(res)
	qqline(res)
	shapiro.test(res)
	
# Gráfico global:
	par(mfrow = c(2,2))
	plot(reg)

#----------------------------------------------------------------------
# step con datos EJERCICIO 1
#----------------------------------------------------------------------

	data = read.table("EMPRESAS08.txt")
	reg0 = lm(RESULTAD~., data=data)
	summary(reg0)
	Multicoli(data[,-1])

### Función por pasos: step. Por defecto: backward, direction="forward".

# Hacia adelante sin posibilidad de salida:

	reg1 = lm(RESULTAD~1, data=data)
	step.1 = step(reg1, scope=~PLANTILL+CASHFLOW+CAPITAL+RECPROP+VENTAS+INMOVILI+ACTIVOS,direction="forward")

# Hacia atrás sin posibilidad de entrada:

	step.2 = step(reg0)

# Hacia adelante 

	reg1 = lm(RESULTAD~1, data=data)
	step.3 = step(reg1, scope=~PLANTILL+CASHFLOW+CAPITAL+RECPROP+VENTAS+INMOVILI+ACTIVOS,direction="both")

# Hacia atrás con posibilidad de entrada:

	step.4 = step(reg0, direction="both")

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
	
	mod.d = lm(SALARIO~(ANTIG+ESTUDIOS)*SEXO, data)
	summary(mod.d)

		
	