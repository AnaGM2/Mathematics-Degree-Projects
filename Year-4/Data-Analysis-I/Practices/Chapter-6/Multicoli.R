Multicoli<-function(X){
  # Este programa está creado para una matriz con los datos
  # de las variables explicativas.
	p<-ncol(X)
	R2.multi<-NULL
	for (i in 1:p){
		XX<-as.data.frame(X[,-i])
		yy<-X[,i]
		R2i<-summary(lm(yy~.,data=XX))$r.squared
		R2.multi<-c(R2.multi,R2i)
	}
	output<-R2.multi
	output
}
