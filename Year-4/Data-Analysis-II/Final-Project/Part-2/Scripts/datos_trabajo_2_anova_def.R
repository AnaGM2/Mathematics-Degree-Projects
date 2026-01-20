library(zoo)
library(lmtest)

datos <- read.csv("bank_data.csv")
datos$y <- ifelse(datos$y == "yes", 1, 0)

modelo <- aov(y~job+marital+education+default+housing+loan+contact+month+poutcome,data = datos)
summary(modelo)
# La variable más significativa es poutcome ya que p-valor<2e-16 y F = 98.243 es mayor que el de month

modelo_def <- aov(y~poutcome,data = datos)
summary(modelo_def)

boxplot(datos$y~datos$poutcome)
# No hay igualdad de varianzas y no hay normalidad

bartlett.test(datos$y~datos$poutcome)
# Rechazamos igualdad de varianzas (homocedasticidad)

res = modelo_def$residuals

par(mfrow=c(1,2))
hist(res)
qqnorm(res)
qqline(res,col=2)

shapiro.test(res)
# No hay normalidad

plot(res)
# Parece que no hay independencia de los residuos

dwtest(modelo_def)
# Parece que el test Durbin-Watson detecta que hay independencia de los residuos

boxplot(res)
# Hay outliers en los residuos


# INTERVALOS DE CONFIANZA

y_success = datos$y[datos$poutcome == "success"]
y_failure = datos$y[datos$poutcome == "failure"]
y_other = datos$y[datos$poutcome == "other"]
y_unknown = datos$y[datos$poutcome == "unknown"]

p_success = datos$poutcome[datos$poutcome == "success"]
p_failure = datos$poutcome[datos$poutcome == "failure"]
p_other = datos$poutcome[datos$poutcome == "other"]
p_unknown = datos$poutcome[datos$poutcome == "unknown"]

y_sf = c(y_success,y_failure)
p_sf = c(p_success,p_failure)

y_fo = c(y_failure,y_other)
p_fo = c(p_failure,p_other)

# IC clásico

t.test(y_sf~p_sf, p.adjust.method = "none")$conf.int
# Hay diferencia de proporciones entre los grupos success y failure
# ya que el 0 no está en el IC

t.test(y_fo~p_fo, p.adjust.method = "none")$conf.int
# Hay diferencia de proporciones entre los grupos failure y other
# ya que el 0 no está en el IC

# IC Tukey

TukeyHSD(aov(datos$y~datos$poutcome))
# No hay diferencias entre other-failure porque el 0 está en el intervalo y p-valor=0.06
# No hay diferencias entre unknown-failure porque p-valor=0.051
# En el resto sí hay diferencias de proporciones
