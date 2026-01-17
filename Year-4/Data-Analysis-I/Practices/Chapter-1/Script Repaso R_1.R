################################################################
######   ANÁLISIS DE DATOS I. REPASO ESTADISTICA CON R - Ejemplos
######   María J. Nueda Roldán
######   Septiembre 2015
################################################################

#############      INTRODUCIR DATOS               ############## 

EDAD <- c(18,19,17,19,22,21,22,19,19,28,27,22,23,18,18,37,56,19,20,19)
NOTA <- c(7,3.4,5.3,6.1,5,5,9,4.1,3,5,5,6.3,5.3,5.5,9.5,7.8,8,3.6,4,5)
ALTURA <- c(1.68,1.80, 1.71,1.56,1.70,1.79,1.64,1.65,1.85,1.70,1.75,1.65,1.80,1.62,1.60,1.72,1.78,1.67,1.87,1.55)
PESO <- c(60,75,60,50,57,75,58,55,80,66,70,58,78,62,64,65,80,70,90,58)

SEXO <- factor(c(1,1,1,2,2,1,1,2,1,1,2,1,2,1,2,2,1,1,1,1),labels=c("HOMBRE","MUJER"))
CALIFICACIÓN<-factor(c(3,1,2,2,2,2,4,1,1,2,2,2,2,2,4,3,3,1,1,2),labels=c("SUSPENSO","APROBADO", "NOTABLE", "SOBRESALIENTE"))


#############      TABULACIÓN Y REPRESENTACIÓN     ############## 
table(CALIFICACIÓN)
T.cal <- table(CALIFICACIÓN)
barplot(T.cal)
hist(PESO)

#############      INFERENCIA ESTADÍSTICA          ############## 

t.test(NOTA, mu=6)

t.test(ALTURA~SEXO, var.equal=T, conf.level=0.9)
var.test(ALTURA~SEXO)


PESO <- c(57,49,60,55,57,48,50,61,52,56,55,48,58,56,54,48,52,56,50,58)
MOMENTO <- rep(c("antes","después"),each=10)
t.test(PESO~MOMENTO, paired=T, alternative="greater")
