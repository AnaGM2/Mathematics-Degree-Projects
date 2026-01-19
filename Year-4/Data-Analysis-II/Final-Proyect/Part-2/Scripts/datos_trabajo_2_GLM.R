library(MASS)

data = read.csv("bank_data.csv")

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

sum(data_predicho)

sum(data$y=="yes")

predicciones <- predict(modelo_definitivo, newdata = data, type = "response")

# Cargamos la biblioteca pROC
library(pROC)

# Creamos el objeto ROC
roc_obj <- roc(datos$y, predicciones)

# Graficamos la curva ROC
plot(roc_obj)


# Evaluación del error con MSE: Error Cuadrático Medio.
n = nrow(data)
pred = predict(modelo_definitivo, data = data, type = "response")

data$y= ifelse(data$y == "yes", 1, 0)

MSE = sum((pred-data$y)^2)/n


# Validación cruzada

data.training = data[1:3500,]
# training: de 1 a 3500
data.test = data[3501:n,]
# test: de 3501 a 4521

mod.training <- glm(y ~ marital + education + housing + loan + contact + day + 
                           month + duration + campaign + poutcome, data = data.training, family = "binomial")

MSE.training = sum((mod.training$fitted.values-data.training$y)^2)/3500 #MSE del training

pred.test = predict(mod.training, data.test, type = "response")

MSE.test = sum((pred.test-data.test$y)^2)/(n-3500) #MSE del test

sum(pred.test > 0.3)
sum(data.test$y==1)
