% x1 = unidades linternas de modelo básico
% x2 = unidades linternas de modelo superior

% Max 3x1+5x2
% s.a. 3x1+8x2 <= 5000
%      2x1+3x2 <= 2500
%      x1 <= 900
%      x2 <= 500
%      x1,x2 >= 0
%      x1,x2 enteros


c=[3,5]';
A=[3,8;2,3];
b=[5000,2500];
lb=[];
ub=[900,500];
ctype="UU";
vartype="II";
sense=-1;
param.presol=0;
[xopt,vopt,error,extra] = glpk(c,A,b,lb,ub,ctype,vartype,sense,param)


% Deberá fabricar 716 de modelo básico y 356 de superior.

% v(P) = 3*716 + 5*356 = 3928 euros obtendrá la empresa.