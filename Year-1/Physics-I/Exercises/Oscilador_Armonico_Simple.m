% Oscilador armónico.
clc, clear all, close all

% Función cálculo derivadas.
function upunto = oscilador(u,t)
  % Variables globales.
  global m k b Fo omega1;
  upunto(1) = u(2);
  upunto(2) = 1/m*(-k*u(1) - b*u(2) + Fo*cos(omega1*t));
endfunction

% Programa principal.
global m k b Fo omega1;
m = 1
k = 2
b = 1
Fo = 1
omega0 = sqrt(k/m)
omega1 = omega0

% Condiciones iniciales.
u0 = [10,0];

% Vector tiempo.
t = linspace(0, 50, 2000);

%Llamada al integrador de ecuaciones.
u = lsode("oscilador", u0, t);

figure(1, "position", [0,0,600,400])
plot(t, u(:,1),'linewidth', 3)
title('Posición vs t', 'fontsize', 24);
xlabel('tiempo(s)', 'fontsize', 24);
ylabel('Posición X(m)', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;

figure(2, "position", [0,0,600,400])
plot(t, u,'linewidth', 3)
title('Posición y Velocidad vs t', 'fontsize', 24);
xlabel('tiempo(s)', 'fontsize', 24);
ylabel('Posición X(m) y V (m/s)', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;
legend('Posición', 'Velocidad');

figure(3, "position", [0,0,600,400])
plot(u(:,1), u(:,2),'linewidth', 3)
title('Espacio de Fase', 'fontsize', 24);
xlabel('Posición X(m)', 'fontsize', 24);
ylabel('Velocidad(m/s)', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;
