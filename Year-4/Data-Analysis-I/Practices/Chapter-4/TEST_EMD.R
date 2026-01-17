
############### EJERCICIO 1 ###############

# A partir de los datos disicoches.txt: La correlación entre las disimilaridades 
# iniciales y las distancias obtenidas entre cada par de coches con la solución 
# del EMD-no métrico (redondeando a 3 decimales) es: 0.969

library(MASS)

D = read.table("disicoches.txt")
D = as.dist(D)
carac = read.table("caracoches.txt",header=TRUE,row.names=1)

# No métrico
emd.2 = isoMDS(D)

she = Shepard(D, emd.2$points)
round(cor(she$x, she$y),3)


############### EJERCICIO 2 ###############

# Al aplicar EMD-no métrico a disicoches, si permitimos un nivel de tolerancia de
# 0.000001, lograríamos alcanzar un nivel de stress (redondando a 3 decimales) de:
# 3.876

emd.3 = isoMDS(D, tol=0.000001)
round(emd.3$stress,3)


############### EJERCICIO 3 ###############

# Al aplicar un Análisis de Escalas Multidimensionales (EMD) no métrico a la
# matriz disicoches.txt, al comparar los valores de stress podemos decir que:
# Conseguimos mejorar la solución con respecto al análisis EMD métrico.

emd.2 = isoMDS(D)
# Disminuye el stress


############### EJERCICIO 4 ###############

# A partir de los datos disicoches.txt, la calidad del ajuste obtenido con el 
# EMD-métrico, calculada a partir de los valores propios de la matriz Sigma es:
# 96.56%

# Métrico
emd.1 = cmdscale(D, eig=TRUE)
cumsum(emd.1$eig^2 / sum(emd.1$eig^2))
# Calidad de representación: 0.9655698


############### EJERCICIO 5 ###############

# Podremos calcular una medida de la bondad del ajuste obtenido a partir de los 
# valores propios de la matriz Σ:
# Sólo en un análisis EMD-métrico.


############### EJERCICIO 6 ###############

# La representación gráfica en 2 dimensiones de los 12 coches obtenida con un 
# Análisis EMD-no métrico nos indica:
# Respecto del primer eje el coche más diferenciado es el Carrera.
# Respecto del segundo eje el coche más diferenciado es el Opel-caravana.

plot(emd.2$points, type = "n")
text(emd.2$points, labels =rownames(carac), col=2)


############### EJERCICIO 7 ###############

# La interpretación que le podríamos dar a las 2 dimensiones en las que hemos
# representado a los 12 coches con el EMD no métrico nos indica que el individuo 
# que ha comparado los coches:
# No se fija más en el tamaño que en el precio y la potencia del vehículo.
# Le da importancia al tamaño del vehículo.

cor(carac,emd.2$points)


############### EJERCICIO 8 ###############

# A partir de los datos disicoches.txt, el primer valor propio de la matriz Σ,
# asociada a un análisis EMD-métrico, redondeado a 3 decimales es: 74.727

round(emd.1$eig[1],3)


############### EJERCICIO 9 ###############

# El diagrama de Shepard se puede utilizar para valorar la calidad del ajuste 
# obtenido: En un análisis EMD-no métrico y también en el EMD-métrico.


############### EJERCICIO 10 ###############

# La matriz de correlaciones de la configuración obtenida con el EMD-no métrico
# con la información caracoches.txt nos indica:
# Las variables potencia y precio están altamente correlacionadas.

cor(carac,emd.2$points)
cor(carac)
