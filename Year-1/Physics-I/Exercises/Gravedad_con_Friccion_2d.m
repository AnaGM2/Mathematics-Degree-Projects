% Gravedad con fricción.
clc, clear all, close all

% Función cálculo derivadas.
function upunto = gravedad2d(u,t)
  % Variables globales.
  global m b g;
  upunto(1) = u(3);
  upunto(2) = u(4);
  upunto(3) = -b/m*u(3);
  upunto(4) = -g - b/m*u(4);
endfunction

% Programa principal.
global m b g;
m = 1
b = 1
g = 9.8

% Condiciones iniciales.
X0 = 0
Y0 = 0
Vx0 = 20
Vy0 = 20
u0 = [X0;Y0;Vx0;Vy0];

% Vector tiempo.
t = linspace(0, 10, 1000);

%Llamada al integrador de ecuaciones.
u = lsode("gravedad2d", u0, t);

figure(1, "position", [300,300,800,600]);
plot(u(:,1), u(:,2), 'linewidth', 3);
title('Trayectoria 2D', 'fontsize', 24);
xlabel('X (m)', 'fontsize', 24);
ylabel('Y (m)', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;

figure(2, "position", [300,300,800,600]);
plot(u(:,3), u(:,4), 'linewidth', 3);
title('Velocidad 2D', 'fontsize', 24);
xlabel('Vx (m/s)', 'fontsize', 24);
ylabel('Vy (m/s)', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;
