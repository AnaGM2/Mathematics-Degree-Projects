% x = número de soldados
% y = número de trenes

% Max (27-10-14)x+(21-9-10)y = 3x+2y
% s.a. 2x+y <= 100
%      x+y <= 80
%      x <= 40
%      x,y >= 0
%      x,y enteros


c=[3,2]';
A=[2,1;1,1];
b=[100,80];
lb=[];
ub=[40,inf];
ctype="UU";
vartype="II";
sense=-1;
param.presol=0;
[xopt,vopt,error,extra] = glpk(c,A,b,lb,ub,ctype,vartype,sense,param)

% 20 soldados y 60 trenes.

% v(P) = 3*20 + 2*60 = 180 euros.