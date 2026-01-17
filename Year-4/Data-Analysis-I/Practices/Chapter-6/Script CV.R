# Script Validación Cruzada con lm()
# María José Nueda Roldán

library(MASS)
dim(Boston)

# Evaluación del error con MSE: Error Cuadrático Medio.
mod = lm(medv~., data = Boston)
summary(mod)$sigma
pred = predict(mod, Boston)
n = nrow(Boston)
sqrt(sum((pred-Boston$medv)^2)/(n-14))
MSE = sum((pred-Boston$medv)^2)/n
# MSE=SCE/n

# Evaluación de MSE en un conjunto test:
# training (n1): datos de entrenamiento que se usan para estimar el modelo: betaj.estim
# test (n2): datos para evaluar el error: R2, R2.adj, AIC, ...

data.training = Boston[1:400,]
# training: de 1 a 400
data.test = Boston[401:n,]
# test: de 401 a 506
mod.training = lm(medv~., data = data.training)
# también se puede especificar con subset los casos de Boston:
mod.training = lm(medv~., data = Boston, subset = c(1:400) )

sum((mod.training$fitted.values-data.training$medv)^2)/400 #MSE del training
# MSE1 = 22.3

pred.test = predict(mod.training, data.test)
sum((pred.test-data.test$medv)^2)/106 #MSE del test
# MSE2 = 37.89

# Si tomamos los dos conjuntos de manera aleatoria:
set.seed(1) #para poder reproducir los mismos resultados
train = sample(n, 400) # aleatoriamente toma 400 valores
data.training = Boston[train,]
data.test = Boston[-train,]
mod.training = lm(medv~., data = data.training)
sum((mod.training$fitted.values-data.training$medv)^2)/400 #MSE del training
pred.test = predict(mod.training, data.test)
sum((pred.test-data.test$medv)^2)/106 #MSE del test

# Lo ideal es repetir el proceso varias veces y tomar como MSE la media:
MSE.1 = NULL
MSE.2 = NULL
for (i in 1:20)
{
  train = sample(n, 400)
  data.training = Boston[train,]
  data.test = Boston[-train,]
  mod.training = lm(medv~., data = data.training)
  MSE.1=c(MSE.1,sum((mod.training$fitted.values-data.training$medv)^2)/400)
  pred.test = predict(mod.training, data.test)
  MSE.2=c(MSE.2,sum((pred.test-data.test$medv)^2)/106)
}
mean(MSE.1)
mean(MSE.2)
# No hay mucha diferencia entre los MSE y el del test sale mayor que el del training

# Podemos elaborar una función que haga estos cálculos:
source("lmCV.r")

# Este proceso es útil para comparar modelos
lmCV(data=Boston, n.training=400, formula=medv~age+lstat )
lmCV(data=Boston, n.training=400, formula=medv~age+lstat+rad )

# Me quedo con el primero porque el Error.test es menor

