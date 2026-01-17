
############### EJERCICIO 1 ###############

data = read.table("escarabajos.txt")

resulL = aov(data$LONGITUD~data$TIPO)
summary(resulL)

resulA = aov(data$ANGULO~data$TIPO)
summary(resulA)

# Mayor poder discriminatorio: LONGITUD pues toma un valor del estadístico F mayor

Y = as.matrix(data[,2:3])
resul2 = manova(Y ~ data$TIPO)
summary.aov(resul2)

# Con respecto a la variable LONGITUD el tipo de escarabajo que más se diferencia
# es heikertingeri

boxplot(data$LONGITUD~data$TIPO)
TukeyHSD(resulL)

# Con respecto a la variable ANGULO el tipo de escarabajo que más se diferencia
# es heptapotamica

boxplot(data$ANGULO~data$TIPO)
TukeyHSD(resulA)

# Comparación de medias por pares:

# La diferencia entre la media de la variable ANGULO del E.concinna y el E.heikertingeri
# no es estadísticamente significativa ya que su p-valor ajustado toma el valor 1

pairwise.t.test(data$ANGULO,data$TIPO,p.adjust.method ="bonfe")


############### EJERCICIO 2 ###############

taqui = read.table("taqui.txt")
Y2 = as.matrix(taqui[,3:4])

# Nivel de significación alpha = 0.05

resulVM = aov(taqui$VELOCIDA~taqui$METODO)
summary(resulVM)

resulPM = aov(taqui$PRECISION~taqui$METODO)
summary(resulPM)

resulM = manova(Y2 ~ taqui$METODO)
summary.aov(resulM)

# Hay alguna diferencia entre las medias de alguna de las variables estudiadas
# para los niveles de MÉTODO.

resulVH = aov(taqui$VELOCIDA~taqui$HORARIO)
summary(resulVH)

resulPH = aov(taqui$PRECISION~taqui$HORARIO)
summary(resulPH)

resulH = manova(Y2 ~ taqui$HORARIO)
summary.aov(resulH)

# Hay alguna diferencia entre las medias de alguna de las variables estudiadas
# para los niveles de HORARIO.

resulVHM = aov(VELOCIDA~HORARIO*METODO,data=taqui)
summary(resulVHM)

resulPHM = aov(PRECISION~HORARIO*METODO,data=taqui)
summary(resulPHM)

resulMH = manova(Y2 ~ taqui$METODO*taqui$HORARIO)
summary.aov(resulMH)

# Sí hay alguna interacción estadísticamente significativa entre HORARIO-MÉTODO
# para alguna de las variables estudiadas.

interaction.plot(taqui$METODO,taqui$HORARIO, taqui$VELOCIDA, col=c(1,2,3), lwd=3)
interaction.plot(taqui$METODO,taqui$HORARIO, taqui$PRECISION, col=c(1,2,3), lwd=3)

# Gráficamente se aprecia que la posible interacción entre HORARIO-MÉTODO se 
# debería a que:
# Con el Horario Extensivo se obtienen los mejores resultados con el Método B
# Con el Horario Intensivo los mejores resultados se obtienen con el Método A

summary(aov(VELOCIDA~METODO*HORARIO,data=taqui))
summary(resulVM)

# SCT = SCB1 + SCB2 + SCB1x2 + SCW
# 2 Factores: 2828 = 132 + 1055 + 308 + 1333
# 1 Factor: 2828 = 132 + 2696