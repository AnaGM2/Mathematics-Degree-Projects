% x1 = kg de azufre = 800
% x2 = kg de clorato potásico = 550
% x3 = kg de carbón vegetal = 150

% Max 45(x1+x2+x3)-40x1-50x2-25x3
% s.a. x1 <= 800
%      x1 >= (20/100)(x1+x2+x3)
%      x2 >= (25/100)(x1+x2+x3)
%      x3 <= (10/100)(x1+x2+x3)
%      x1+x2+x3 >= 1500
%      x1,x2,x3 >= 0

% Max 5x1-5x2+20x3
% s.a. x1 <= 800
%      4x1-x2-x3 >= 0
%      -x1+3x2-x3 >= 0
%      -x1-x2+9x3 <= 0
%      x1+x2+x3 >= 1500
%      x1,x2,x3 >= 0


c=[5,-5,20]';
A=[4,-1,-1;-1,3,-1;-1,-1,9;1,1,1];
b=[0,0,0,1500];
lb=[];
ub=[800,inf,inf];
ctype="LLUL";
vartype="CCC";
sense=-1;
param.presol=0;
[xopt,vopt,error,extra] = glpk(c,A,b,lb,ub,ctype,vartype,sense,param)