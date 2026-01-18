
data$day_category <- cut(data$day, breaks = c(0, 10, 20, 31), labels = c("10d", "20d", "30d"))
data$campaign_category <- cut(data$campaign, breaks = c(-Inf, 5, Inf), labels = c("Baja", "Alta"))
data$duration_category <- cut(data$duration, breaks = c(0, 180, 480, Inf), labels = c("corta", "media", "larga"))

modANOVA1 <- aov(y.bin~marital + education + housing + loan + 
                   contact + month + 
                   data$duration_category + data$day_category + data$campaign_category + poutcome,data = data)
summary(modANOVA1)

# La variable más significativa es duration ya que p-valor<2e-16
# y F = 417.994 es mayor que el de poutcome.

modelo_def1 <- aov(y.bin~duration_category,data = data)
summary(modelo_def1)

boxplot(data$y.bin~data$duration_category)
# No hay igualdad de varianzas y no hay normalidad.
res1 = modelo_def1$residuals

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
# 

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
# Idem

t.test(y_ml~p_ml, p.adjust.method = "none")$conf.int
# Idem

##########################################################

# IC Tukey:

TukeyHSD(modelo_def1)
# hay diferencias de proporciones.

plot(TukeyHSD(aov(data$y.bin~data$duration_category), conf.level=.95),las=2)
