% Péndulo.
clc, clear all, close all

% Función cálculo derivadas.
function upunto = lissajous(u,t)
  % Variables globales.
  global m k1 k2;
  upunto(1) = u(3);
  upunto(2) = u(4);
  upunto(3) = -k1/m*u(1);
  upunto(4) = -k2/m*u(2);
endfunction

% Programa principal.
global m k1 k2;
m = 1
k1 = 1
k2 = 2

% Condiciones iniciales.
u0 = [5;5;0;0]

% Vector tiempo.
t = linspace(0, 10, 1000);

%Llamada al integrador de ecuaciones.
u = lsode("lissajous", u0, t);

figure(1, "position", [300,300,800,600]);
plot3(u(:,1), u(:,2), t, "linewidth", 5);
title('Trayectoria', 'fontsize', 24);
xlabel('X(m)', 'fontsize', 24);
ylabel('V(m/s)', 'fontsize', 24);
zlabel('t(s)', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;

figure(2, "position", [300,300,800,600]);
plot(u(:,1), u(:,2), "linewidth", 5);
title('Trayectoria 2D', 'fontsize', 24);
xlabel('X(m)', 'fontsize', 24);
ylabel('V(m/s)', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;
