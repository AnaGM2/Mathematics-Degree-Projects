library(MASS)

data = read.csv("bank_data.csv")

## Calcular el Modelo

data$y= as.factor(data$y)

## CALCULAR EL MODELO 

modelo = glm(data$y~., data = data, family = binomial)

modelo_optimo <- step(modelo,direction = "both")

modelo_definitivo <- glm(data$y ~data$marital + data$education + data$housing + data$loan + data$contact + data$day + 
                           data$month + data$duration + data$campaign + data$poutcome, data = data, family = "binomial")

summary(modelo_definitivo)
#####################################
modelo_definitivo$fitted.values

data_predicho <- (modelo_definitivo$fitted.values>0.2)

## Con p=0.1 se produce un aumento considerable de errores como 852 aprox.
## Mientras que con p=0.2 el aumento de errores no afecta demasiado 
## a la especificidad y aumenta considerablemente la sensibilidad.

sum(data_predicho)

sum(data$y=="yes")
#############################################################


valores_predichos <- factor(data_predicho, labels = levels(data$y))
caret::confusionMatrix(valores_predichos, data$y, positive = "yes")
#############################################################
predicciones <- predict(modelo_definitivo, newdata = data, type = "response")

# Cargamos la biblioteca pROC
library(pROC)

# Creamos el objeto ROC
roc_obj <- roc(data$y, predicciones)



# Graficamos la curva ROC
plot(roc_obj)