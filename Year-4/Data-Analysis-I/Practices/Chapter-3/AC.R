AC<-function(X,q=2)
{
	X<-as.matrix(X)
	n<-nrow(X)
	p<-ncol(X)
	N<-sum(X)

	if(n<p){
	X<-t(X)
	n<-nrow(X)
	p<-ncol(X)}

	f<-apply(X,1,sum)
	c<-apply(X,2,sum)
	XI<-X/matrix(f,n,p)
	XJ<-t(X)/matrix(c,p,n)
	
	MI<-diag(N/c)
	MJ<-diag(N/f)
	
	PI<-diag(f/N)
	PJ<-diag(c/N)

	gI<-c/N
	gJ<-f/N

	XIc<-XI-matrix(gI,n,p,byrow=TRUE)
	XJc<-XJ-matrix(gJ,p,n,byrow=TRUE)

	VI<-t(XIc)%*%PI%*%XIc
	CI<-MI^(1/2)%*%VI%*%MI^(1/2)
	
	values<-eigen(CI)$values
	vI<-eigen(CI)$vectors[,1:q]

################################################################
## INERCIA
	var<-values/sum(values)
	cum.var<-cumsum(var)
	VAR<-matrix(c(var,cum.var),p,2)

	values<-values[1:q]

## CÁLCULO DE LAS PUNTUACIONES
	YI<-XI%*%MI^(1/2)%*%vI
	YJ<-XJ%*%YI%*%diag(1/sqrt(values))
	colnames(YI)<-c(paste("YI",1:q))
	colnames(YJ)<-c(paste("YJ",1:q))

## CÁLCULO DE LA CONTRIBUCIÓN ABSOLUTA: alfa (de los puntos al eje)
	alfa.f<-PI%*%YI^2%*%diag(1/values)
	colnames(alfa.f)<-c(paste("CTA",1:q))
	alfa.c<-PJ%*%YJ^2%*%diag(1/values)
	colnames(alfa.c)<-c(paste("CTA",1:q))

## CÁLCULO DE LA CONTRIBUCIÓN RELATIVA: ro (calidad de representación)
	num<-YI^2
	denom<-apply(XIc^2%*%MI,1,sum)
	ro.f<-cbind(num/denom,apply(num/denom,1,sum))
	colnames(ro.f)<-c(paste("CTR",1:q),"SUMA")
	num<-YJ^2
	denom<-apply(XJc^2%*%MJ,1,sum)
	ro.c<-cbind(num/denom,apply(num/denom,1,sum))
	colnames(ro.c)<-c(paste("CTR",1:q),"SUMA")

#################################################################
#	library(MASS)
#	biplot(corresp(X,nf=q))

	FILAS<-cbind(YI,alfa.f,ro.f)
	COLUMNAS<-cbind(YJ,alfa.c,ro.c)

	output<-list(VAR,FILAS,COLUMNAS)
	names(output)<-c("INERCIA","FILAS","COLUMNAS")
	
biplot.ac(output)
output
}

biplot.ac<-function(A=A)
{
xlims=c(min(A$FILAS[,1],A$COLUMNAS[,1]),max(A$FILAS[,1],A$COLUMNAS[,1]))
ylims=c(min(A$FILAS[,2],A$COLUMNAS[,2]),max(A$FILAS[,2],A$COLUMNAS[,2]))

plot(A$FILAS[,1:2],xlim=xlims,ylim=ylims,type="n",xlab="Eje 1",ylab="Eje 2")
text(A$FILAS[,1:2], labels =rownames(A$FILAS),col="blue")
text(A$COLUMNAS[,1:2], labels =rownames(A$COLUMNAS),col=2)
}

