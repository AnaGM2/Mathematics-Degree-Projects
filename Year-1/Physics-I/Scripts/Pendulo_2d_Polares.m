% PENDULO 2D. COORDENADAS POLARES (rho, theta).
% Inicialización de Pantalla, Variables, Gráficos.
clc, clear all, close all

% Función para el integrador "lsode".
function upunto = pendulo(u,t)
  % Parámetros a compartir con el Programa Principal.
  global l g;
  
  % Sistema de Ecuaciones diferenciales a resolver por el Integrador.
  upunto(1) = u(3);
  upunto(2) = u(4);
  upunto(3) = 0;
  upunto(4) = -g/l*sin(u(2));
endfunction

% PROGRAMA PRINCIPAL

% Variables Globales (parámetros compartidos con la Función definida para el Integrador).
global l g;

% Valores de Inicio para los Parámetros de la Función.
l = 1
g = 9.8

% Condiciones Iniciales.
rho0 = l
theta0 = 15*pi/180  % Pasamos de grados a radianes.
u0 = [rho0;theta0;0;0];

% Vector tiempo "t" (tiempo inicial, tiempo final, número de pasos de tiempo).
t = linspace(0, 10, 1000);

% Integrador (Livermore Solver for Ordinary Differential Equations).
u = lsode('pendulo', u0, t);

% Representaciones Gráficas.
figure(1, 'position', [300,300,800,600]);
f_polar = polar(u(:,2), u(:,1));   % Función de dibujo en Coordenadas Polares. Primero el Angulo: polar(theta,r).
set(f_polar, 'linewidth', 3);      % El grosor de la línea no se admite directamente en la función "polar".
title('Trayectoria en Coordenadas Polares - Distancia vs Angulo', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;

figure(2, 'position', [300,300,800,600]);
plot(t, u(:,2), 'linewidth', 3);   % Función de dibujo normal - Oscilación.
title('Angulo vs t - Oscilación', 'fontsize', 24);
xlabel('Tiempo (s)', 'fontsize', 24);
ylabel('Theta (rad)', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;
