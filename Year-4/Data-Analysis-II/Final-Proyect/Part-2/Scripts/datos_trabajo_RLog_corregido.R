
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

modelo0 = glm(y~age+job+marital+education+default+balance+housing+loan+contact+day
              +month+campaign+pdays+previous+poutcome, data = data, family = binomial)
summary(modelo0)

# Buscamos un modelo con menor AIC usando stepwise:

modelo <- step(modelo0,direction = "both")
summary(modelo)
