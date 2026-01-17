lmCV <- function(data, n.training, formula, N=20)
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
  
  mod.training = lm(formula, data = data.training)
  
  MSE.1 = c(MSE.1,sum((mod.training$fitted.values-data.training$medv)^2)/n.training)
  pred.test = predict(mod.training, data.test)
  MSE.2=c(MSE.2,sum((pred.test-data.test$medv)^2)/n.test)
  }
  output = c(mean(MSE.1),mean(MSE.2) )
  names(output)=c("Error.training", "Error.test")
  output
}

