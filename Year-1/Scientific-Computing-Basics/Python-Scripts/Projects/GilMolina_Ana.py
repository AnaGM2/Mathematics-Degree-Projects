# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 23:08:09 2020

@author: gilpe
"""


import numpy as np
import numpy.polynomial.polynomial as npp
import matplotlib.pyplot as plt



###############################
#PRIMERA FUNCIÓN
###############################

def perfecta():
    """
    Función que indica si un número es una potencia perfecta del grado indicado.
    """
    n = input('Introduzca un número natural ')
    n = float(n)
    # Debemos convertir los números a tipo float, pues con objetos de tipo int y str no se puede operar.
    while n<=0 or n%1!=0:
        # Este bucle se repetirá mientras el número introducido no sea natural.
        n = input('El número introducido no es natural. Por favor, introduzca un número natural ')
        n = float(n)
    g = input('Introduzca el grado del cual se determinará si el número anterior es potencia perfecta ')
    g = float(g)
    while g<=1 or g%1!=0:
        # Este bucle se repetirá mientras el grado introducido no sea un natural mayor que 1.
        g = input('El grado debe ser un número natural mayor que 1. Por favor, introduzca el grado ')
        g = float(g)
    for i in np.arange(2,n):
        # Este bucle recorrerá los naturales de 2 a n comprobando si para alguno de ellos se cumple la
        # condición establecida en el if siguiente.
        if i**g==n:
            # Establecemos la condición para que n sea potencia perfecta de grado g, la cual es que exista un
            # m natural tal que 1<m<n que cumpla que m^g = n.
            m = int(i)
            n = int(n)
            g = int(g)
            # Volvemos a convertir los números a tipo int para que al usar el print no salgan con decimales.
            print('El número',n,'es una potencia perfecta de grado',g,'pues {} = {}^{}'.format(n,m,g))
            return
            # El return servirá para romper la función una vez encontrado m.
    # En caso de no encontrar ningún m que cumpla la condición anterior la función informará que n no es 
    # potencia perfecta de grado g.
    print('El número',n,'no es una potencia perfecta de grado',g)


perfecta()
# Probar con 64 y 2, 27 y 3, pues 64 es potencia perfecta de grado 2 y 27 es potencia perfecta de grado 3.
# Probar con 9 y 5, 10 y 3, pues en estos casos no serán potencia perfecta.



###############################
#SEGUNDA FUNCIÓN
###############################

def distancia(Pr,vr,Ps,vs):
    """
    Función que calcula la distancia entre dos rectas dados sus vectores directores y un punto por el que pasan.
    Introduzca en primera posición una lista con las coordenadas del punto por el que pasa la primera recta.
    Introduzca en segunda posición una lista con los elementos del vector director de la primera recta.
    Introduzca en tercera posición una lista con las coordenadas del punto por el que pasa la segunda recta.
    Introduzca en cuarta posición una lista con los elementos del vector director de la segunda recta.

    """
    Pr = np.array(Pr)
    vr = np.array(vr)
    Ps = np.array(Ps)  
    vs = np.array(vs)
    # Definimos una matriz formada por vr, vs y el vector que va de Pr a Ps que usaremos más adelante.
    A = np.array([vr,vs,Ps-Pr])
    # Debemos separar los casos en los que las rectas sean paralelas, coincidentes, secantes o se crucen.
    # Para ver si son paralelas o coincidentes, deberemos dividir los elementos del vector director de la
    # primera recta entre los de la segunda y ver si todas las divisiones dan el mismo resultado.
    if vr[0]/vs[0]==vr[1]/vs[1] and vr[1]/vs[1]==vr[2]/vs[2]:
        # En este caso las rectas son paralelas o coincidentes.
        # En primer lugar debemos calcular el vector que va de Pr a Ps.
        w = Ps-Pr
        # A continuación calculamos el producto vectorial entre w y vr.
        pv = np.array([w[1]*vr[2]-vr[1]*w[2],w[2]*vr[0]-vr[2]*w[0],w[0]*vr[1]-vr[0]*w[1]])
        # Ahora calculamos el módulo del producto vectorial calculado.
        mpv = np.sqrt(pv[0]**2+pv[1]**2+pv[2]**2)
        # Por último calculamos el módulo del vector director de r.
        mvr = np.sqrt(vr[0]**2+vr[1]**2+vr[2]**2)
        # La distancia será el resultado de dividir el módulo del producto vectorial entre el módulo de vr.
        d = mpv/mvr
        if d==0:
            print('Las rectas son coincidentes, por lo que su distancia es 0')
        else:
            print('Las rectas son paralelas y su distancia es',d)
    # Para ver si las rectas son secantes tendremos que calcular el determinante de la matriz A definida
    # anteriormente y comprobar que es igual a 0.
    elif np.linalg.det(A)==0:
        # En este caso las rectas son secantes.
        print('Las rectas son secantes, por lo que su distancia es 0')
    # Si el determinate de A es distinto de 0 entonces las rectas se cruzan.
    else:
        # Como no se cumple ninguna de las condiciones de los if anteriores, las rectas se cruzan.
        # Calculemos en primer lugar el determinante de A.
        detA = np.linalg.det(A)
        # A continuación calculamos el producto vectorial entre vr y vs.
        pv = np.array([vr[1]*vs[2]-vs[1]*vr[2],vr[2]*vs[0]-vs[2]*vr[0],vr[0]*vs[1]-vs[0]*vr[1]])
        # Calculamos el módulo del producto vectorial anterior.
        mpv = np.sqrt(pv[0]**2+pv[1]**2+pv[2]**2)
        # La distancia será el resultado de dividir el valor absoluto del determinante de A entre el módulo
        # del producto vectorial.
        d = abs(detA)/mpv
        print('Las rectas se cruzan y su distancia es',d)


# Probemos con rectas coincidentes.
distancia([1,1,1],[1,1,1],[1,1,1],[2,2,2])
# Probemos con rectas paralelas.
distancia([0,-1,0],[1,1,1],[3,-5,1],[1,1,1])
# Probemos con rectas secantes.
distancia([2,3,4],[1,1,1],[3,4,5],[2,3,9])
#Probemos con rectas que se cruzan.
distancia([1,-1,0],[2,3,-1],[0,-2,1],[4,-2,3])



###############################
#TERCERA FUNCIÓN
###############################

def análisis(y):
    """
    Introducir un array con los coeficientes de un polinomio en potencias decrecientes.
    Se obtendrá:
    -Los puntos de corte con los ejes.
    -Las asístontas.
    -Los máximos y mínimos relativos.
    -Los puntos de inflexión.
    -La representación gráfica.

    """
    # Puntos de corte con el eje de abscisas. Debemos igualar el polinomio a 0, es decir, calcular sus raíces.
    corteX = list(np.roots(y))
    if corteX==[]:
        print('No hay puntos de corte con el eje de abscisas.')
    else:
        print('Los puntos de corte con el eje de abscisas son',corteX,'.')
    # Puntos de corte con el eje de ordenadas. Debemos calcular los valores que adquiere y cuando x=0.
    corteY = np.polyval(y,0)
    print('El punto de corte con el eje de ordenadas es',corteY,'.')
    # Asíntota vertical no habrá nunca en una función polinómica, pues su dominio siempre serán los reales.
    # Calculamos el grado del polinomio. Para ello creamos una lista con los valores del array.
    lista = list(y)
    # Invertimos su orden.
    lista.reverse()
    #Creamos un polinomio en potencias crecientes con la lista.
    poli = npp.Polynomial(lista)
    # Y calculamos su grado.
    grado = poli.degree()
    if grado==0:
        # Asíntota horizontal solamente habrá si el polinomio es de grado 0, y será el término independiente.
        AH = y[0]
        print('Hay una asíntota horizontal en y={}'.format(AH),'.')
    elif grado==1:
        # Si no existe asíntota horizontal, podrá existir asíntota oblícua. Esto solamente ocurrirá si el
        # polinomio es de grado 1, y será el propio polinomio.
        if y[1]>0:
            print('Hay una asíntota oblicua en y={}x+{}'.format(y[0],y[1]),'.')
        elif y[1]==0:
            print('Hay una asíntota oblicua en y={}x'.format(y[0]),'.')
        else:
            print('Hay una asíntota oblicua en y={}x{}'.format(y[0],y[1]),'.')
    else:
        print('No hay asíntontas.')
    # Para obtener los máximos y mínimos relativos debemos calcular la primera derivada del polinomio.
    deriv1 = poli.deriv(1)
    # A continuación debemos igualarla a 0, es decir, calcular sus raíces.
    d1raíces = deriv1.roots()
    # Ahora calculamos la segunda derivada.
    deriv2 = poli.deriv(2)
    # Por último, le damos los valores de las raíces de la primera derivada a la x de la segunda derivada y
    # vemos si el signo de la solución es positivo o negativo.
    if list(d1raíces)!=[]:
        for i in d1raíces:
            n = deriv2(i)
            if n<0:
                print('(',i,',',np.polyval(y,i),') es un máximo.')
            elif n>0:
                print('(',i,',',np.polyval(y,i),') es un mínimo.')
    else:
        print('No hay máximos ni mínimos.')
    # Para obtener los puntos de inflexión debemos calcular las raíces de la segunda derivada del polinomio.
    d2raíces = deriv2.roots()
    for i in d2raíces:
        print('(',i,',',np.polyval(y,i),') es un punto de inflexión.')
    # Por último hacemos la representación gráfica. Creamos un array con los valores de x.
    x = np.linspace(-20,20,1000)
    # Cambiamos el tamaño del gráfico.
    plt.figure(figsize=(10,5))
    # Establecemos la representación de la función.
    plt.ylim(-200,200)
    plt.plot(x,np.polyval(y,x),'k')
    #Añadimos una malla.
    plt.grid()
    # Añadimos los puntos de corte con el eje de abscisas (se representarán en color rojo).
    for i in corteX:
        plt.plot(i,0,'Dr',ms=9)
    # Añadimos los puntos de corte con el eje de ordenadas (se representarán en color amarillo).
    plt.plot(i,0,'*y',ms=8)
    # Añadimos los puntos de inflexión (se representarán en color azul).
    for i in d2raíces:
        plt.plot(i,np.polyval(y,i),'*c',ms=5)
    # Añadimos nombres a la gráfica y a los ejes.
    plt.title('Polinomio')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
        
    
# Veamos algunos ejemplos.
análisis(np.array([1,-4,-2,12,0]))
análisis(np.array([1,0,-8,0,7]))
análisis(np.array([7,8]))
análisis(np.array([3,4,-36,0,0]))