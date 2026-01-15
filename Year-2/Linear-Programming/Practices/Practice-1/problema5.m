% x1 = litros aceite normal = 25
% x2 = garrafas (5 litros) aceite virgen extra = 57

% Max 2x1+6x2
% s.a. (1/50)x1+5(2/10)x2 <= 12
%      (3/30)x1+5(1/6)x2 <= 12
%      xi >=0
%      x2 entero


c=[2,6]';
A=[1/50,2/10;3/30,1/6];
b=[12,12];
lb=[];
ub=[];
ctype="UU";
vartype="CI";
sense=-1;
param.presol=0;
[xopt,vopt,error,extra] = glpk(c,A,b,lb,ub,ctype,vartype,sense,param)

% v(P) = 2*25 + 6*57 = 392 euros


% x1 = litros aceite normal = 24
% x2 = litros aceite virgen extra = 288

% Max 2x1+(6/5)x2
% s.a. (1/50)x1+(2/50)x2 <= 12
%      (3/30)x1+(1/30)x2 <= 12
%      xi >=0


c=[2,6/5]';
A=[1/50,2/50;3/30,1/30];
b=[12,12];
lb=[];
ub=[];
ctype="UU";
vartype="CC";
sense=-1;
param.presol=0;
[xopt,vopt,error,extra] = glpk(c,A,b,lb,ub,ctype,vartype,sense,param)

% v(P) = 2*24 + (6/5)*288 = 393.6 euros

% Conviene vender el aceite virgen extra a granel.
