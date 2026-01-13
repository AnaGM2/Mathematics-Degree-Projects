% OSCILADOR ARMONICO SIMPLE + AMORTIGUADO + FORZADO (1D).
% Inicialización de Pantalla, Variables, Gráficos.
clc, clear all, close all

% Función para el integrador "lsode".
function upunto = oscilador(u,t)
  % Parámetros a compartir con el Programa Principal.
  global m k b F0 omega_f;
  
  % Sistema de Ecuaciones diferenciales a resolver por el Integrador.
  upunto(1) = u(2);
  upunto(2) = -k/m*u(1) - b/m*u(2) + F0/m*cos(omega_f*t);
endfunction

% PROGRAMA PRINCIPAL

% Variables Globales (parámetros compartidos con la Función definida para el Integrador).
global m k b F0 omega_f;

% Valores de Inicio para los Parámetros de la Función.
% "omega0" es una variable local (no está en "global").
m = 1
k = 1
b = 0
F0 = 0.1
omega0 = sqrt(k/m)
omega_f = 2*omega0

% Condiciones Iniciales.
X0 = 10
V0 = 0
u0 = [X0,V0];

% Vector tiempo "t" (tiempo inicial, tiempo final, número de pasos de tiempo).
t = linspace(0, 50, 5000);

% Integrador (Livermore Solver for Ordinary Differential Equations).
u = lsode('oscilador', u0, t);

% Representaciones Gráficas.
figure(1, 'position', [300,300,800,600]);
plot(t, u(:,1), 'linewidth', 3);
title('Posición vs Tiempo', 'fontsize', 24);
xlabel('Tiempo (s)', 'fontsize', 24);
ylabel('X (m)', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;

figure(2, 'position', [300,300,800,600]);
plot(t, u(:,2), 'linewidth', 3);
title('Velocidad vs Tiempo', 'fontsize', 24);
xlabel('Tiempo (s)', 'fontsize', 24);
ylabel('V (m/s)', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;
