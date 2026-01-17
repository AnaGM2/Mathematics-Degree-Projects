# EJERCICIO. 
# Datos: temper.txt

temper = read.table("temper.txt", header=TRUE)
head(temper)

#a)
reg = lm(CONSUMO~TEMPER, temper)
summary(reg)
coef=summary(reg)$coef

plot(temper[,1:2], col=2, pch=20)
abline(a=coef[1,1], b=coef[2,1], lwd=2, col=4)
# Al principio y al final de la recta hay más residuos por arriba que por abajo
# Por en medio hay más residuos por abajo que por arriba
# Tendría más sentido ajustar una curva en lugar de una recta
# Hay cierto comportamiento cuadrático

# b) 
plot(reg$fit,reg$res)
abline(h=0,col=2)

reg2 = lm(CONSUMO~TEMPER+I(TEMPER^2), temper)
summary(reg2)
# El R2 mejora, pero muy poco, pues antes ya era bueno
# La variable cuadrática es significativa, hay cierta relación cuadrática
coef2=summary(reg2)$coef
plot(reg2$fit,reg2$res)
abline(h=0,col=2)

plot(temper[,1:2], col=2, pch=20)
abline(a=coef[1,1], b=coef[2,1], lwd=2, col=4)
curve(coef2[1,1]+coef2[2,1]*x+coef2[3,1]*x^2, add = TRUE, lwd=2, col=3)

# c)
reg3 = lm(CONSUMO~TEMPER+I(TEMPER^2)+as.factor(DIA), temper)
# DIA no es una variable cuantitativa, si no cualitativa, por eso le decimos
# que lo trate como un factor
# La variable DIA tiene 5 categorías, por lo que necesita 4 variables binarias
summary(reg3)
# La única diferencia significativa es la del lunes con el viernes

Viernes = temper$DIA==5
reg4 = lm(CONSUMO~TEMPER+I(TEMPER^2)+Viernes, temper)
summary(reg4)
# L-J: parten de 473
# V: parte de 473-15=458