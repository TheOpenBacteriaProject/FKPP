# -*- coding: utf-8 -*-
"""
Presentamos un codigo mediante el cual podemos generar la simulacion en 3d 
de la ecuacion FKPP. El proceso seguido es el que se puede encontrar en la 
documentacion del proyecto.

En este primer acercamiento hemos preferido cierta claridad en el codigo a 
eficiencia. Cuando la web esté operativa, las simulaciones se manejarán de un modo 
optimizado.

@author: TheOpenBacteriaProject
"""

#Importamos distintas librerías utiles para el desarrollo del codigo en todos los códigos
#para poder usarlos en el mismo ide simultáneamente y poder desplazar trozos de unos a 
#otros sin preocuparnos por la compatibillidad. El fin de estos códigos es científico pero
#también educativo, por tanto, creemos que este puede ser un bun enfoque.

from time import time
import numpy
import math
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D 
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title
import matplotlib.colors as mcolors
print("Dependencies loaded...")

#Definimos la función para crear nuestro mapa de colores personalizado 
#con los colores del proyecto

def make_colormap(seq):

    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)


c = mcolors.ColorConverter().to_rgb
rvb = make_colormap(
    [c('c'), c('orange'), c('darkorange')])


#Para controlar la eficiencia disponemos un calculador de tiempo
tiempo_inicial = time()



###Declaramos las variables iniciales. Este script tiene como finalidad mostrar
### y generar la simulacion.
 
nx = 50
ny = 50
nt = 17
vel=15
nu = .02
dx = 10.0 / (nx - 1) #discretizaciones
dy = 10.0 / (ny - 1)
sigma = .01
dt = sigma * dx * dy / nu

x = numpy.linspace(-5, 5, nx)
y = numpy.linspace(-5, 5, ny)

u = numpy.ones((ny, nx))  
un = numpy.ones((ny, nx))

###Este primer bloque sirve para generar como puede verse la condicion inicial:
### unos bloques que representarán puntos en los que hay bacterias.
### Esta presentación es opcional y podría omitirse puesto que en nuestra funcion 
### de evolución ya tenemos esta declaración

u[int(3.5/dy):int(4.0/dy),int(3.5/dx):int(4.0/dx)] = 2
u[int(10./dy):int(10.5/dy),int(7.0/dx):int(7.5/dx)] = 2

fig = pyplot.figure()
ax = fig.gca(projection='3d')
X, Y = numpy.meshgrid(x, y)
surf = ax.plot_surface(X, Y, u, rstride=1, cstride=1, cmap=rvb,
        linewidth=0, antialiased=False)

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(1, 10.5)

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
title('Condicion inicial');



###Definimos la función que evoluciona nuestro proceso biologico:
###la entrada es el tamaño temporal (el modificable) y el mallado, que se mantiene fijo por motivos 
### de estabilidad.

def FKPP(nt,nx):
    
    ### Este primer bloque volvemos a declarar las variables para que el anterior
    ### sea completamente omitible.
    
    u[int(3.5/dy):int(4.0/dy+1),int(3.5/dx):int(4.0/dx+1)] = 2
    u[int(8./dy):int(8.5/dy+1),int(6.0/dx):int(6.5/dx+1)] = 2
    for i in range(0,nx):
        for j in range(0,nx):
            if u[i][j]!=2:
                u[i][j]=0 ##Nos aseguramos de que no haya bacterias en ningun otro punto
    
    #Ciclo para la evolucion descrita en la documentación.
    for n in range(nt + 1): 
        un = u.copy()
        u[1:-1, 1:-1] = (un[1:-1,1:-1] + vel*nu * dt / dx**2 *(un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +vel*nu * dt / dy**2 * (un[2:,1: -1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1])+dt*un[1:-1,1:-1]-dt*un[1:-1,1:-1]*un[1:-1,1:-1]/2)
        u[0, :] = 0
        u[-1, :] = 0
        u[:, 0] = 0
        u[:, -1] = 0
        
        #Este ciclo nos permite acotar el crecimiento de la bacteria a un circulo
        #Ante la posibilidad de saltos por la discretizacion numérica exite aunque 
        #seria poco represetnativa
        ##Abrimos la puerta para una futura mejora del codigo, pasando a coordenadas
        ##polares, pero el limitado tiempo nos lo ha impedido.
        
        for angle in range(0, 360, 5):
            x = 24 * math.sin(math.radians(angle)) + int(round((nx/2.0)-1))
            y = 24 * math.cos(math.radians(angle)) + int(round((nx/2.0)-1))
            for i in range(0,nx):
                for j in range(0,nx):
                    if i==int(round(x)) and j==int(round(y)):
                        u[i][j]=0
    #Este último ciclo (que debe estar fuera del principal para que la aproximacion 
    #no afecte al desarrollo normal de la evolucion temporal), nos sirve para 
    #aproximar la sensibilidad de los resultados, eliminando los elementos que estén
    #por debajo de un rango para paliar la difusión infinita generada por el uso de la 
    #ecuacion de difusión clásica.
    #Incluir modelos de flujo limitado es otra de los futuros avances planeados      
    for i in range(0,nx):
        for j in range(0,nx):
            if u[i][j]<=0.4:
                u[i][j]=0
                
    return u

#Creacion de la grafica:

u=FKPP(200,nx)
fig = pyplot.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, u[:], rstride=1, cstride=1, cmap=rvb,
    linewidth=0, antialiased=True)
ax.set_zlim(0, 10.5)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
title('concetracion bacterias')
pyplot.show()

#Recogemos los datos de tiempo generados
tiempo_final = time() 
tiempo_ejecucion = tiempo_final - tiempo_inicial
print(tiempo_ejecucion)