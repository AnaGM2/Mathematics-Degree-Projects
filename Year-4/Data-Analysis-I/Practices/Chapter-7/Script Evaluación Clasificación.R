#-------------------------------------------------------------
# default
#-------------------------------------------------------------
library(ISLR)
library(MASS)

z <- lda(default ~balance+student, Default)
P <- predict(z, Default)
table(P$class, Default$default)

# Tasa de error
(23+252)/10000
# Fiabilidad
(9644+81)/10000
#Precisión
81/(23+81)
#Exhaustividad = Sensibilidad
81/(252+81)
# Especificidad
9644/9677


# Si consideramos p=0.2 como umbral para clasificar a los que no pagan
class = rep("No",nrow(Default))
head(P$posterior)
class[P$posterior[,2]>0.2]="Yes"
table(class, Default$default)

#Precisión
195/(235+195)
#Exhaustividad = Sensibilidad
195/(252+81)
# Especificidad
9432/9677
