% Péndulo.
clc, clear all, close all

% Función cálculo derivadas.
function upunto = pendulo(u,t)
  % Variables globales.
  global l g;
  upunto(1) = u(3);
  upunto(2) = u(4);
  upunto(3) = 0;
  upunto(4) = -g/l*sin(u(2));
endfunction

% Programa principal.
global l g;
l = 1
g = 9.8
theta0 = 75*pi/180;

% Condiciones iniciales.
u0 = [l;theta0;0;0]

% Vector tiempo.
t = linspace(0, 10, 1000);

%Llamada al integrador de ecuaciones.
u = lsode("pendulo", u0, t);

figure(1, 'position', [300,300,800,600]);
f_polar = polar(u(:,2), u(:,1));   
set(f_polar, 'linewidth', 3);      
title('Trayectoria en Coordenadas Polares - Distancia vs Ángulo', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;

figure(2, "position", [300,300,800,600]);
plot(t, u(:,2), 'linewidth', 3);
title('Ángulo vs t - Oscilación', 'fontsize', 24);
xlabel('Tiempo(s)', 'fontsize', 24);
ylabel('Theta(rad)', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;
