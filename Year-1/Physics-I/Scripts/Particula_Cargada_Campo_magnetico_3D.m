% PARTÍCULA CARGADA EN UN CAMPO MAGNÉTICO EN 3D.
% Inicialización de Pantalla, Variables, Gráficos.
clc, clear all, close all

% Función para el integrador "lsode".
function upunto = campo_b_3d(u,t)
  % Parámetros a compartir con el Programa Principal.
  global m q Bx By Bz;

  % Sistema de Ecuaciones diferenciales a resolver por el Integrador.
  upunto(1)=u(4);
  upunto(2)=u(5);
  upunto(3)=u(6);
  upunto(4)=q/m*(u(5)*Bz-u(6)*By);
  upunto(5)=q/m*(u(6)*Bx-u(4)*Bz);
  upunto(6)=q/m*(u(4)*By-u(5)*Bx);
endfunction

% PROGRAMA PRINCIPAL

% Variables Globales (parámetros compartidos con la Función definida para el Integrador).
global m q Bx By Bz;

% Valores de Inicio para los Parámetros de la Función.
m=1.67e-27      % Masa del protón en Kg.
q=1.602e-19     % Carga del protón en C.

Bx=0.15            % Componente "X" de "B" en T (Tesla).
By=0.1            % Componente "Y" de "B" en T.
Bz=0.15         % Componente "Z" de "B" en T.

% Condiciones Iniciales.
X0=0
Y0=0
Z0=0

Vx0=1e2
Vy0=1e2
Vz0=1e2

u0=[X0,Y0,Z0,Vx0,Vy0,Vz0];

% Vector tiempo "t" (tiempo inicial, tiempo final, número de pasos de tiempo).
t=linspace(0,0.000001,1000);    % Valores muy pequeños para poder ver parte de la trayectoria.

% Integrador (Livermore Solver for Ordinary Differential Equations).
u = lsode('campo_b_3d', u0, t);

% Representaciones Gráficas.
figure(1, "position", [300,300,800,600]);
plot3(u(:,1),u(:,2),u(:,3), "linewidth", 3);
title('Trayectoria 3D','fontsize',24);
xlabel('X (m)','fontsize',24);
ylabel('Y (m)','fontsize',24);
zlabel('Z (m)','fontsize',24);
set(gca, 'fontsize', 20);
grid;

figure(2, "position", [300,300,800,600]);
plot3(u(:,4),u(:,5),u(:,6), "linewidth", 3);
title('Velocidad 3D','fontsize',24);
xlabel('Vx (m/s)','fontsize',24);
ylabel('Vy (m/s)','fontsize',24);
zlabel('Vz (m/s)','fontsize',24);
set(gca, 'fontsize', 20);
grid;
