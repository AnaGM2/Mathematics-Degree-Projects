#############################################################################################
# EJ 1 EXAMEN PRÁCTICO 11-ENERO-16
#############################################################################################

library(MASS)
data(crabs)
data2<-crabs[,-3]

reg0 = lm(BD~ FL+RW+CL+CW, data=crabs)
summary(reg0)

# MODELO 1 ----------------------
reg1 = lm(BD ~ FL+CL, data=crabs)
summary(reg1)
# a1) BD.estim = -1.24 + 0.59FL +0.19CL

source("Multicoli.R")
Multicoli(crabs[,c(4,6)])
# a2) Hay multicolinealidad

res2 = reg1$res^2
summary(lm(res2~FL+CL, data=crabs))
# a3) No hay heterocedasticidad
# No hay relación entre las variables y el p-valor es alto

# MODELO 2 ----------------------
# Partiendo del primer modelo
reg2 = lm(BD~ FL*sp, data=crabs)
summary(reg2)
# Blue (sp=0)
# E[BD|Blue] = -1.53 + FL
# Orange (sp=1)
# E[BD|Orange] = (-1.53+0.84) + (1-0.06)FL
coef=summary(reg2)$coefficients

# En lugar de usar para el color el habitual; as.numeric(crabs$sp)+1
# codificamos con Orange/Blue, ya que definen los dos grupos de crabs
col=rep("Orange", nrow(crabs))
col[crabs$sp=="B"]="Blue"

plot(crabs$FL, crabs$BD, col=col, pch=20)
legend("topleft", c("B", "O"), pch=20, col=c("Blue", "Orange"))
abline(a=coef[1,1], b=coef[2,1], col="Blue", lwd=2)
abline(a=coef[1,1]+coef[3,1], b=coef[2,1]+coef[4,1], col="Orange", lwd=2)
# La diferencia de pendientes es significativa

# si se escoge CL (partiendo del segundo modelo)
reg2b = lm(BD~ CL*sp, data=crabs)
summary(reg2b)

# MODELO 3 ----------------------
source("ACP.R")
acp = ACP(crabs[,4:7], q=2)
acp$Inercia
acp$mu
acp$R
compo1 = acp$princomp$scores[,1]

reg3 = lm(BD~compo1, data=crabs)
summary(reg3)


# 1) R2 = 0.982
# 2) R2 = 0.976
# 3) R2 = 0.96
# Los 3 modelos tienen buenos R2's
# El más cómodo de interpretar es el segundo


#############################################################################################
# EJERCICIO 2
#############################################################################################

Y = as.matrix(crabs[,4:8])
model = manova(Y~crabs$sp*crabs$sex)
summary.aov(model)

# Todas significativas (fijarse en p-valor de crabs$sp)

# RW sale significativa para crabs$sex, es la que más discrimina entre sexos
# p-valor= 6.133e-06 más pequeño, F = 21.608 más grande

# Todas las interacciones son significativas
# Las medidas morfologicas para macho, hembra de naranja son diferentes a las
# de macho, hembra de azul

lda.sp = lda(sp~FL+RW+CL+CW+BD, crabs)
pred1 = predict(lda.sp)$class
table(pred1,crabs$sp)

lda.sex = lda(sex~FL+RW+CL+CW+BD, crabs)
pred2 = predict(lda.sex)$class
table(pred2,crabs$sex)

# Variable sp, se consigue que no haya ningún error