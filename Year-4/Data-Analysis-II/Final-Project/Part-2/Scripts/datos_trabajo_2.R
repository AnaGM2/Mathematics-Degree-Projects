
data = read.csv("bank_data.csv")
data = data[,-1]

head(data)

n = nrow(data)

# Variable a estudiar: ¿se ha suscrito el cliente a un depósito a plazo?
data$y= as.factor(data$y)


##########################################################
# REGRESIÓN LOGÍSTICA
##########################################################

# Usamos regresión logística ya que la variable a estudiar es binaria.

modelo0 = glm(data$y~., data = data, family = binomial)
summary(modelo0)

# Buscamos un modelo con menor AIC usando stepwise:

modelo <- step(modelo0,direction = "both")
summary(modelo)

##########################################################

# Bondad del modelo: R^2

R2 = (modelo$null.deviance-modelo$deviance)/modelo$null.deviance
R2

# Con este modelo mejoramos un 32.05% el modelo nulo.

R02 = (modelo0$null.deviance-modelo0$deviance)/modelo0$null.deviance
R02

# El modelo en el que consideramos todas las variables mejora un 32.73% el modelo
# nulo. Sin embargo, elegimos el modelo obtenido con step porque tiene menor
# AIC (métrica que tiene en cuenta el Deviance, pero también el número de variables).
# La métrica AIC indica que merece la pena excluir algunas variables.

# Entre dos modelos con similar Deviance (nuestro caso):
modelo0$deviance
modelo$deviance
# elegimos el que menor número de variables tiene.

##########################################################

library(ggplot2)

pred <- predict(modelo, data, type = "response")
rank <- rank(pred)
data$y.bin= ifelse(data$y == "yes", 1, 0)

ggplot(data) +
  geom_point(aes(x = rank, y = y.bin, colour='y')) +
  geom_point(aes(x = rank, y = pred, colour='Logistic Regression')) +
  scale_color_manual(values = c("y" = '#ff00ff','Logistic Regression' = '#3399ff')) +
  xlab(label = 'Predicted rank') +
  ylab(label = 'y probability')

# ¿Cuántas predicciones están lejos del 0 y el 1?
100*sum((0.1 < pred) & (pred < 0.9)) / nrow(data)

##########################################################

# Clasificamos a un individuo de la siguiente manera:
# y = Yes si p>0.5
# y = No en caso contrario

pred1 = pred > 0.5
pred1[pred1=='TRUE'] = 'yes'
pred1[pred1=='FALSE'] = 'no'

table(pred1, data$y)

# Tasa de error (baja)
(85+346)/n
# Fiabilidad (alta)
(3915+175)/n
# Precisión
175/(85+175)
# Exhaustividad = Sensibilidad
175/(346+175)
# Especificidad (alta)
3915/(3915+85)

# De los 521 que se suscriben, el 66.41% no son detectados:
346/521

# Cambiamos el umbral de clasificación.

# Clasificamos a un individuo de la siguiente manera:
# y = Yes si p>0.2
# y = No en caso contrario

pred2 = pred > 0.2
pred2[pred2=='TRUE'] = 'yes'
pred2[pred2=='FALSE'] = 'no'

table(pred2, data$y)

# Tasa de error (aumenta pero sigue siendo baja)
(339+186)/n
# Fiabilidad (disminuye pero sigue siendo alta)
(3661+335)/n
# Precisión (disminuye)
335/(339+335)
# Exhaustividad = Sensibilidad (aumenta)
335/(186+335)
# Especificidad (disminuye pero sigue siendo alta)
3661/(3661+339)

# El aumento de errores no afecta demasiado a la especificidad.
# Se pierde precisión pero se aumenta considerablemente la sensibilidad.

# De los 521 que se suscriben, solo el 35.7% no son detectados:
186/521

# Por tanto, preferimos quedarnos con p=0.2. Probamos uno más:

# Clasificamos a un individuo de la siguiente manera:
# y = Yes si p>0.1
# y = No en caso contrario

pred3 = pred > 0.1
pred3[pred3=='TRUE'] = 'yes'
pred3[pred3=='FALSE'] = 'no'

table(pred3, data$y)

# Tasa de error (aumenta considerablemente)
(762+90)/n
# Fiabilidad (disminuye considerablemente)
(3238+431)/n

# Para p=0.1 se produce un aumento considerable de errores.
# Finalmente, nos quedamos con p=0.2.

##########################################################

# Cargamos la biblioteca pROC:
library(pROC)

# Creamos el objeto ROC:
roc_obj <- roc(data$y, pred)

# Graficamos la curva ROC:
plot(roc_obj)

##########################################################

# Evaluación del error con MSE: Error Cuadrático Medio.

pred2= ifelse(pred2 == "yes", 1, 0)

MSE = sum((pred2-data$y.bin)^2)/n
MSE

# También podemos considerar su raíz:

sqrt(MSE)

# Evaluación del error con Error Absoluto Medio.

MAE = sum(abs(pred2-data$y.bin))/n
MAE

##########################################################

# Análisis gráfico del error:

delta <- pred2 - data$y.bin

ggplot(data = data) +
  geom_histogram(aes(x = delta), 
                 alpha=0.3, fill ="red",binwidth=0.05,position="dodge")

# Distribución del error absoluto:

ggplot(data = data) +
  geom_histogram(aes(x = abs(delta)), 
                 alpha=0.3, fill ="red",binwidth=0.05)+
  xlab("Absolute delta") + 
  ylab("Count")

# El error está centrado en el 0, aunque hay algunos outliers.

##########################################################

# Validación cruzada.

data.training = data[1:3500,]
# training: de 1 a 3500
data.test = data[3501:n,]
# test: de 3501 a 4521

mod.training <- glm(y ~ marital + education + housing + loan + contact + day + 
                      month + duration + campaign + poutcome, data = data.training, family = "binomial")

#MSE del training:
pred2.training = mod.training$fitted.values > 0.2
pred2.training= ifelse(pred2.training == "TRUE", 1, 0)

MSE.training = sum((pred2.training-data.training$y.bin)^2)/3500
MSE.training

#MSE del test:
pred2.test = predict(mod.training, data.test, type = "response") > 0.2
pred2.test= ifelse(pred2.test == "TRUE", 1, 0)

MSE.test = sum((pred2.test-data.test$y.bin)^2)/(n-3500)
MSE.test

# Lo ideal es repetir el proceso varias veces y tomar como MSE la media.

set.seed(0) # Para poder reproducir los mismos resultados

# Creamos una función que haga estos cálculos:

glmCV <- function(data, n.training, formula, N=20)
{
  n = nrow(data)
  n.test = n-n.training
  
  MSE.1 = NULL
  MSE.2 = NULL
  for (i in 1:N)
  {
    train = sample(n, n.training)
    data.training = data[train,]
    data.test = data[-train,]
    
    mod.training = glm(formula, data = data.training, family = "binomial")
    
    pred2.training = mod.training$fitted.values > 0.2
    pred2.training= ifelse(pred2.training == "TRUE", 1, 0)
    MSE.1 = c(MSE.1,sum((pred2.training-data.training$y.bin)^2)/n.training)
    
    pred2.test = predict(mod.training, data.test, type = "response") > 0.2
    pred2.test= ifelse(pred2.test == "TRUE", 1, 0)
    MSE.2=c(MSE.2,sum((pred2.test-data.test$y.bin)^2)/n.test)
  }
  output = c(mean(MSE.1),mean(MSE.2) )
  names(output)=c("Error.training", "Error.test")
  output
}

glmCV(data=data, n.training=3500, formula=y ~ marital + education + housing + loan + 
        contact + day + month + duration + campaign + poutcome)

# No hay mucha diferencia entre los MSE.
# El del test sale mayor que el del training.


##########################################################
# ANOVA
##########################################################

# Como nuestra variable de interés es binaria (toma los valores "yes" y "no")
# ANOVA no es muy apropiado para realizar una diferencia de medias.
# En vez de una diferencia de medias haremos una diferencia de proporciones.

# Elegimos las variables cualitativas:
head(data)

modANOVA <- aov(y.bin~job+marital+education+default+housing+loan+contact+month+poutcome,data = data)
summary(modANOVA)
# La variable más significativa es poutcome ya que p-valor<2e-16
# y F = 98.243 es mayor que el de month.

modelo_def <- aov(y.bin~poutcome,data = data)
summary(modelo_def)

boxplot(data$y.bin~data$poutcome)
# No hay igualdad de varianzas y no hay normalidad.

res = modelo_def$residuals

##########################################################

ggplot(data, aes(x=y, fill=poutcome, color=poutcome)) +
  geom_bar(position=position_dodge()) +
  scale_fill_brewer(palette="Pastel1") +
  scale_color_brewer(palette="Dark2") +
  theme_minimal() +
  ggtitle("Gráfico de barras por suscripción por resultado de la anterior campaña") +
  labs(x="Suscripción", y="Nº de clientes") +
  theme(legend.title = element_blank())

##########################################################

# Normalidad:

f1<-function(x){qqnorm(x);qqline(x,col=2)}
par(mfrow=c(2,2))
tapply(data$y.bin, data$poutcome, f1)

tapply(data$y.bin, data$poutcome, shapiro.test)
# Todos los p-value < 0.05 => Rechazamos normalidad para todos los grupos.

# Normalidad de residuos:

par(mfrow=c(1,2))
hist(res)
qqnorm(res)
qqline(res,col=2)

shapiro.test(res)
# p-value < 0.05 => Rechazamos normalidad de residuos.

# No hay normalidad.

##########################################################

# Homocedasticidad:

bartlett.test(data$y.bin~data$poutcome)
# p-value < 0.05 => Rechazamos igualdad de varianzas (homocedasticidad).

# Patrones en los residuos:
summary(lm(res^2~data$poutcome))
plot(modelo_def$fitted.values, res)

# No hay homocedasticidad.

##########################################################

# Independencia de residuos:

plot(res)
# Parece que se observan patrones en los residuos.
# ¿No hay independencia de residuos?

library(zoo)
library(lmtest)

dwtest(modelo_def)
# Sin embargo, el test Durbin-Watson detecta independencia de los residuos.

##########################################################

# Outliers en los residuos:

boxplot(res)

# Hay outliers en los residuos.

##########################################################

# Contrastes a pares:

pairwise.t.test(data$y.bin, data$poutcome, p.adjust.method="none")

# Sin ajustar p-valores nos da diferencia de proporciones entre
# todos los pares de grupos, pues para todos ellos p-valor<0.05.

# Ajustamos por Bonferroni:

pairwise.t.test(data$y.bin, data$poutcome, p.adjust.method="bonfe")

# Hay diferencia de proporciones entre success-failure, success-other,
# unknown-other y unknown-success, porque p-valor<0.05.

# Ajustamos por FDR:

pairwise.t.test(data$y.bin, data$poutcome, p.adjust.method="fdr")

# Nos da todas las diferencias entre pares de grupos significativas
# (igual que sin ajustar p-valores).

##########################################################

y_success = data$y.bin[data$poutcome == "success"]
y_failure = data$y.bin[data$poutcome == "failure"]
y_other = data$y.bin[data$poutcome == "other"]
y_unknown = data$y.bin[data$poutcome == "unknown"]

p_success = data$poutcome[data$poutcome == "success"]
p_failure = data$poutcome[data$poutcome == "failure"]
p_other = data$poutcome[data$poutcome == "other"]
p_unknown = data$poutcome[data$poutcome == "unknown"]

y_sf = c(y_success,y_failure)
p_sf = c(p_success,p_failure)

y_fo = c(y_failure,y_other)
p_fo = c(p_failure,p_other)

# IC clásico:

t.test(y_sf~p_sf, p.adjust.method = "none")$conf.int
# Hay diferencia de proporciones entre los grupos success y failure
# ya que el 0 no está en el IC.

t.test(y_fo~p_fo, p.adjust.method = "none")$conf.int
# Parece que hay diferencia de proporciones entre los grupos failure y other
# ya que el 0 no está en el IC. ¿Realmente la hay?
# Al ajustar con bonferroni hemos visto que no.

##########################################################

# IC Tukey:

TukeyHSD(modelo_def)
# No hay diferencias entre other-failure porque el 0 está en el intervalo y p-valor=0.06
# No hay diferencias entre unknown-failure porque p-valor=0.051.
# En el resto sí hay diferencias de proporciones.

plot(TukeyHSD(aov(data$y.bin~data$poutcome), conf.level=.95),las=2)
