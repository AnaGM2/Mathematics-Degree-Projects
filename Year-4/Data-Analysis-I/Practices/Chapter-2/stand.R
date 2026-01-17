stand<-function(X)
{
	X = as.matrix(X)
	n = nrow(X)
	medias = apply(X,2,mean)
	des = apply(X,2,sd)
	des = des*sqrt((n-1)/n)

	Xc = X-(matrix(1,n,1)%*%medias)
	Xs = Xc%*%diag(1/des)
	Xs
}