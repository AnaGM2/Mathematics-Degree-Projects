% x1 = toneladas carga 1 compartimento delantero = 0
% x2 = toneladas carga 2 compartimento delantero = 10
% x3 = toneladas carga 3 compartimento delantero = 0
% x4 = toneladas carga 4 compartimento delantero = 0

% y1 = toneladas carga 1 compartimento central = 0
% y2 = toneladas carga 2 compartimento central = 0
% y3 = toneladas carga 3 compartimento central = 12.94737
% y4 = toneladas carga 4 compartimento central = 3.05263

% z1 = toneladas carga 1 compartimento trasero = 0
% z2 = toneladas carga 2 compartimento trasero = 5
% z3 = toneladas carga 3 compartimento trasero = 3
% z4 = toneladas carga 4 compartimento trasero = 0

% Max 310(x1+y1+z1)+380(x2+y2+z2)+350(x3+y3+z3)+285(x4+y4+z4)
% s.a. x1+x2+x3+x4 <= 10
%      y1+y2+y3+y4 <= 16
%      z1+z2+z3+z4 <= 8
%      x1+y1+z1 <= 18
%      x2+y2+z2 <= 15
%      x3+y3+z3 <= 23
%      x4+y4+z4 <= 12
%      480x1+650x2+580x3+390x4 <= 6800
%      480y1+650y2+580y3+390y4 <= 8700
%      480z1+650z2+580z3+390z4 <= 5300
%      (x1+x2+x3+x4)/10 = (y1+y2+y3+y4)/16 = (z1+z2+z3+z4)/8
%      xi,yi,ji >= 0


c=[310,380,350,285,310,380,350,285,310,380,350,285]';
A=[1,1,1,1,0,0,0,0,0,0,0,0; 0,0,0,0,1,1,1,1,0,0,0,0; 0,0,0,0,0,0,0,0,1,1,1,1; 1,0,0,0,1,0,0,0,1,0,0,0; 0,1,0,0,0,1,0,0,0,1,0,0; 0,0,1,0,0,0,1,0,0,0,1,0; 0,0,0,1,0,0,0,1,0,0,0,1; 480,650,580,390,0,0,0,0,0,0,0,0; 0,0,0,0,480,650,580,390,0,0,0,0; 0,0,0,0,0,0,0,0,480,650,580,390; 16,16,16,16,-10,-10,-10,-10,0,0,0,0; 8,8,8,8,0,0,0,0,-10,-10,-10,-10];
b=[10,16,8,18,15,23,12,6800,8700,5300,0,0];
lb=[];
ub=[];
ctype="UUUUUUUUUUSS";
vartype="CCCCCCCCCCCC";
sense=-1;
param.presol=0;
[xopt,vopt,error,extra] = glpk(c,A,b,lb,ub,ctype,vartype,sense,param)




% xij = prop de carga i en el compartimento j

% Max 18*310(x11+x12+x13)+15*380(x21+x22+x23)+23*350(x31+x32+x33)+12*285(x41+x42+x43)
% s.a. 18x11+15x21+23x31+12x41 <= 10
%      18x12+15x22+23x32+12x42 <= 16
%      18x13+15x23+23x33+12x43 <= 8
%      18*480x11+15*650x21+23*580x31+12*390x41 <= 6800
%      18*480x12+15*650x22+23*580x32+12*390x42 <= 8700
%      18*480x13+15*650x23+23*580x33+12*390x43 <= 5300
%      (18x11+15x21+23x31+12x41)/10 = (18x12+15x22+23x32+12x42)/16 = (18x13+15x23+23x33+12x43)/8
%      0 <= xij <= 1, i=1,2,3,4, j=1,2,3
%      xi1+xi2+xi3 <= 1, i=1,2,3,4