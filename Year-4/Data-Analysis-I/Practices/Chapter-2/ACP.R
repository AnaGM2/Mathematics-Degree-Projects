ACP <- function(X, q = 2)
{
	X = as.matrix(X)
	n = nrow(X)
	p = ncol(X)

	acp = princomp(X, cor=T)

# VARIANZA O INERCIA EXPLICADA
	var = acp$sdev^2/sum(acp$sdev^2)
	cum.var = cumsum(acp$sdev^2/sum(acp$sdev^2))
	VAR = matrix(c(var, cum.var), p, 2)
	colnames(VAR) = c("Var.exp", "Var.exp.acum")

	par(mfrow=c(2, 2))
	screeplot(acp, type="lines")

#-----------------------------------------------
# VARIABLES
#-----------------------------------------------
	# INTERPRETACIÓN: a partir de la  correlación entre variables originales y CP 
	R = acp$loadings[, 1:q]%*%diag(acp$sdev[1:q])     # R=D(1/sigma)*U*D(sqrt(lambda))
                       # acp$loadings = D(1/sigma)*U, diag(acp$sdev)=D(sqrt(lambda))
	# Representación de las variables
	rownames(R) = colnames(X)
	plot(R[, 1], R[, 2], xlim=c(-1, 1), ylim=c(-1, 1), type="n", xlab="Componente 1", ylab="Componente 2")
	text(R[, 1], R[, 2], col=2, labels=rownames(R))
	title("Grafico de las variables")

	# Calidad de representación de las variables
	mu = apply(R^2, 1, sum)

#-----------------------------------------------
# INDIVIDUOS
#-----------------------------------------------
	plot(acp$scores[, 1], acp$scores[, 2], xlab="Component 1",  ylab="Component 2", type="n", main="Individuos")
	text(acp$scores[, 1], acp$scores[, 2], col=2)

	num = apply(acp$scores[, 1:q]^2, 1, sum)
	Xs = stand(X)
	denom = apply(Xs^2, 1, sum)
	ro = num/denom

#-----------------------------------------------
# REPRESENTACIÓN CONJUNTA
	biplot(acp)
#-----------------------------------------------
	
	output = list(acp, VAR, R, mu, ro)
	names(output) = c("princomp", "Inercia", "R", "mu", "ro")
	output
}

#-----------------------------------------------
stand<-function(X)
{
  X = as.matrix(X)
  n = nrow(X)
  medias = apply(X, 2, mean)
  des = apply(X, 2, sd)
  des = des*sqrt((n-1)/n)
  
  Xc = X-(matrix(1, n, 1)%*%medias)
  Xs = Xc%*%diag(1/des)
  Xs
}
