
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

# Modelo con interacciones:

# modelo.int <- glm(y ~ age*job*marital*education*default*balance*housing*loan*contact*
#                    day*month*duration*campaign*pdays*previous*poutcome, data = data, family = binomial)

# Demasiado coste computacional.

# Modelo sin interacciones:

modelo0 = glm(data$y~., data = data, family = binomial)
summary(modelo0)

# Buscamos un modelo con menor AIC usando stepwise:

modelo <- step(modelo0,direction = "both")
summary(modelo)

exp(modelo$coefficients)

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

# Estabilidad del R^2 mediante bootstrap 

rsq <- function(formula, data, indices){
  d = data[indices,] # permite a boot seleccionar el sample
  # fit regresión logística
  fit = glm(formula, data=d, family=binomial)
  return((fit$null.deviance-fit$deviance)/fit$null.deviance)
}

# Bootstrapping con 1000 réplicas del R^2:
R2b = boot::boot(data=data, statistic=rsq, R=1000, formula=y~marital + education + 
                  housing + loan + contact + day + month + duration + campaign + poutcome)
R2b
plot(R2b)
boot::boot.ci(R2b, type="perc")

##########################################################

coef(modelo)

# Bootstrap para los coeficientes del modelo

# Función para obtener los coeficientes de la regresión:
bs <- function(formula, data, indices){
  d = data[indices,] # permite a boot seleccionar el sample
  fit = glm(formula, data=d, family=binomial)
  return(coef(fit))
}

# Bootstrapping con 1000 réplicas:
Coefb = boot::boot(data=data, statistic=bs, R=1000, formula=y~marital + education + 
                     housing + loan + contact + day + month + duration + campaign + poutcome)
Coefb

plot(Coefb, index=1) # intercept
plot(Coefb, index=2) # maritalmarried
plot(Coefb, index=3) # maritalsingle
plot(Coefb, index=4) # educationsecondary
plot(Coefb, index=5) # educationtertiary
plot(Coefb, index=6) # educationunknown
plot(Coefb, index=7) # housingyes
plot(Coefb, index=8) # loanyes
plot(Coefb, index=9) # contacttelephone
# etc

# Obtener intervalos de confianza del 95%:
boot::boot.ci(Coefb, type="perc", index=1) # intercept
boot::boot.ci(Coefb, type="perc", index=2) # maritalmarried
boot::boot.ci(Coefb, type="perc", index=3) # maritalsingle
# etc

# Lo hacemos mejor con un bucle:
for (i in (1:27)){print(boot::boot.ci(Coefb, type="perc", index=i))}

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

# Al ser duration, day y campaign variables cuantativas, hemos transformado esas variables en varariables categóricas para hacer el ANOVA

data$day_category <- cut(data$day, breaks = c(0, 10, 20, 31), labels = c("10d", "20d", "30d"))
data$campaign_category <- cut(data$campaign, breaks = c(-Inf, 5, Inf), labels = c("Baja", "Alta"))
data$duration_category <- cut(data$duration, breaks = c(0, 180, 480, Inf), labels = c("corta", "media", "larga"))


modANOVA1 <- aov(y.bin~marital + education + housing + loan + 
                   contact + month + 
                   data$duration_category + data$day_category + data$campaign_category + poutcome,data = data)
summary(modANOVA1)

# La variable más significativa es duration_category ya que p-valor<2e-16
# y tiene el valor más alto de F = 417.994.

modelo_def1 <- aov(y.bin~duration_category,data = data)
summary(modelo_def1)

boxplot(data$y.bin~data$duration_category)
# No hay igualdad de varianzas y no hay normalidad.
res1 = modelo_def1$residuals

##########################################################

ggplot(data, aes(x=y, fill=duration_category, color=duration_category)) +
  geom_bar(position=position_dodge()) +
  scale_fill_brewer(palette="Pastel1") +
  scale_color_brewer(palette="Dark2") +
  theme_minimal() +
  ggtitle("Gráfico de barras por suscripción por duración del último contacto") +
  labs(x="Suscripción", y="Nº de clientes") +
  theme(legend.title = element_blank())

##########################################################

# Normalidad:

f2<-function(x){qqnorm(x);qqline(x,col=2)}
par(mfrow=c(2,2))
tapply(data$y.bin, data$duration_category, f2)

tapply(data$y.bin, data$duration_category, shapiro.test)
# Todos los p-value < 0.05 => Rechazamos normalidad para todos los grupos.

# Normalidad de residuos:

par(mfrow=c(1,2))
hist(res1)
qqnorm(res1)
qqline(res1,col=2)

shapiro.test(res1)

# p-value < 0.05 => Rechazamos normalidad de residuos.

# No hay normalidad.

##########################################################

# Homocedasticidad:

bartlett.test(data$y.bin~data$duration_category)
# p-value < 0.05 => Rechazamos igualdad de varianzas (homocedasticidad).

# Patrones en los residuos:
summary(lm(res1^2~data$duration_category))
plot(modelo_def1$fitted.values, res1)

# No hay homocedasticidad.

##########################################################

# Independencia de residuos:

plot(res1)
# Parece que se observan patrones en los residuos.
# ¿No hay independencia de residuos?

library(zoo)
library(lmtest)

dwtest(modelo_def1)
# Con un valor DW cercano a 2 y un p-value de 0.29, no hay suficiente evidencia para rechazar la hipótesis nula


##########################################################

# Outliers en los residuos:

boxplot(res1)

# Hay outliers en los residuos.

##########################################################

# Contrastes a pares:

pairwise.t.test(data$y.bin, data$duration_category, p.adjust.method="none")

# Sin ajustar p-valores nos da diferencia de proporciones entre
# todos los pares de grupos, pues para todos ellos p-valor<0.05.

# Ajustamos por Bonferroni:

pairwise.t.test(data$y.bin, data$duration_category, p.adjust.method="bonfe")

# Idem

# Ajustamos por FDR:

pairwise.t.test(data$y.bin, data$duration_category, p.adjust.method="fdr")

# Idem

##########################################################

y_corta = data$y.bin[data$duration_category == "corta"]
y_media = data$y.bin[data$duration_category == "media"]
y_larga = data$y.bin[data$duration_category == "larga"]


p_corta = data$duration_category[data$duration_category == "corta"]
p_media = data$duration_category[data$duration_category == "media"]
p_larga = data$duration_category[data$duration_category == "larga"]


y_cm = c(y_corta,y_media)
p_cm = c(p_corta,p_media)

y_cl = c(y_corta,y_larga)
p_cl = c(p_corta,p_larga)

y_ml = c(y_media,y_larga)
p_ml = c(p_media,p_larga)

# IC clásico:

t.test(y_cm~p_cm, p.adjust.method = "none")$conf.int
# Hay diferencia de proporciones entre los grupos dur_corta y dur_media
# ya que el 0 no está en el IC.

t.test(y_cl~p_cl, p.adjust.method = "none")$conf.int
# Hay diferencia de proporciones entre los grupos dur_corta y dur_larga
# ya que el 0 no está en el IC.

t.test(y_ml~p_ml, p.adjust.method = "none")$conf.int
# Hay diferencia de proporciones entre los grupos dur_media y dur_larga
# ya que el 0 no está en el IC.

##########################################################

# IC Tukey:

TukeyHSD(modelo_def1)
# Como todos los valores p ajustados son 0, todas las comparaciones entre 
# los niveles de "duration_category" son significativamente diferentes entre sí.
# Y que el 0 no está en el IC por tanto hay diferencias de proporciones.

plot(TukeyHSD(aov(data$y.bin~data$duration_category), conf.level=.95),las=2)
