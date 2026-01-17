
############### EJERCICIO 1 ###############

data = read.table("EMPRESAS08.txt")

source("ACP.R")
acp = ACP(data[,-1],q=3)
scores = acp$princomp$scores[,1:3]

# a) No hay multicolinealidad

Multicoli(scores)

# b) Coeficiente de determinación: 0.883

mod = lm(RESULTAD~scores,data=data)
summary(mod)

# c) El modelo que estudia la relación entre residuos al cuadrado y las
# variables independientes sí es estadísticamente significativo.
# Rechazamos la hipótesis de homocedasticidad o igualdad de varianzas.

res2 = mod$residuals^2
summary(lm(res2~scores, data=data))

# d) Correlación entre εi y εi−1: 0.057

res = mod$residuals
n = nrow(data)
cor(res[-1],res[-n])

# e) Hay 6 valores anómalos o atípicos.

rstudent = abs(rstudent(mod))
p = 3
qt = qt(0.025, n-p-2, lower.tail=F)
sum(rstudent > qt)


############### EJERCICIO 2 ###############

data2 = read.table("SALARIOS.txt")

# a) No hay diferencias entre hombres y mujeres en la evolución del salario 
# conforme aumenta la antigüedad, ya que ni SEXO ni SEXO:ANTIG son significativas.

mod.a = lm(SALARIO~ANTIG*SEXO, data2)
summary(mod.a)

# b) Variable más significativa: ESTUDIOS
# Aumento medio de salario que sufre un trabajador en la empresa por un mes
# de trabajo: 4.58

mod.b = lm(SALARIO~ANTIG+ESTUDIOS, data2)
summary(mod.b)
