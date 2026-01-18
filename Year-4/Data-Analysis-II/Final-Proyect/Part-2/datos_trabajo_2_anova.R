# Instalar el paquete
install.packages("car")
install.packages("lmtest")



# Cargar el paquete
library(MASS)
library(caret)
library(readxl)
library(car)
library(lmtest)


## ANOVA NO ES MUY APROPIADO PARA REALIZAR UNA DIFERENCIA DE MEDIAS TENIENDO EN CUENTA QUE NUESTRA VARIABLE ES UNA
## VARIABLE DICOTÓMICA (CON YES Y NO); POR TANTO EN VEZ DE DIFERENCIA DE MEDIAS SE VA A REALIZAR UNA DIFERENCIA DE PROPORCIONES.


datos <- read.csv("bank_data.csv")
datos$y <- ifelse(datos$y == "yes", 1, 0)

datos$y
sum(datos$y) ### Num. clientes suscritos al depósito a plazo

modelo <- aov(y~job+marital+education+default+housing+loan+contact+month+poutcome,data = datos)

summary(modelo)

res = modelo$residuals

# Verificar el supuesto de normalidad
shapiro.test(res)
## NO SIGUE UNA DISTRIBUCIÓN NORMAL!!

##La prueba de Shapiro-Wilk que estás utilizando verifica si los residuos de tu modelo
##siguen una distribución normal.Si el p-valor de esta prueba es menor que el nivel de significancia
##(usualmente 0.05), entonces puedes rechazar la hipótesis nula de que los residuos siguen una distribución normal.
##Estoindicaría que los residuos no son normales y podrías considerar transformar tus datos o usar un modelo diferente.

par(mfrow=c(1,2))
hist(res)
qqnorm(res)
qqline(res)


# Verificar el supuesto de homogeneidad de varianzas
leveneTest(modelo)
##

##La prueba de Levene que estás utilizando verifica si las varianzas de los residuos son iguales
##a través de los grupos.Si el p-valor de esta prueba es menor que el nivel de significancia,
##entonces puedes rechazar la hipótesis nula de que las varianzas son iguales.


# Verificar el supuesto de independencia
dwtest(modelo)

## SÍ TENEMOS INDEPENDENCIA DE LOS RESIDUOS!!

##La prueba de Durbin-Watson que estás utilizando verifica si los residuos son independientes.
##El valor de la estadística de Durbin-Watson varía entre 0 y 4. Un valor de 2 sugiere que no
##hay autocorrelación en la muestra. Valores menores a 2 indican autocorrelación positiva y valores
##mayores a 2 indican autocorrelación negativa. Si la autocorrelación es significativa, podrías considerar
##agregar términos de autocorrelación a tu modelo.

plot(res)


# Outliers en los residuos
boxplot(res)


