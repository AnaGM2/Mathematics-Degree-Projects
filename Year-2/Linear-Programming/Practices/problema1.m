x=[0,1,2,3,4,5]';
y=[0,2,4,3,5,8]';

n=length(x);

plot(x,y,'x');hold on;

A=[x,ones(n,1),-eye(n),eye(n)];
b=y;
ctype=repmat("S",1,n);
vtype=repmat("C",1,2+2*n);

lb=[-inf,-inf,zeros(1,2*n)];
ub=[];

c=[0,0,ones(1,2*n)];
param.presolve=0;

[xopt,fopt,error,extra]=glpk(c,A,b,lb,ub,ctype,vtype,1,param)

plot([0,5],[xopt(1)*0+xopt(2),xopt(1)*5+xopt(2)],'r')