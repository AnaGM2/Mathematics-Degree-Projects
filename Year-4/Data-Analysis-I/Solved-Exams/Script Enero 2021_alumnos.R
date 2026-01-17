#------------------------
## Examen Práctico 18/01/2021
#------------------------
#EJERCICIO 1
#------------------------
V=matrix(c(1,0,-0.8,0,4,0.6,-0.8,0.6,4),3,3)
M2=diag(diag(V)^(-1/2))
S=M2%*%V%*%M2
vals=eigen(S)$values 
cumsum(vals/sum(vals))


#------------------------
#EJERCICIO 2
#------------------------
library(MASS)
head(Boston)
Boston2=Boston[,c(-4,-9)]
head(Boston2)

#a)
reg1=lm(medv~., data=Boston2)
summary(reg1)
#b)
source('Multicoli.R')
Multicoli(Boston2[,-12])
#c)
source('D:/1-DOCENCIA/2ANALISIS DE DATOS I/2 PRACTICA/2ACP/ACP2010.R')
acp1=ACP(Boston2[,-12],q=3)
acp1$princomp$sdev
compo=acp1$princomp$scores[,1:3]
reg2=lm(Boston$medv~compo)
summary(reg2)
#d)
res2 = reg2$residuals^2
summary(lm(res2~compo))
#e)
reg3=lm(Boston$medv~compo*Boston$chas)
summary(reg3)

#------------------------
#EJERCICIO 3
#------------------------
Boston3=scale(Boston2)
#a)
D=dist(Boston3)
hc=hclust(D,method="complete")
plot(hc, hang=-1)
cut=cutree(hc,5)
#b)
set.seed(1)
km = kmeans(Boston2, 5)
table(km$cluster)

#------------------------
#EJERCICIO 4
#------------------------
# a)
head(cabbages)
model = lda(Date~HeadWt+VitC,data=cabbages)
z=predict(model)
table(z$class,cabbages$Date)
# No se puede predecir con éxito porque hay muchos errores
# Si no piden la H, directamente hacer lda

# b) 
Y=as.matrix(cabbages[,3:4])
ej2=manova(Y~Date*Cult, data=cabbages)
summary.aov(ej2) 
# escogemos HeadWt (p-valor = 0.0015571 es el más pequeño)
# SCB1x2 = 6.8863
boxplot(HeadWt~Date, data=cabbages)
boxplot(HeadWt~Cult, data=cabbages)
pairwise.t.test(cabbages$HeadWt,cabbages$Date,p.adjust.method = "bonferroni")
# La diferencia significativa está entre d20 Y d21
pairwise.t.test(cabbages$HeadWt, cabbages$Cult,p.adjust.method = "bonferroni")
# Sale significativa, c39 da un peso mayor que c52
interaction.plot(cabbages$Date,cabbages$Cult,cabbages$HeadWt, col=c(2,3))
# Para c39 el peso no varía con el tiempo

# añado en clase esto:
# lda para precedir Cult en función de HeadWt+VitC. 
# Si consideramos c39(-) y c52(+), calcula la sensib y especif
model = lda(Cult~HeadWt+VitC,data=cabbages)
z=predict(model)
table(z$class,cabbages$Cult)
sens = 21/30
espe = 26/30