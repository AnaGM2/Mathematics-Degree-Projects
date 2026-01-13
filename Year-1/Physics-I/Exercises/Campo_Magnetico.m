% Péndulo.
clc, clear all, close all

% Función cálculo derivadas.
function upunto = campo_B3D(u,t)
  % Variables globales.
  global m q Bx By Bz;
  upunto(1) = u(4);
  upunto(2) = u(5);
  upunto(3) = u(6);
  upunto(4) = (q/m)*(u(5)*Bz-u(6)*By);
  upunto(5) = (q/m)*(u(6)*Bx-u(4)*Bz);
  upunto(6) = (q/m)*(u(4)*By-u(5)*Bx);
endfunction

% Programa principal.
global m q Bx By Bz;

m = 1.67e-27

q = 1.602e-19

Bx = 0
By = 0
Bz = 0

X0 = 0
Y0 = 0
Z0 = 0

Vx0 = 1e5
Vy0 = 1e5
Vz0 = 1e5

% Condiciones iniciales.
u0 = [X0;Y0;Z0;Vx0;Vy0;Vz0]

% Vector tiempo.
t = linspace(0,0.00001,1000);

%Llamada al integrador de ecuaciones.
u = lsode("campo_B3D", u0, t);

figure(1, "position", [0,0,800,600]);
plot3(u(:,1), u(:,2), u(:,3));
title('Trayectoria 3D', 'fontsize', 24);
xlabel('X(m)', 'fontsize', 24);
ylabel('Y(m)', 'fontsize', 24);
zlabel('Z(m)', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;

figure(2, "position", [0,0,800,600]);
plot3(u(:,4), u(:,5), u(:,6));
title('Velocidad 3D', 'fontsize', 24);
xlabel('Vx(m/s)', 'fontsize', 24);
ylabel('Vy(m/s)', 'fontsize', 24);
zlabel('Vz(m/s)', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;
