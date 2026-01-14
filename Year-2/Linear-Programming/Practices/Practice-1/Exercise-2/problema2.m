% x = horas proceso 1 por día
% y = horas proceso 2 por día

% Min 50x+10y
% s.a. 3x+y >= 30
%      x+2y >= 20
%      x >= 5
%      x+y <= 24
%      y >= 0
%      x,y enteros


c=[50,10]';
A=[3,1;1,2;1,1];
b=[30,20,24];
lb=[5,0];
ub=[];
ctype="LLU";
vartype="II";
sense=1;
param.presol=0;
[xopt,vopt,error,extra] = glpk(c,A,b,lb,ub,ctype,vartype,sense,param)


# 5 horas proceso 1, 15 horas proceso 2.

# v(P) = 50*5 + 10*15 = 400 euros.