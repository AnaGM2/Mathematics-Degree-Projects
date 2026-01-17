######  TEMA 2: Análisis de Correspondencias
######   María José Nueda Roldán


##### EJEMPLO  ---------------------------

# Datos individuos x variables:
DATA = read.table("DATA.txt")
head(DATA)
T1 = table(DATA)
summary(T1)

# H0: X e Y independientes
# H1: No
# p-valor < alpha => Rechazo H0 => H1
# p-valor > alpha => H0

# Formato xtabs: 
T2 = xtabs(data = DATA)  
summary(T2)

# Datos en tabla contingecia:
TABLA = read.table("TABLA.txt")
class(TABLA)
summary(TABLA)
T3 = as.table(as.matrix(TABLA))
summary(T3) 


## Función corresp()
library(MASS)
out1 = corresp(TABLA, nf=2)
names(out1)
biplot(out1)


## Programa AC.R (Abrir archivo y ver detalles)
source("AC.R")
out2 =	AC(TABLA)
names(out2)

out2$INERCIA
round(out2$FILAS, 4)
round(out2$COLUMNAS, 4)


############### EJERCICIO 1 ###############

VINOS = read.table("VINOS.txt", header=TRUE)
VINOS = as.table(as.matrix(VINOS))
summary(VINOS)

EJ1 = AC(VINOS)
EJ1$INERCIA
round(EJ1$FILAS,4)
round(EJ1$COLUMNAS,4)

# Todos están bien representados menos Francia.

# El primer eje diferencia entre USA, Inglaterra a la izquierda con blanco afrutado 
# y Países Bajos, Alemania a la derecha con dulces.

# El segundo eje representa a España con tinto reserva.


############### EJERCICIO 2 ###############

Codi = rep("low", 146)
Codi[quine$Days>15] = "medium"
Codi[quine$Days>30] = "high"
Codi[quine$Days>45] = "very-high"

DATA2 = table(Codi, quine$Age)
summary(DATA2)
EJ2 = AC(DATA2)

EJ2$INERCIA
round(EJ2$FILAS, 4)
round(EJ2$COLUMNAS, 4)
