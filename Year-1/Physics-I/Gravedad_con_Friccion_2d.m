% GRAVEDAD CON FRICCIÓN 2D.
% Inicialización de Pantalla, Variables, Gráficos.
clc, clear all, close all

% Función para el integrador "lsode".
function upunto = gravedad2d(u,t)
  % Parámetros a compartir con el Programa Principal.
  global m b g;

  % Sistema de Ecuaciones diferenciales a resolver por el Integrador.
  upunto(1) = u(3);
  upunto(2) = u(4);
  upunto(3) = -b/m*u(3);
  upunto(4) = -g - b/m*u(4);
endfunction

% PROGRAMA PRINCIPAL

% Variables Globales (parámetros compartidos con la Función definida para el Integrador).
global m b g;

% Valores de Inicio para los Parámetros de la Función.
m = 1
b = 0
g = 9.8

% Condiciones Iniciales.
X0 = 0
Y0 = 0
Vx0 = 20
Vy0 = 20
u0 = [X0;Y0;Vx0;Vy0];

% Vector tiempo "t" (tiempo inicial, tiempo final, número de pasos de tiempo).
t = linspace(0, 10, 1000);

% Integrador (Livermore Solver for Ordinary Differential Equations).
u = lsode('gravedad2d', u0, t);

% Representaciones Gráficas.
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
