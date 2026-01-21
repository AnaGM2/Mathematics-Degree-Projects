#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:16:10 2024

@author: gilpe
"""

import scipy.io as scio
file =  scio.loadmat("C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/datos_SAT_ERA5_reducidos.mat")
t2m = file["t2m"][:] # temperatura del aire a 2m sobre el nivel del mar en grados centigrados, 3D (time, latitude, longitude)
time = file["time"][:][0] ## dias desde 1940-01-01 hasta marzo de 2024
longitude = file["longitude"][:][0] ## en grados
latitude = file["latitude"][:][0]  ## en grados


##################################################
### Dibujamos el mapa de temperatura promedio ###
#################################################

import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.crs as ccrs
import numpy as np
import matplotlib.pyplot as plt

lon,lat = np.meshgrid(longitude,latitude) ## pasamos de un vector a una array
 
latmax = 90
latmin = -90
lonmin = -180
lonmax = 180

img_extent = (lonmin, lonmax, latmin, latmax)

fig = plt.figure(figsize=(20,16))
fig.subplots_adjust(wspace=0.3,hspace=0.1)

ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree(central_longitude=0))
bounds = np.arange(-10,30,1)
cs =ax.coastlines(resolution='50m', color='black', linewidth=1)
ax.set_extent(img_extent)
font = {'fontname':'Cosm5ic Sans','fontsize':19}

cs=ax.pcolormesh(lon,lat,np.nanmean(t2m,0), cmap="tab20b",transform=ccrs.PlateCarree(),vmin=-10,vmax=30)
cbar_ax = fig.add_axes([0.18, 0.9, 0.68, 0.03]) # left,bottom,width,height
cbar=plt.colorbar(cs,cax=cbar_ax,orientation='horizontal',boundaries=bounds,ticks=bounds[::2],extend='both',drawedges=True,format=r"%d")
cbar.set_label(r"Temperatura del aire [$^{\circ} C$]",labelpad=-85,rotation=0,fontsize=20) 
cbar.dividers.set_linewidths(1)
cbar.outline.set_lw(2)
cbar.solids.set_rasterized(True) 
cbar.ax.yaxis.set_ticks_position('right')
for t in cbar.ax.get_xticklabels():
    t.set_fontsize(19)
    t.set_fontweight('bold')

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_left = False
gl.ylabels_right = False
gl.ylabels_left = True
gl.xlines = True
gl.xlocator = mticker.FixedLocator([-150,-120,-90,-60,-30,0,30,60,90,120,150])
gl.ylocator = mticker.FixedLocator([-80,-60,-40,-20,0,20,40,60,80])

gl.xlabel = True
gl.ylabel = True

gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {'size': 20, 'color': 'k','style': 'italic'}
gl.ylabel_style = {'size': 20, 'color': 'k','style': 'italic'}        
plt.show()


#################################################################
### Regresión lineal para eliminar tendencia lineal (con nan) ###
#################################################################

import scipy.stats as scst
t2m_detrended = t2m.copy() ## aqui almacenamos los datos de temperatura sin tendencia lineal
# Para cada punto de latitud y longitud, ajustar el modelo y eliminar la tendencia lineal
for i in range(len(latitude)):
    for j in range(len(longitude)):
       
        mask = ~np.isnan(t2m[:,i,j])
        serie = t2m[:,i,j]        
        slope, intercept, r_value, p_value, std_err = scst.linregress(time[mask], serie[mask])
        t2m_detrended[:,i,j] = t2m[:,i,j] - (slope*time)
       

##############################################
### Eliminar ciclos estacionales (con nan) ###
##############################################

t2m_det_des = t2m_detrended.copy()  ## aqui almacenamos los datos de temperatura sin tendencia lineal ni ciclo estacional
seasonal_cycle = np.zeros((12,len(latitude),len(longitude))) ## aqui guardamos los ciclos estacionales de todos los puntos
# Para cada punto de latitud y longitud, ajustar el modelo y eliminar el ciclo estacional
for i in range(len(latitude)):
    for j in range(len(longitude)):
        for k in range(0,12):
       
            seasonal_cycle[k,i,j] = np.nanmean(t2m_detrended[k::12,i,j])
            t2m_det_des[k::12,i,j] = t2m_detrended[k::12,i,j] - seasonal_cycle[k,i,j]
            
            
# Gráfico (para una latitud y una longitud concretas)
plt.figure(figsize=(10, 6))
plt.plot(time, t2m_det_des[:,0,0], color='blue')
plt.title('Temperatura a lo largo del tiempo')
plt.xlabel('Días')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.show()


#####################################################
### Interpolación lineal para estimar valores nan ###
#####################################################

t2m  # array de datos con valores nan

# Reemplazar nan con interpolación lineal a lo largo del tiempo
for i in range(len(latitude)):
    for j in range(len(longitude)):
        # Obtener los datos de temperatura para la latitud y longitud específicas
        temperatura = t2m[:, i, j]
        # Realizar interpolación lineal
        temperatura_interp = np.interp(np.arange(len(temperatura)), 
                                        np.arange(len(temperatura))[~np.isnan(temperatura)],
                                        temperatura[~np.isnan(temperatura)])
        # Reemplazar los valores nan con la interpolación lineal
        t2m[:, i, j] = np.where(np.isnan(t2m[:, i, j]), temperatura_interp, t2m[:, i, j])


#################################################################
### Regresión lineal para eliminar tendencia lineal (sin nan) ###
#################################################################

# Tendencia lineal: cambios en la temperatura a medida que pasa el tiempo
# Causas: calentamiento global, ciclos climáticos a largo plazo, etc

from sklearn.linear_model import LinearRegression

# Crear un modelo de regresión lineal
lr = LinearRegression()

# Variable dependiente y: temperatura (t2m)
# Variable independiente X: tiempo (time)

# Las variables independientes deben estar en una matriz en la que cada fila representa
# una muestra, y cada columna una característica:
X = time.reshape(-1, 1)  

# Para cada punto de latitud y longitud, ajustar el modelo y eliminar la tendencia lineal
for i in range(len(latitude)):
    for j in range(len(longitude)):
        # Obtener los datos de temperatura para la latitud y longitud específicas
        y = t2m[:, i, j] 
        # Ajustar el modelo de regresión lineal
        lr.fit(X, y)  
        # Eliminar la tendencia lineal
        tendencia_lineal = lr.predict(X)
        t2m[:, i, j] = t2m[:, i, j] - tendencia_lineal  


##########################################################################
### Descomposición estacional para eliminar ciclo estacional (sin nan) ###
##########################################################################

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(time[0:20], t2m[:,0,0][0:20], color='blue')
plt.title('Temperatura a lo largo del tiempo')
plt.xlabel('Días')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.show()

# En la anterior representación se observa que el periodo es de 365 días.
time
# La variable time va de 30 en 30 días aproximadamente.
# Debemos tomar un periodo de 12 para hacer la descomposición estacional.

import statsmodels.api as sm

# Para cada punto de latitud y longitud, hacer la descomposición estacional y eliminar el ciclo estacional
for i in range(len(latitude)):
    for j in range(len(longitude)):
        # Descomposición estacional con periodo de 12
        descomposicion = sm.tsa.seasonal_decompose(t2m[:, i, j] , period=12)
        
        # Eliminar el ciclo estacional
        estacionalidad = descomposicion.seasonal
        t2m[:, i, j] = t2m[:, i, j] - estacionalidad

# Gráfico (para una latitud y una longitud concretas)
plt.figure(figsize=(10, 6))
plt.plot(time, t2m[:,0,0], color='blue')
plt.title('Temperatura a lo largo del tiempo')
plt.xlabel('Días')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.show()

# Ya no se aprecian tendencia lineal ni ciclo estacional


############################################
### Cálculo de Sij con Pearson con lag=0 ###
############################################

from scipy.stats import pearsonr

# Con 4 bucles:

# Diccionarios para almacenar el coeficiente de Pearson y el p_valor para cada par de series
S_pearson = {}
p_values_pearson = {}

for i in range(len(latitude)):
    for j in range(len(longitude)):
        serie1 = t2m[:, i, j]
        for k in range(i, len(latitude)):
            for l in range(j, len(longitude)):
                serie2 = t2m[:, k, l]
                coef_pearson, p_value = pearsonr(serie1, serie2)
                S_pearson[((i, j), (k, l))] = coef_pearson
                p_values_pearson[((i, j), (k, l))] = p_value

# Con 2 bucles:
    
nx = len(longitude)
ny = len(latitude)
S_pearson = np.zeros((ny*nx,ny*nx))
p_values_pearson =np.zeros((ny*nx,ny*nx))

t2m_reshape = np.reshape(t2m_det_des,[len(time),nx*ny])

for k in range(0,ny*nx):
    for j in range(0,ny*nx):

           serie1 = t2m_reshape[:, k]
           serie2 = t2m_reshape[:, j]
           msk = (~np.isnan(serie1) & ~np.isnan(serie2))
           coef_pearson, p_value = pearsonr(serie1[msk], serie2[msk])
           S_pearson[k, j] = coef_pearson
           p_values_pearson[k,j] = p_value
               
           print(k,j) 
             
# Guardar en un archivo .npy
# np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/S_pearson.npy', S_pearson)
# np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/p_values_pearson.npy', p_values_pearson)

# Cargar las matrices desde archivos .npy
S_pearson = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/S_pearson.npy')
p_values_pearson = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/p_values_pearson.npy')

# Expandir a 4D         
original_shape = (ny, nx, ny, nx)
expanded_S_pearson = np.reshape(S_pearson, original_shape)
expanded_p_values_pearson = np.reshape(p_values_pearson, original_shape)
    

#############################################
### Cálculo de Sij con Spearman con lag=0 ###
#############################################

from scipy.stats import spearmanr

# Con 4 bucles

# Diccionarios para almacenar el coeficiente de Spearman y el p_valor para cada par de series
S_spearman = {}
p_values_spearman = {}

for i in range(len(latitude)):
    for j in range(len(longitude)):
        serie1 = t2m[:, i, j]
        for k in range(i, len(latitude)):
            for l in range(j, len(longitude)):
                serie2 = t2m[:, k, l]
                coef_spearman, p_value = spearmanr(serie1, serie2)
                S_spearman[((i, j), (k, l))] = coef_spearman
                p_values_spearman[((i, j), (k, l))] = p_value
                
# Con 2 bucles:
    
nx = len(longitude)
ny = len(latitude)
S_spearman = np.zeros((ny*nx,ny*nx))
p_values_spearman =np.zeros((ny*nx,ny*nx))

t2m_reshape = np.reshape(t2m_det_des,[len(time),nx*ny])

for k in range(0,ny*nx):
    for j in range(0,ny*nx):

           serie1 = t2m_reshape[:, k]
           serie2 = t2m_reshape[:, j]
           msk = (~np.isnan(serie1) & ~np.isnan(serie2))
           coef_spearman, p_value = spearmanr(serie1[msk], serie2[msk])
           S_spearman[k, j] = coef_spearman
           p_values_spearman[k,j] = p_value
               
           print(k,j) 
           
# Guardar en un archivo .npy
# np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/S_spearman.npy', S_spearman)
# np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/p_values_spearman.npy', p_values_spearman)

# Cargar las matrices desde archivos .npy
S_spearman = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/S_spearman.npy')
p_values_spearman = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/p_values_spearman.npy')
                      
# Expandir a 4D
original_shape = (ny, nx, ny, nx)
expanded_S_spearman = np.reshape(S_spearman, original_shape)
expanded_p_values_spearman = np.reshape(p_values_spearman, original_shape)


#############################################
### Cálculo de Sij con Pearson con lag=12 ###
#############################################

from scipy.stats import pearsonr

# Con 4 bucles:

# Diccionarios para almacenar el coeficiente de Pearson y el p_valor para cada par de series
S_pearson_lag12 = {}
p_values_pearson_lag12 = {}

lag = 12

for i in range(len(latitude)):
    for j in range(len(longitude)):
        serie1 = t2m[:-lag, i, j]  # Quitar los últimos 12 valores de la serie 1
        for k in range(len(latitude)):
            for l in range(len(longitude)):
                serie2 = t2m[lag:, k, l]  # Ajustar la serie 2 para comenzar desde el índice 12
                coef_pearson, p_value = pearsonr(serie1, serie2)
                S_pearson_lag12[((i, j), (k, l))] = coef_pearson
                p_values_pearson_lag12[((i, j), (k, l))] = p_value

# Con 2 bucles:
    
nx = len(longitude)
ny = len(latitude)
S_pearson_lag12 = np.zeros((ny*nx,ny*nx))
p_values_pearson_lag12 =np.zeros((ny*nx,ny*nx))

t2m_reshape = np.reshape(t2m_det_des,[len(time),nx*ny])

lag = 12

for k in range(0,ny*nx):
    for j in range(0,ny*nx):

           serie1 = t2m_reshape[:-lag, k]
           serie2 = t2m_reshape[lag:, j]
           msk = (~np.isnan(serie1) & ~np.isnan(serie2))
           coef_pearson, p_value = pearsonr(serie1[msk], serie2[msk])
           S_pearson_lag12[k, j] = coef_pearson
           p_values_pearson_lag12[k,j] = p_value
               
           print(k,j) 

# Guardar en un archivo .npy
# np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/S_pearson_lag12.npy', S_pearson_lag12)
# np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/p_values_pearson_lag12.npy', p_values_pearson_lag12)

# Cargar las matrices desde archivos .npy
S_pearson_lag12 = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/S_pearson_lag12.npy')
p_values_pearson_lag12 = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/p_values_pearson_lag12.npy')
                      
# Expandir a 4D         
original_shape = (ny, nx, ny, nx)
expanded_S_pearson_lag12 = np.reshape(S_pearson_lag12, original_shape)
expanded_p_values_pearson_lag12 = np.reshape(p_values_pearson_lag12, original_shape)


##############################################
### Cálculo de Sij con Spearman con lag=12 ###
##############################################

from scipy.stats import spearmanr

# Con 4 bucles:

# Diccionarios para almacenar el coeficiente de Pearson y el p_valor para cada par de series
S_spearman_lag12 = {}
p_values_spearman_lag12 = {}

lag = 12

for i in range(len(latitude)):
    for j in range(len(longitude)):
        serie1 = t2m[:-lag, i, j]  # Quitar los últimos 12 valores de la serie 1
        for k in range(len(latitude)):
            for l in range(len(longitude)):
                serie2 = t2m[lag:, k, l]  # Ajustar la serie 2 para comenzar desde el índice 12
                coef_spearman, p_value = spearmanr(serie1, serie2)
                S_spearman_lag12[((i, j), (k, l))] = coef_spearman
                p_values_spearman_lag12[((i, j), (k, l))] = p_value

# Con 2 bucles:
    
nx = len(longitude)
ny = len(latitude)
S_spearman_lag12 = np.zeros((ny*nx,ny*nx))
p_values_spearman_lag12 = np.zeros((ny*nx,ny*nx))

t2m_reshape = np.reshape(t2m_det_des,[len(time),nx*ny])

lag = 12

for k in range(0,ny*nx):
    for j in range(0,ny*nx):

           serie1 = t2m_reshape[:-lag, k]
           serie2 = t2m_reshape[lag:, j]
           msk = (~np.isnan(serie1) & ~np.isnan(serie2))
           coef_spearman, p_value = spearmanr(serie1[msk], serie2[msk])
           S_spearman_lag12[k, j] = coef_spearman
           p_values_spearman_lag12[k,j] = p_value
               
           print(k,j) 
        
# Guardar en un archivo .npy
# np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/S_spearman_lag12.npy', S_spearman_lag12)
# np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/p_values_spearman_lag12.npy', p_values_spearman_lag12)

# Cargar las matrices desde archivos .npy
S_spearman_lag12 = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/S_spearman_lag12.npy')
p_values_spearman_lag12 = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/p_values_spearman_lag12.npy')
              
# Expandir a 4D
original_shape = (ny, nx, ny, nx)
expanded_S_spearman_lag12 = np.reshape(S_spearman_lag12, original_shape)
expanded_p_values_spearman_lag12 = np.reshape(p_values_spearman_lag12, original_shape)


####################################################################
### Cálculo de la matriz de adyacencia A con Pearson con lag = 0 ###
####################################################################

# Elegimos coeficiente de correlación
S = expanded_S_pearson

# Fijamos un umbral
W = 0.5
 
# Matriz de adyacencia: Aij = H(Sij - W)

# Función de Heaviside: H(x) = 0 si x < 0, H(x) = 1 si x >= 0

def H(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1
    
# Inicializar la matriz de adyacencia
A_pearson_abs = np.zeros_like(expanded_S_pearson)

# Rellenar la matriz de adyacencia
for i in range(ny):
    for j in range(nx):
        for k in range(ny):
            for l in range(nx):
                A_pearson_abs[i, j, k, l] = H(abs(expanded_S_pearson[i, j, k, l]) - W)

# np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/A_pearson_abs.npy', A_pearson_abs)

A_pearson_abs = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/A_pearson_abs.npy')


#####################################################################
### Cálculo de la matriz de adyacencia A con Spearman con lag = 0 ###
#####################################################################

# Elegimos coeficiente de correlación
S = expanded_S_spearman

# Fijamos un umbral
W = 0.5

# Inicializar la matriz de adyacencia
A_spearman_abs = np.zeros_like(expanded_S_spearman)

# Rellenar la matriz de adyacencia
for i in range(ny):
    for j in range(nx):
        for k in range(ny):
            for l in range(nx):
                A_spearman_abs[i, j, k, l] = H(abs(expanded_S_spearman[i, j, k, l]) - W)
    
# np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/A_spearman_abs.npy', A_spearman_abs)

A_spearman_abs = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/A_spearman_abs.npy')

    
#####################################################################
### Cálculo de la matriz de adyacencia A con Pearson con lag = 12 ###
#####################################################################

# Elegimos coeficiente de correlación
S = expanded_S_pearson_lag12

# Fijamos un umbral
W = 0.5

# Inicializar la matriz de adyacencia
A_pearson_lag12_abs = np.zeros_like(expanded_S_pearson_lag12)

# Rellenar la matriz de adyacencia
for i in range(ny):
    for j in range(nx):
        for k in range(ny):
            for l in range(nx):
                A_pearson_lag12_abs[i, j, k, l] = H(abs(expanded_S_pearson_lag12[i, j, k, l]) - W)
    
np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/A_pearson_lag12_abs.npy', A_pearson_lag12_abs)

A_pearson_lag12_abs = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/A_pearson_lag12_abs.npy')

    
######################################################################
### Cálculo de la matriz de adyacencia A con Spearman con lag = 12 ###
######################################################################

# Elegimos coeficiente de correlación
S = expanded_S_spearman_lag12

# Fijamos un umbral
W = 0.5

# Inicializar la matriz de adyacencia
A_spearman_lag12_abs = np.zeros_like(expanded_S_spearman_lag12)

# Rellenar la matriz de adyacencia
for i in range(ny):
    for j in range(nx):
        for k in range(ny):
            for l in range(nx):
                A_spearman_lag12_abs[i, j, k, l] = H(abs(expanded_S_spearman_lag12[i, j, k, l]) - W)
    
np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/A_spearman_lag12_abs.npy', A_spearman_lag12_abs)

A_spearman_lag12_abs = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/A_spearman_lag12_abs.npy')


#################################################################
### Propiedades de la red a partir de la matriz de adyacencia ###
#################################################################

# Elegimos matriz de adyacencia
A = A_pearson_abs

# Observación: las correlaciones de Pearson y de Spearman son simétricas,
# luego la red que estamos construyendo es no dirigida

# Con la biblioteca NetworkX, podemos obtener un grafo a partir de A
import networkx as nk

# Crear un grafo no dirigido
G = nk.Graph()

# Añadir nodos al grafo
for i in range(ny):
    for j in range(nx):
        G.add_node((i, j))
        
# Añadir aristas al grafo
for i in range(ny):
    for j in range(nx):
        for k in range(ny):
            for l in range(nx):
                if A[i, j, k, l] == 1:
                    G.add_edge((i, j), (k, l))
                    
                    
## LONGITUD DEL CAMINO MÁS CORTO ##

# Elegimos nodo inicial
i1 = 0
j1 = 0

# Elegimos nodo final
i2 = 1
j2 = 1

# Longitud del camino más corto entre estos dos nodos
shortest_path_length = nk.shortest_path_length(G, source=(i1, j1), target=(i2, j2))

# Longitud del camino más corto promedio entre todos los pares de nodos
avg_shortest_path_length = nk.average_shortest_path_length(G)


## GRADO DE UN NODO ##

# Función para calcular el grado de un nodo específico
def grado_nodo(i, j, A):
    """
    Parameters
    ----------
    i : latitud del nodo
    j : longitud del nodo
    A : matriz de adyacencia

    Returns
    -------
    grado : grado del nodo

    """
    grado = 0
    for k in range(ny):
        for l in range(nx):
            if A[i, j, k, l] == 1:
                grado += 1
    return grado

# Matriz para almacenar los grados de todos los nodos
grados = np.zeros((ny, nx))

# Calcular el grado de cada nodo en la red
for i in range(ny):
    for j in range(nx):
        grados[i, j] = grado_nodo(i, j, A)
             
# Calcular el grado de los nodos con NetworkX
grados = dict(nk.degree(G))              


## CENTRALIDAD DE CERCANÍA ##

# Centralidad de cercanía para cada nodo
closeness_centrality = nk.closeness_centrality(G)


## CENTRALIDAD DE INTERMEDIACIÓN ##

# Centralidad de intermediación para cada nodo
betweenness_centrality = nk.betweenness_centrality(G)


## DISTRIBUCIÓN DE GRADO ##

# Obtener la distribución de grado
degree_distribution = [d for n, d in G.degree()]

# Calcular la mediana y la desviación estándar
median_degree = np.median(degree_distribution)
std_dev_degree = np.std(degree_distribution)

# Graficar el histograma de la distribución de grados
plt.hist(degree_distribution, bins='auto',color='b')

# Añadir líneas verticales para la mediana y la desviación estándar
plt.axvline(x=median_degree, color='red', linestyle='--', label=f'Mediana: {median_degree}')
plt.axvline(x=median_degree + std_dev_degree, color='lime', linestyle='--', label=f'Mediana + Desv. Estándar: {median_degree + std_dev_degree:.2f}')
plt.axvline(x=median_degree - std_dev_degree, color='lime', linestyle='--', label=f'Mediana - Desv. Estándar: {median_degree - std_dev_degree:.2f}')

plt.title("Distribución de Grado con Pearson", fontsize=20, y=1.03)
plt.xlabel("Grado")
plt.ylabel("Frecuencia")
plt.legend()
plt.xlim(-150, 1200)
plt.ylim(0, 1400)
plt.show()


## COEFICIENTE DE AGRUPAMIENTO  ##

# Coeficiente de agrupamiento para cada nodo
clustering_coefficient = nk.clustering(G)

# Coeficiente de agrupamiento promedio de Watts-Strogatz
clustering_global = nk.average_clustering(G)


## DIÁMETRO DE LA RED ##

# Debemos comprobar primero si la red está conectada
nk.is_connected(G)

# En caso afirmativo, entonces calculamos el diámetro
diameter = nk.diameter(G)


## COMPONENTES CONECTADAS ##

connected_components = list(nk.connected_components(G))


#################################################
### Mapas a partir de la matriz de adyacencia ###
#################################################

# Elegimos matriz de adyacencia
A = A_pearson_abs

# Primeras pruebas
plt.pcolormesh(A[0,0]), plt.colorbar()
latitude[0],longitude[0]  
plt.pcolormesh(longitude,latitude,A[30,40]), plt.colorbar()

import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from matplotlib.colors import ListedColormap

# Número total de latitudes y longitudes
n = len(latitude)  
m = len(longitude)

# Función para convertir latitud/longitud a índices
def get_indices(lat, lon, latmin, latmax, lonmin, lonmax, n, m):
    lat_idx = int((lat - latmin) / (latmax - latmin) * (n - 1))
    lon_idx = int((lon - lonmin) / (lonmax - lonmin) * (m - 1))
    return lat_idx, lon_idx

# Extensión de la imagen
latmin, latmax = -90, 90
lonmin, lonmax = -180, 180

# Crear la cuadrícula de coordenadas para pcolormesh
lats = np.linspace(latmin, latmax, n)
lons = np.linspace(lonmin, lonmax, m)
lon_grid, lat_grid = np.meshgrid(lons, lats)

# Definir una paleta de colores discreta
cmap = ListedColormap(['blue', 'yellow'])


## POLO NORTE ##

# Coordenadas del Polo Norte
lat_pn, lon_pn = 90, 0
lat_idx_pn, lon_idx_pn = get_indices(lat_pn, lon_pn, latmin, latmax, lonmin, lonmax, n, m)

fig_pn = plt.figure(figsize=(20, 16))
ax_pn = plt.axes(projection=ccrs.PlateCarree())
ax_pn.set_extent([lonmin, lonmax, latmin, latmax])
ax_pn.coastlines(resolution='50m')

plt.pcolormesh(lon_grid, lat_grid, A[lat_idx_pn, lon_idx_pn], cmap=cmap, transform=ccrs.PlateCarree(), shading='auto')
plt.colorbar(ticks=[0, 1])
plt.title("Red de temperatura en el Polo Norte con Spearman",fontsize=35,pad=30)

gl_pn = ax_pn.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                        linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl_pn.xlabels_top = False
gl_pn.ylabels_left = True
gl_pn.ylabels_right = False
gl_pn.xlines = True
gl_pn.xlocator = mticker.FixedLocator([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150])
gl_pn.ylocator = mticker.FixedLocator([-80, -60, -40, -20, 0, 20, 40, 60, 80])

gl_pn.xlabel = True
gl_pn.ylabel = True

gl_pn.xformatter = LONGITUDE_FORMATTER
gl_pn.yformatter = LATITUDE_FORMATTER
gl_pn.xlabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}
gl_pn.ylabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}        

plt.show()


## ECUADOR ##

# Coordenadas del Ecuador
lat_eq, lon_eq = 0, 0
lat_idx_eq, lon_idx_eq = get_indices(lat_eq, lon_eq, latmin, latmax, lonmin, lonmax, n, m)

fig_eq = plt.figure(figsize=(20, 16))
ax_eq = plt.axes(projection=ccrs.PlateCarree())
ax_eq.set_extent([lonmin, lonmax, latmin, latmax])
ax_eq.coastlines(resolution='50m')

plt.pcolormesh(lon_grid, lat_grid, A[lat_idx_eq, lon_idx_eq], cmap=cmap, transform=ccrs.PlateCarree(), shading='auto')
plt.colorbar(ticks=[0, 1])
plt.title("Red de temperatura en el Ecuador con Pearson",fontsize=35,pad=30)

gl_eq = ax_eq.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                        linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl_eq.xlabels_top = False
gl_eq.ylabels_left = True
gl_eq.ylabels_right = False
gl_eq.xlines = True
gl_eq.xlocator = mticker.FixedLocator([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150])
gl_eq.ylocator = mticker.FixedLocator([-80, -60, -40, -20, 0, 20, 40, 60, 80])

gl_eq.xlabel = True
gl_eq.ylabel = True

gl_eq.xformatter = LONGITUDE_FORMATTER
gl_eq.yformatter = LATITUDE_FORMATTER
gl_eq.xlabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}
gl_eq.ylabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}        

plt.show()


## NUEVA YORK ##

# Coordenadas de Nueva York
lat_ny, lon_ny = 40.7128, -74.0060
lat_idx_ny, lon_idx_ny = get_indices(lat_ny, lon_ny, latmin, latmax, lonmin, lonmax, n, m)

fig_ny = plt.figure(figsize=(20, 16))
ax_ny = plt.axes(projection=ccrs.PlateCarree())
ax_ny.set_extent([lonmin, lonmax, latmin, latmax])
ax_ny.coastlines(resolution='50m')

plt.pcolormesh(lon_grid, lat_grid, A[lat_idx_ny, lon_idx_ny], cmap=cmap, transform=ccrs.PlateCarree(), shading='auto')
plt.colorbar(ticks=[0, 1])
plt.title("Red de temperatura en Nueva York con Pearson",fontsize=35,pad=30)

gl_ny = ax_ny.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                        linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl_ny.xlabels_top = False
gl_ny.ylabels_left = True
gl_ny.ylabels_right = False
gl_ny.xlines = True
gl_ny.xlocator = mticker.FixedLocator([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150])
gl_ny.ylocator = mticker.FixedLocator([-80, -60, -40, -20, 0, 20, 40, 60, 80])

gl_ny.xlabel = True
gl_ny.ylabel = True

gl_ny.xformatter = LONGITUDE_FORMATTER
gl_ny.yformatter = LATITUDE_FORMATTER
gl_ny.xlabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}
gl_ny.ylabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}        

plt.show()


## MADRID ##

# Coordenadas de Madrid
lat_madrid = 40.4168
lon_madrid = -3.7038

# Calcular los índices de la matriz A para Madrid
lat_idx_madrid, lon_idx_madrid = get_indices(lat_madrid, lon_madrid, latmin, latmax, lonmin, lonmax, n, m)

# Crear una nueva figura para Madrid
fig_madrid = plt.figure(figsize=(20, 16))
ax_madrid = plt.axes(projection=ccrs.PlateCarree())
ax_madrid.set_extent([lonmin, lonmax, latmin, latmax])
ax_madrid.coastlines(resolution='50m')

# Usar pcolormesh con la cuadrícula de coordenadas
plt.pcolormesh(lon_grid, lat_grid, A[lat_idx_madrid, lon_idx_madrid], cmap=cmap, transform=ccrs.PlateCarree(), shading='auto')
plt.colorbar(ticks=[0, 1])
plt.title("Red de temperatura en Madrid con Pearson",fontsize=35,pad=30)

# Configurar las líneas de cuadrícula
gl_madrid = ax_madrid.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                                linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl_madrid.xlabels_top = False
gl_madrid.ylabels_left = True
gl_madrid.ylabels_right = False
gl_madrid.xlines = True
gl_madrid.xlocator = mticker.FixedLocator([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150])
gl_madrid.ylocator = mticker.FixedLocator([-80, -60, -40, -20, 0, 20, 40, 60, 80])

gl_madrid.xlabel = True
gl_madrid.ylabel = True

gl_madrid.xformatter = LONGITUDE_FORMATTER
gl_madrid.yformatter = LATITUDE_FORMATTER
gl_madrid.xlabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}
gl_madrid.ylabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}        

plt.show()


#################################################
### Redes a partir de la matriz de adyacencia ###
#################################################

import networkx as nx


## POLO NORTE ##

nodo_seleccionado = (lat_idx_pn, lon_idx_pn)


## ECUADOR ##

nodo_seleccionado = (lat_idx_eq, lon_idx_eq)


## NUEVA YORK ##

nodo_seleccionado = (lat_idx_ny, lon_idx_ny)


## MADRID ##

nodo_seleccionado = (lat_idx_madrid, lon_idx_madrid) 

# Obtener las conexiones del nodo seleccionado
conexiones_nodo_seleccionado = [(i, j) for i in range(A.shape[0]) for j in range(A.shape[1]) if A[nodo_seleccionado[0], nodo_seleccionado[1], i, j] == 1]

# Crear el grafo solo para el nodo seleccionado y sus conexiones
G = nx.Graph()
G.add_edges_from(conexiones_nodo_seleccionado)

# Fijar la disposición de los nodos
fixed_positions = nx.spring_layout(G, seed=1)

# Dibujar el grafo
plt.figure(figsize=(20, 16))
nx.draw(G, pos=fixed_positions, with_labels=True, node_color='black', node_size=700, edge_color='gray',font_color='white')
plt.title(f"Red para el nodo seleccionado: {nodo_seleccionado}")
plt.show()


############################
### Diámetros en el mapa ###
############################

# Calcular el diámetro para cada subgrafo
diametros = []
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        conexiones_nodo = [(k, l) for k in range(A.shape[2]) for l in range(A.shape[3]) if A[i, j, k, l] == 1]
        G = nx.Graph()
        G.add_edges_from(conexiones_nodo)
        if nx.is_connected(G):  # Verificar si el grafo es conexo (si no, asignar NaN)
            diametro = nx.diameter(G)
            diametros.append((latitude[i], longitude[j], diametro))
        else:
            diametros.append((latitude[i], longitude[j], np.nan))
            
# Pearson
#np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/diametros_pearson.npy', diametros)
diametros = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/diametros_pearson.npy')

# Spearman
#np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/diametros_spearman.npy', diametros)
diametros = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/diametros_spearman.npy')

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER


## CON CÍRCULOS ##

# Crear arrays de latitudes y longitudes
latitudes = [d[0] for d in diametros]
longitudes = [d[1] for d in diametros]
values = [d[2] for d in diametros]

# Configuración de los límites del mapa
latmax = 90
latmin = -90
lonmin = -180
lonmax = 180
img_extent = (lonmin, lonmax, latmin, latmax)

# Crear la figura y el eje con la proyección PlateCarree
fig = plt.figure(figsize=(20, 16))
fig.subplots_adjust(wspace=0.3, hspace=0.1)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=0))

# Añadir características del mapa
ax.coastlines(resolution='50m', color='black', linewidth=1)
ax.set_extent(img_extent)

# Normalizar los diámetros para mapearlos a un rango de colores
norm = plt.Normalize(min(values), max(values))
cmap = plt.get_cmap('viridis')

# Añadir puntos en el mapa
sc = ax.scatter(longitudes, latitudes, c=values, s=np.array(values)*10, cmap=cmap, norm=norm, edgecolor='k', alpha=0.7, transform=ccrs.PlateCarree())

# Añadir colorbar
bounds = np.linspace(min(values), max(values), 10)
cbar_ax = fig.add_axes([0.18, 0.91, 0.68, 0.03])  # left, bottom, width, height
cbar = plt.colorbar(sc, cax=cbar_ax, orientation='horizontal', boundaries=bounds, ticks=bounds, extend='both', drawedges=True, format=r"%d")
cbar.set_label(r"Diámetro de las Redes con Spearman", labelpad=-85, rotation=0, fontsize=20)
cbar.dividers.set_linewidths(1)
cbar.outline.set_lw(2)
cbar.solids.set_rasterized(True)
cbar.ax.yaxis.set_ticks_position('right')
for t in cbar.ax.get_xticklabels():
    t.set_fontsize(19)
    t.set_fontweight('bold')

# Configuración de las líneas de la cuadrícula
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_left = True
gl.ylabels_right = False
gl.xlines = True
gl.xlocator = mticker.FixedLocator([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150])
gl.ylocator = mticker.FixedLocator([-80, -60, -40, -20, 0, 20, 40, 60, 80])

gl.xlabel = True
gl.ylabel = True

gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}
gl.ylabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}

# Título del mapa
plt.title('Mapa del Mundo con Diámetros de Red')

# Mostrar el mapa
plt.show()


## CON MALLA DE COLORES ##

# Crear arrays de latitudes, longitudes y valores
latitudes = [d[0] for d in diametros]
longitudes = [d[1] for d in diametros]
values = [d[2] for d in diametros]

# Crear una malla de longitudes y latitudes
lon_unique = np.unique(longitudes)
lat_unique = np.unique(latitudes)
lon, lat = np.meshgrid(lon_unique, lat_unique)

# Crear una matriz para los valores interpolados
interp = np.zeros(lon.shape)
for i in range(len(latitudes)):
    lat_idx = np.where(lat_unique == latitudes[i])[0][0]
    lon_idx = np.where(lon_unique == longitudes[i])[0][0]
    interp[lat_idx, lon_idx] = values[i]

# Configuración de los límites del mapa
latmax = 90
latmin = -90
lonmin = -180
lonmax = 180
img_extent = (lonmin, lonmax, latmin, latmax)

# Crear la figura y el eje con la proyección PlateCarree
fig = plt.figure(figsize=(20, 16))
fig.subplots_adjust(wspace=0.3, hspace=0.1)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=0))

# Añadir características del mapa
ax.coastlines(resolution='50m', color='black', linewidth=1)
ax.set_extent(img_extent)

# Normalizar los valores para mapearlos a un rango de colores
norm = plt.Normalize(min(values), max(values))
cmap = plt.get_cmap('viridis')

# Añadir la malla de colores
cs = ax.pcolormesh(lon, lat, interp, cmap=cmap, norm=norm, transform=ccrs.PlateCarree())

# Añadir colorbar
bounds = np.arange(min(values), max(values) + 0.5, 0.5)
cbar_ax = fig.add_axes([0.18, 0.91, 0.68, 0.03])  # left, bottom, width, height
cbar = plt.colorbar(cs, cax=cbar_ax, orientation='horizontal', boundaries=bounds, ticks=bounds, extend='both', drawedges=True, format=r"%0.1f")
#cbar.set_label(r"Diámetro de las Redes con Spearman", labelpad=-85, rotation=0, fontsize=20)
cbar.dividers.set_linewidths(1)
cbar.outline.set_lw(2)
cbar.solids.set_rasterized(True)
cbar.ax.yaxis.set_ticks_position('right')
for t in cbar.ax.get_xticklabels():
    t.set_fontsize(19)
    t.set_fontweight('bold')

# Configuración de las líneas de la cuadrícula
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_left = True
gl.ylabels_right = False
gl.xlines = True
gl.xlocator = mticker.FixedLocator([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150])
gl.ylocator = mticker.FixedLocator([-80, -60, -40, -20, 0, 20, 40, 60, 80])

gl.xlabel = True
gl.ylabel = True

gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}
gl.ylabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}

# Título del mapa
plt.title('Mapa con los Diámetros de cada Red con Spearman',fontsize=35,pad=13)

# Mostrar el mapa
plt.show()



##############################################
### Número de nodos de cada red en el mapa ###
##############################################

num_nodos_por_red = []

nx = len(longitude)
ny = len(latitude)

for i in range(ny):
    for j in range(nx):
        # Contar el número de nodos para esta red
        num_nodos = sum(sum(A[i, j]))
        num_nodos_por_red.append((latitude[i], longitude[j], num_nodos))
        

## CON CÍRCULOS ##

# Crear arrays de latitudes y longitudes
latitudes = [d[0] for d in num_nodos_por_red]
longitudes = [d[1] for d in num_nodos_por_red]
values = [d[2] for d in num_nodos_por_red]

# Configuración de los límites del mapa
latmax = 90
latmin = -90
lonmin = -180
lonmax = 180
img_extent = (lonmin, lonmax, latmin, latmax)

# Crear la figura y el eje con la proyección PlateCarree
fig = plt.figure(figsize=(20, 16))
fig.subplots_adjust(wspace=0.3, hspace=0.1)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=0))

# Añadir características del mapa
ax.coastlines(resolution='50m', color='black', linewidth=1)
ax.set_extent(img_extent)

# Normalizar los diámetros para mapearlos a un rango de colores
norm = plt.Normalize(min(values), max(values))
cmap = plt.get_cmap('viridis')

# Añadir puntos en el mapa
sc = ax.scatter(longitudes, latitudes, c=values, s=np.array(values)*0.4, cmap=cmap, norm=norm, edgecolor='k', alpha=0.7, transform=ccrs.PlateCarree())

# Añadir colorbar
bounds = np.linspace(min(values), max(values), 10)
cbar_ax = fig.add_axes([0.18, 0.91, 0.68, 0.03])  # left, bottom, width, height
cbar = plt.colorbar(sc, cax=cbar_ax, orientation='horizontal', boundaries=bounds, ticks=bounds, extend='both', drawedges=True, format=r"%d")
cbar.set_label(r"Número de nodos de cada Red con Spearman", labelpad=-85, rotation=0, fontsize=20)
cbar.dividers.set_linewidths(1)
cbar.outline.set_lw(2)
cbar.solids.set_rasterized(True)
cbar.ax.yaxis.set_ticks_position('right')
for t in cbar.ax.get_xticklabels():
    t.set_fontsize(19)
    t.set_fontweight('bold')

# Configuración de las líneas de la cuadrícula
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_left = True
gl.ylabels_right = False
gl.xlines = True
gl.xlocator = mticker.FixedLocator([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150])
gl.ylocator = mticker.FixedLocator([-80, -60, -40, -20, 0, 20, 40, 60, 80])

gl.xlabel = True
gl.ylabel = True

gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}
gl.ylabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}

# Título del mapa
plt.title('Mapa del Mundo con número de nodos de cada red')

# Mostrar el mapa
plt.show()    


## CON MALLA DE COLORES ##

# Crear arrays de latitudes y longitudes
latitudes = [d[0] for d in num_nodos_por_red]
longitudes = [d[1] for d in num_nodos_por_red]
values = [d[2] for d in num_nodos_por_red]

# Crear una malla de longitudes y latitudes
lon_unique = np.unique(longitudes)
lat_unique = np.unique(latitudes)
lon, lat = np.meshgrid(lon_unique, lat_unique)

# Crear una matriz para los valores
values_mesh = np.full(lon.shape, np.nan)
for i in range(len(latitudes)):
    lat_idx = np.where(lat_unique == latitudes[i])[0][0]
    lon_idx = np.where(lon_unique == longitudes[i])[0][0]
    values_mesh[lat_idx, lon_idx] = values[i]

# Configuración de los límites del mapa
latmax = 90
latmin = -90
lonmin = -180
lonmax = 180
img_extent = (lonmin, lonmax, latmin, latmax)

# Crear la figura y el eje con la proyección PlateCarree
fig = plt.figure(figsize=(20, 16))
fig.subplots_adjust(wspace=0.3, hspace=0.1)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=0))

# Añadir características del mapa
ax.coastlines(resolution='50m', color='black', linewidth=1)
ax.set_extent(img_extent)

# Normalizar los valores para mapearlos a un rango de colores
norm = plt.Normalize(min(values), max(values))
cmap = plt.get_cmap('viridis')

# Añadir la malla de colores
cs = ax.pcolormesh(lon, lat, values_mesh, cmap=cmap, norm=norm, transform=ccrs.PlateCarree())

# Añadir colorbar
bounds = np.linspace(min(values), max(values), 15)
cbar_ax = fig.add_axes([0.18, 0.91, 0.68, 0.03])  # left, bottom, width, height
cbar = plt.colorbar(cs, cax=cbar_ax, orientation='horizontal', boundaries=bounds, ticks=bounds, extend='both', drawedges=True, format=r"%d")
#cbar.set_label(r"Número de nodos de cada Red con Spearman", labelpad=-85, rotation=0, fontsize=20)
cbar.dividers.set_linewidths(1)
cbar.outline.set_lw(2)
cbar.solids.set_rasterized(True)
cbar.ax.yaxis.set_ticks_position('right')
for t in cbar.ax.get_xticklabels():
    t.set_fontsize(19)
    t.set_fontweight('bold')

# Configuración de las líneas de la cuadrícula
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_left = True
gl.ylabels_right = False
gl.xlines = True
gl.xlocator = mticker.FixedLocator([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150])
gl.ylocator = mticker.FixedLocator([-80, -60, -40, -20, 0, 20, 40, 60, 80])

gl.xlabel = True
gl.ylabel = True

gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}
gl.ylabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}

# Título del mapa
plt.title('Mapa con el Número de Nodos de cada Red con Pearson',fontsize=35,pad=13)

# Mostrar el mapa
plt.show()


###########################################
### Nodo central de cada red en el mapa ###
###########################################

# Cargar la barra de colores

import sys

sys.path.insert(0, "C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/pythonCodes/pythonCodes/")
from create_colorbar import create_colorbar, make_cmap

pathCustom =  "C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/pythonCodes/pythonCodes/colormaps/"
custombar = create_colorbar(13,False,pathCustom) # customized colorbar

# Construir grafo

import networkx as nk

G = nk.Graph()
for i in range(ny):
    for j in range(nx):
        for k in range(ny):
            for l in range(nx):
                if A[i, j, k, l] == 1:
                    G.add_edge((latitude[i], longitude[j]), (latitude[k], longitude[l]))

# Calcular la centralidad de grado para cada nodo
centralidades_de_grado = nk.degree_centrality(G)

# Pearson
#np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/grado_pearson.npy', centralidades_de_grado, allow_pickle=True)
centralidades_de_grado = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/grado_pearson.npy', allow_pickle=True).item()

# Spearman
#np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/grado_spearman.npy', centralidades_de_grado, allow_pickle=True)
centralidades_de_grado = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/grado_spearman.npy', allow_pickle=True).item()

# Encontrar el nodo con la mayor centralidad de grado
nodo_central = max(centralidades_de_grado, key=centralidades_de_grado.get)


## CON CÍRCULOS ##

# Crear arrays de latitudes y longitudes
latitudes = [d[0][0] for d in centralidades_de_grado.items()]
longitudes = [d[0][1] for d in centralidades_de_grado.items()]
values = [d[1] for d in centralidades_de_grado.items()]

# Configuración de los límites del mapa
latmax = 90
latmin = -90
lonmin = -180
lonmax = 180
img_extent = (lonmin, lonmax, latmin, latmax)

# Crear la figura y el eje con la proyección PlateCarree
fig = plt.figure(figsize=(20, 16))
fig.subplots_adjust(wspace=0.3, hspace=0.1)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=0))

# Añadir características del mapa
ax.coastlines(resolution='50m', color='black', linewidth=1)
ax.set_extent(img_extent)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)

# Normalizar los diámetros para mapearlos a un rango de colores
norm = plt.Normalize(min(values), max(values))
cmap = plt.get_cmap('viridis')

# Añadir puntos en el mapa
sc = ax.scatter(longitudes, latitudes, c=values, s=np.array(values)*1000, cmap=cmap, norm=norm, edgecolor='k', alpha=0.7, transform=ccrs.PlateCarree())

# Marcar el nodo más central con una cruz roja
ax.plot(nodo_central[1], nodo_central[0], 'rx', markersize=15, mew=2, transform=ccrs.PlateCarree(), label='Nodo más central')


# Añadir colorbar
bounds = np.linspace(min(values), max(values), 10)
cbar_ax = fig.add_axes([0.18, 0.91, 0.68, 0.03])  # left, bottom, width, height
cbar = plt.colorbar(sc, cax=cbar_ax, orientation='horizontal', boundaries=bounds, ticks=bounds, extend='both', drawedges=True, format=r"%.2f")
cbar.set_label(r"Centralidad de los nodos con Spearman", labelpad=-85, rotation=0, fontsize=20)
cbar.dividers.set_linewidths(1)
cbar.outline.set_lw(2)
cbar.solids.set_rasterized(True)
cbar.ax.yaxis.set_ticks_position('right')
for t in cbar.ax.get_xticklabels():
    t.set_fontsize(19)
    t.set_fontweight('bold')

# Configuración de las líneas de la cuadrícula
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_left = True
gl.ylabels_right = False
gl.xlines = True
gl.xlocator = mticker.FixedLocator([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150])
gl.ylocator = mticker.FixedLocator([-80, -60, -40, -20, 0, 20, 40, 60, 80])

gl.xlabel = True
gl.ylabel = True

gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}
gl.ylabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}

# Título del mapa
plt.title('Mapa del Mundo con la centralidad de cada nodo')

# Mostrar el mapa
plt.show() 


## CON MALLA DE COLORES ##

# Crear arrays de latitudes y longitudes
latitudes = [d[0][0] for d in centralidades_de_grado.items()]
longitudes = [d[0][1] for d in centralidades_de_grado.items()]
values = [d[1] for d in centralidades_de_grado.items()]

max_value = 0.07051712558764271

# Crear una malla de longitudes y latitudes
lon_unique = np.unique(longitudes)
lat_unique = np.unique(latitudes)
lon, lat = np.meshgrid(lon_unique, lat_unique)

# Crear una matriz para los valores
values_mesh = np.full(lon.shape, np.nan)
for i in range(len(latitudes)):
    lat_idx = np.where(lat_unique == latitudes[i])[0][0]
    lon_idx = np.where(lon_unique == longitudes[i])[0][0]
    values_mesh[lat_idx, lon_idx] = values[i]

# Configuración de los límites del mapa
latmax = 90
latmin = -90
lonmin = -180
lonmax = 180
img_extent = (lonmin, lonmax, latmin, latmax)

# Crear la figura y el eje con la proyección PlateCarree
fig = plt.figure(figsize=(20, 16))
fig.subplots_adjust(wspace=0.3, hspace=0.1)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=0))

# Añadir características del mapa
ax.coastlines(resolution='50m', color='black', linewidth=1)
ax.set_extent(img_extent)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)

# Normalizar los valores para mapearlos a un rango de colores
norm = plt.Normalize(0, max_value)
cmap = plt.get_cmap('viridis')

# Añadir la malla de colores
cs = ax.pcolormesh(lon, lat, values_mesh, cmap=custombar, norm=norm,transform=ccrs.PlateCarree(),rasterized=True)

# Marcar el nodo más central con una cruz roja
nodo_central = max(centralidades_de_grado, key=centralidades_de_grado.get)
ax.plot(nodo_central[1], nodo_central[0], 'rx', markersize=15, mew=2, transform=ccrs.PlateCarree(), label='Nodo más central')

# Añadir colorbar
#bounds = np.linspace(0, max(values), 10)
cbar_ax = fig.add_axes([0.18, 0.91, 0.68, 0.03])  # left, bottom, width, height
#cbar = plt.colorbar(cs, cax=cbar_ax, orientation='horizontal', boundaries=bounds, ticks=bounds, extend='both', drawedges=True, format=r"%.3f")
cbar = plt.colorbar(cs, cax=cbar_ax, orientation='horizontal', extend='max',format=r"%.3f")
#cbar.set_label(r"Centralidad de los nodos con Spearman", labelpad=-85, rotation=0, fontsize=20)
cbar.set_ticks(np.linspace(0, max_value, num=10))
cbar.dividers.set_linewidths(1)
cbar.outline.set_lw(2)
cbar.solids.set_rasterized(True)
cbar.ax.yaxis.set_ticks_position('right')
for t in cbar.ax.get_xticklabels():
    t.set_fontsize(19)
    t.set_fontweight('bold')

# Configuración de las líneas de la cuadrícula
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_left = True
gl.ylabels_right = False
gl.xlines = True
gl.xlocator = mticker.FixedLocator([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150])
gl.ylocator = mticker.FixedLocator([-80, -60, -40, -20, 0, 20, 40, 60, 80])

gl.xlabel = True
gl.ylabel = True

gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}
gl.ylabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}

# Título del mapa
plt.title('Mapa con la Centralidad de Grado de cada Nodo con Pearson',fontsize=35,pad=13)

# Mostrar el mapa
plt.show()


##############################################
### Nodo intermedio de cada red en el mapa ###
##############################################

import networkx as nk

# Calcular la intermediación para cada nodo
intermediacion = nk.betweenness_centrality(G)

# Pearson
#np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/intermediacion_pearson.npy', intermediacion, allow_pickle=True)
intermediacion = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/intermediacion_pearson.npy', allow_pickle=True).item()

# Spearman
#np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/intermediacion_spearman.npy', intermediacion, allow_pickle=True)
intermediacion = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/intermediacion_spearman.npy', allow_pickle=True).item()

# Encontrar el nodo con la mayor centralidad de intermediación
nodo_intermedio = max(intermediacion, key=intermediacion.get)


## CON CÍRCULOS ##

# Crear arrays de latitudes y longitudes
latitudes = [d[0][0] for d in intermediacion.items()]
longitudes = [d[0][1] for d in intermediacion.items()]
values = [d[1] for d in intermediacion.items()]

# Configuración de los límites del mapa
latmax = 90
latmin = -90
lonmin = -180
lonmax = 180
img_extent = (lonmin, lonmax, latmin, latmax)

# Crear la figura y el eje con la proyección PlateCarree
fig = plt.figure(figsize=(20, 16))
fig.subplots_adjust(wspace=0.3, hspace=0.1)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=0))

# Añadir características del mapa
ax.coastlines(resolution='50m', color='black', linewidth=1)
ax.set_extent(img_extent)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)

# Normalizar los diámetros para mapearlos a un rango de colores
norm = plt.Normalize(min(values), max(values))
cmap = plt.get_cmap('viridis')

# Añadir puntos en el mapa
sc = ax.scatter(longitudes, latitudes, c=values, s=np.array(values)*10000, cmap=cmap, norm=norm, edgecolor='k', alpha=0.7, transform=ccrs.PlateCarree())

# Marcar el nodo intermedio con una cruz roja
ax.plot(nodo_intermedio[1], nodo_intermedio[0], 'rx', markersize=15, mew=2, transform=ccrs.PlateCarree(), label='Nodo intermedio')

# Añadir colorbar
bounds = np.linspace(min(values), max(values), 10)
cbar_ax = fig.add_axes([0.18, 0.91, 0.68, 0.03])  # left, bottom, width, height
cbar = plt.colorbar(sc, cax=cbar_ax, orientation='horizontal', boundaries=bounds, ticks=bounds, extend='both', drawedges=True, format=r"%.3f")
cbar.set_label(r"Intermediación de los nodos con Pearson", labelpad=-85, rotation=0, fontsize=20)
cbar.dividers.set_linewidths(1)
cbar.outline.set_lw(2)
cbar.solids.set_rasterized(True)
cbar.ax.yaxis.set_ticks_position('right')
for t in cbar.ax.get_xticklabels():
    t.set_fontsize(19)
    t.set_fontweight('bold')

# Configuración de las líneas de la cuadrícula
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_left = True
gl.ylabels_right = False
gl.xlines = True
gl.xlocator = mticker.FixedLocator([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150])
gl.ylocator = mticker.FixedLocator([-80, -60, -40, -20, 0, 20, 40, 60, 80])

gl.xlabel = True
gl.ylabel = True

gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}
gl.ylabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}

# Título del mapa
plt.title('Mapa del Mundo con la centralidad de intermediación de los nodos')

# Mostrar el mapa
plt.show() 


## CON MALLA DE COLORES ##

# Crear arrays de latitudes y longitudes
latitudes = [d[0][0] for d in intermediacion.items()]
longitudes = [d[0][1] for d in intermediacion.items()]
values = [d[1] for d in intermediacion.items()]

# Crear una malla de longitudes y latitudes
lon_unique = np.unique(longitudes)
lat_unique = np.unique(latitudes)
lon, lat = np.meshgrid(lon_unique, lat_unique)

# Crear una matriz para los valores
values_mesh = np.full(lon.shape, np.nan)
for i in range(len(latitudes)):
    lat_idx = np.where(lat_unique == latitudes[i])[0][0]
    lon_idx = np.where(lon_unique == longitudes[i])[0][0]
    values_mesh[lat_idx, lon_idx] = values[i]

# Configuración de los límites del mapa
latmax = 90
latmin = -90
lonmin = -180
lonmax = 180
img_extent = (lonmin, lonmax, latmin, latmax)

# Crear la figura y el eje con la proyección PlateCarree
fig = plt.figure(figsize=(20, 16))
fig.subplots_adjust(wspace=0.3, hspace=0.1)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=0))

# Añadir características del mapa
ax.coastlines(resolution='50m', color='black', linewidth=1)
ax.set_extent(img_extent)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)

# Normalizar los valores para mapearlos a un rango de colores
norm = plt.Normalize(min(values), max(values))
cmap = plt.get_cmap('viridis')

# Añadir la malla de colores
cs = ax.pcolormesh(lon, lat, values_mesh, cmap=cmap, norm=norm, transform=ccrs.PlateCarree())

# Encontrar el nodo con la mayor centralidad de intermediación
nodo_intermedio = max(intermediacion, key=intermediacion.get)
ax.plot(nodo_intermedio[1], nodo_intermedio[0], 'rx', markersize=15, mew=2, transform=ccrs.PlateCarree(), label='Nodo más central')

# Añadir colorbar
bounds = np.linspace(min(values), max(values), 10)
cbar_ax = fig.add_axes([0.18, 0.91, 0.68, 0.03])  # left, bottom, width, height
cbar = plt.colorbar(cs, cax=cbar_ax, orientation='horizontal', boundaries=bounds, ticks=bounds, extend='both', drawedges=True, format=r"%.3f")
#cbar.set_label(r"Centralidad de los nodos con Spearman", labelpad=-85, rotation=0, fontsize=20)
cbar.dividers.set_linewidths(1)
cbar.outline.set_lw(2)
cbar.solids.set_rasterized(True)
cbar.ax.yaxis.set_ticks_position('right')
for t in cbar.ax.get_xticklabels():
    t.set_fontsize(19)
    t.set_fontweight('bold')

# Configuración de las líneas de la cuadrícula
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_left = True
gl.ylabels_right = False
gl.xlines = True
gl.xlocator = mticker.FixedLocator([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150])
gl.ylocator = mticker.FixedLocator([-80, -60, -40, -20, 0, 20, 40, 60, 80])

gl.xlabel = True
gl.ylabel = True

gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}
gl.ylabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}

# Título del mapa
plt.title('Mapa con la Centralidad de Intermediación de cada Nodo con Pearson',fontsize=31,pad=13)

# Mostrar el mapa
plt.show()


###########################################
### Nodo cercano de cada red en el mapa ###
###########################################

import networkx as nk

# Calcular la centralidad de cercanía para cada nodo
cercania = nk.closeness_centrality(G)

# Pearson
#np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/cercania_pearson.npy', cercania, allow_pickle=True)
cercania = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/cercania_pearson.npy', allow_pickle=True).item()

# Spearman
#np.save('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/cercania_spearman.npy', cercania, allow_pickle=True)
cercania = np.load('C:/Users/gilpe/Desktop/Matemáticas/Cuarto curso/Segundo cuatrimestre/Trabajo de Fin de Grado/Programas/Clima/cercania_spearman.npy', allow_pickle=True).item()

# Encontrar el nodo con la mayor centralidad de cercania
nodo_cercano = max(cercania, key=cercania.get)


## CON CÍRCULOS ##

# Crear arrays de latitudes y longitudes
latitudes = [d[0][0] for d in cercania.items()]
longitudes = [d[0][1] for d in cercania.items()]
values = [d[1] for d in cercania.items()]

# Configuración de los límites del mapa
latmax = 90
latmin = -90
lonmin = -180
lonmax = 180
img_extent = (lonmin, lonmax, latmin, latmax)

# Crear la figura y el eje con la proyección PlateCarree
fig = plt.figure(figsize=(20, 16))
fig.subplots_adjust(wspace=0.3, hspace=0.1)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=0))

# Añadir características del mapa
ax.coastlines(resolution='50m', color='black', linewidth=1)
ax.set_extent(img_extent)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)

# Normalizar los diámetros para mapearlos a un rango de colores
norm = plt.Normalize(min(values), max(values))
cmap = plt.get_cmap('viridis')

# Añadir puntos en el mapa
sc = ax.scatter(longitudes, latitudes, c=values, s=np.array(values)*300, cmap=cmap, norm=norm, edgecolor='k', alpha=0.7, transform=ccrs.PlateCarree())

# Marcar el nodo con mayor dentralidad de cercanía con una cruz roja
ax.plot(nodo_cercano[1], nodo_cercano[0], 'rx', markersize=15, mew=2, transform=ccrs.PlateCarree(), label='Nodo intermedio')

# Añadir colorbar
bounds = np.linspace(min(values), max(values), 10)
cbar_ax = fig.add_axes([0.18, 0.91, 0.68, 0.03])  # left, bottom, width, height
cbar = plt.colorbar(sc, cax=cbar_ax, orientation='horizontal', boundaries=bounds, ticks=bounds, extend='both', drawedges=True, format=r"%.2f")
cbar.set_label(r"Cercanía de los nodos con Spearman", labelpad=-85, rotation=0, fontsize=20)
cbar.dividers.set_linewidths(1)
cbar.outline.set_lw(2)
cbar.solids.set_rasterized(True)
cbar.ax.yaxis.set_ticks_position('right')
for t in cbar.ax.get_xticklabels():
    t.set_fontsize(19)
    t.set_fontweight('bold')

# Configuración de las líneas de la cuadrícula
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_left = True
gl.ylabels_right = False
gl.xlines = True
gl.xlocator = mticker.FixedLocator([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150])
gl.ylocator = mticker.FixedLocator([-80, -60, -40, -20, 0, 20, 40, 60, 80])

gl.xlabel = True
gl.ylabel = True

gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}
gl.ylabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}

# Título del mapa
plt.title('Mapa del Mundo con la centralidad de cercanía de los nodos')

# Mostrar el mapa
plt.show() 


## CON MALLA DE COLORES ##

# Crear arrays de latitudes y longitudes
latitudes = [d[0][0] for d in cercania.items()]
longitudes = [d[0][1] for d in cercania.items()]
values = [d[1] for d in cercania.items()]

max_value = 0.22532363016054258

# Crear una malla de longitudes y latitudes
lon_unique = np.unique(longitudes)
lat_unique = np.unique(latitudes)
lon, lat = np.meshgrid(lon_unique, lat_unique)

# Crear una matriz para los valores
values_mesh = np.full(lon.shape, np.nan)
for i in range(len(latitudes)):
    lat_idx = np.where(lat_unique == latitudes[i])[0][0]
    lon_idx = np.where(lon_unique == longitudes[i])[0][0]
    values_mesh[lat_idx, lon_idx] = values[i]

# Configuración de los límites del mapa
latmax = 90
latmin = -90
lonmin = -180
lonmax = 180
img_extent = (lonmin, lonmax, latmin, latmax)

# Crear la figura y el eje con la proyección PlateCarree
fig = plt.figure(figsize=(20, 16))
fig.subplots_adjust(wspace=0.3, hspace=0.1)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=0))

# Añadir características del mapa
ax.coastlines(resolution='50m', color='black', linewidth=1)
ax.set_extent(img_extent)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)

# Normalizar los valores para mapearlos a un rango de colores
norm = plt.Normalize(0, max_value)
cmap = plt.get_cmap('viridis')

# Añadir la malla de colores
cs = ax.pcolormesh(lon, lat, values_mesh, cmap=custombar, norm=norm, transform=ccrs.PlateCarree(),rasterized=True)

# Marcar el nodo con la mayor centralidad de cercania
nodo_cercano = max(cercania, key=cercania.get)
ax.plot(nodo_cercano[1], nodo_cercano[0], 'rx', markersize=15, mew=2, transform=ccrs.PlateCarree(), label='Nodo más central')

# Añadir colorbar
#bounds = np.linspace(min(values), max(values), 10)
cbar_ax = fig.add_axes([0.18, 0.91, 0.68, 0.03])  # left, bottom, width, height
#cbar = plt.colorbar(cs, cax=cbar_ax, orientation='horizontal', boundaries=bounds, ticks=bounds, extend='both', drawedges=True, format=r"%.3f")
cbar = plt.colorbar(cs, cax=cbar_ax, orientation='horizontal', extend='max',format=r"%.3f")
#cbar.set_label(r"Centralidad de los nodos con Spearman", labelpad=-85, rotation=0, fontsize=20)
cbar.set_ticks(np.linspace(0, max_value, num=10))
cbar.dividers.set_linewidths(1)
cbar.outline.set_lw(2)
cbar.solids.set_rasterized(True)
cbar.ax.yaxis.set_ticks_position('right')
for t in cbar.ax.get_xticklabels():
    t.set_fontsize(19)
    t.set_fontweight('bold')

# Configuración de las líneas de la cuadrícula
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_left = True
gl.ylabels_right = False
gl.xlines = True
gl.xlocator = mticker.FixedLocator([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150])
gl.ylocator = mticker.FixedLocator([-80, -60, -40, -20, 0, 20, 40, 60, 80])

gl.xlabel = True
gl.ylabel = True

gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}
gl.ylabel_style = {'size': 20, 'color': 'k', 'style': 'italic'}

# Título del mapa
plt.title('Mapa con la Centralidad de Cercanía de cada Nodo con Pearson',fontsize=34,pad=13)

# Mostrar el mapa
plt.show()
