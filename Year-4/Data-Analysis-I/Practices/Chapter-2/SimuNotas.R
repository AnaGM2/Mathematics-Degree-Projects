## Simulación de NOTAS2 

NOTAS <- read.table("NOTAS.txt",header=T)

library(MASS)
mu = c(5,6)
Sigma = matrix(c(1,0.9,0.9,1),2,2) 
X = round(mvrnorm(n=10,mu,Sigma),1)

M = matrix(rep(c(1.5,0.5,1.3,0.6),each=5),10,2)
NOTAS2 = cbind(X, X*M)
colnames(NOTAS2) = colnames(NOTAS)
cor(NOTAS2)

sol.simu = ACP(NOTAS2, q=2)
sol.simu$Inercia
sol.simu$R

