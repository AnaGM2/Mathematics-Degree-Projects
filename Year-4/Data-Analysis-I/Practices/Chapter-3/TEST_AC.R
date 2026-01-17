
############### EJERCICIO 1 ###############

# Antes de aplicar un análisis de correspondencias es aconsejable aplicar el 
# test de independencia para:
# Estudiar si tiene sentido aplicar un análisis de correspondencias.
# Estudiar si hay alguna relación entre las variables categóricas.


############### EJERCICIO 2 ###############

# El programa AC: No utiliza los resultados de corresp() ni los muestra.


############### EJERCICIO 3 ###############

source("AC.R")
VINOS = read.table("VINOS.txt", header=TRUE)
VINOS3 = as.table(as.matrix(VINOS))
summary(VINOS3)

EJ3 = AC(VINOS3, q=2)

round(EJ3$FILAS,4)
round(EJ3$COLUMNAS,4)

# España se inclina principalmente por el vino tinto.
# Francia no está bien representado.


############### EJERCICIO 4 ###############

# La función corresp(): No ofrece los vectores propios.


############### EJERCICIO 5 ###############

out5 = corresp(VINOS, nf=2)
val = out5$cor^2
round(val[1],4)

# El primer valor propio es 0.1522


############### EJERCICIO 6 ###############

EJ3$INERCIA

# Con un eje explicamos el 62.9% de la variabilidad total.


############### EJERCICIO 7 ###############

round(EJ3$FILAS,4)
round(EJ3$COLUMNAS,4)

# El primer eje diferencia, principalmente, entre los gustos de paises de habla
# inglesa (USA-Inglaterra) y los de Paises Bajos y Alemania.

# El segundo eje diferencia, principalmente, gustos de España y Alemania.


############### EJERCICIO 8 ###############

# Los valores propios (o sus raíces cuadradas) que se calculan a aplicar un
# Análisis de Correspondencias:
# Sólo los muestra como salida la función corresp (el programa AC no los muestra).

out5$cor


############### EJERCICIO 9 ###############

round(EJ3$FILAS,4)
round(EJ3$COLUMNAS,4)

# Todas las columnas (vinos) están bien representadas.
# Francia no está bien representado.


############### EJERCICIO 10 ###############

# El programa AC.R calcula las proyecciones columna a partir de las 
# proyecciones fila.