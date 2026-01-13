% OSCILADOR ARMÓNICO SIMPLE EN 2D.
% Inicialización de Pantalla, Variables, Gráficos.
clc, clear all, close all

% Función para el integrador "lsode".
function upunto = lissajous(u,t)
  % Parámetros a compartir con el Programa Principal.
  global m k1 k2;

  % Sistema de Ecuaciones diferenciales a resolver por el Integrador.
  upunto(1) = u(3);
  upunto(2) = u(4);
  upunto(3) = -k1/m*u(1);
  upunto(4) = -k2/m*u(2);
endfunction

% PROGRAMA PRINCIPAL

% Variables Globales (parámetros compartidos con la Función definida para el Integrador).
global m k1 k2;

% Valores de Inicio para los Parámetros de la Función.
m=1

% Condiciones Iniciales.
A=5
B=2
a=23
b=19
delta=pi/7

k1=a^2*m
k2=b^2*m

X0=A*sin(delta)
Y0=0
Vx0=a*A*cos(delta)
Vy0=b*B

u0=[X0,Y0,Vx0,Vy0];

% Vector tiempo "t" (tiempo inicial, tiempo final, número de pasos de tiempo).
t = linspace(0, 10, 1000);

% Integrador (Livermore Solver for Ordinary Differential Equations).
u = lsode('lissajous', u0, t);

% Representaciones Gráficas.
figure(1, "position", [300,300,800,600]);
plot3(u(:,1),u(:,2),t, "linewidth", 3);
title('Trayectoria 3D','fontsize',24);
xlabel('X(m)','fontsize',24);
ylabel('Y(m)','fontsize',24);
zlabel('t(s)','fontsize',24);
set(gca, 'fontsize', 20);
grid;

figure(2, "position", [300,300,800,600]);
plot(u(:,1), u(:,2), 'linewidth', 3);
title('Trayectoria 2D', 'fontsize', 24);
xlabel('X (m)', 'fontsize', 24);
ylabel('Y (m)', 'fontsize', 24);
set(gca, 'fontsize', 20);
grid;
