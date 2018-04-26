import os

import cv2
import numpy as np
import matplotlib.pyplot as plt



#Directorio de las imágenes
path = './ejemplo1.jpg' #customize path properly
#Cargamos la imagen en blanco y negro y un reescalado
img= cv2.imread(path, 0)
img = cv2.resize(img, (0,0), fx=0.1, fy=0.1) 
img1 = img.copy() #Copia de la imagen
print(img.shape)
#Emborronamos la imagen para quitarle ruido
img = cv2.medianBlur(img,5)

img1 = cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR)
#Usamos la transformada de Hough para detectar la placa de petri
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,200,
                            param1=150,param2=100,minRadius=70,maxRadius=0)

circles = np.uint16(np.around(circles))


#Dibujamos la circunferencia de la placa
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img1,(i[0],i[1]),i[2],(255,0,0),2)
    x, y = i[0], i[1]
    r = i[2]- 30 #reducimos el radio para quedarnos con el interior de la placa


#Recortamos la imagen quedándonos con la placa de Petri
height,width = img.shape
mask = np.zeros((height,width), np.uint8)
cv2.circle(mask,(x,y),r,(255,255,255),thickness=-1)
masked_data = cv2.bitwise_and(img1, img1, mask=mask)
_,thresh = cv2.threshold(mask,1,255,cv2.THRESH_BINARY)
contours = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
x,y,w,h = cv2.boundingRect(contours[0])
crop = masked_data[y:y+h,x:x+w]


#Umbralizamos la imagen para obtener las bacterias
umbral = 165
crop_umbral=crop.copy()

crop_umbral[crop>umbral]=255
crop_umbral[crop<=umbral]=0
print(crop_umbral.shape)

#Calculamos el área que ocupa la poblacion sabiendo que la placa tiene de diámetro 9cm
area_per_pixel = (9/crop.shape[0])**2
norm = crop_umbral/255
area = norm.sum() * area_per_pixel


# display results
    
plt.imshow(img1)
plt.show()


plt.figure()
ax = plt.subplot("221")
ax.set_title("Placa de Petri")
ax.imshow(crop)

ax = plt.subplot("222")
ax.set_title("El área ocupada es: %f $cm^{2}$" %(area))
ax.imshow(crop_umbral)
plt.tight_layout()
plt.show()

condicion_inicial = cv2.cvtColor(crop_umbral, cv2.COLOR_RGB2GRAY)

condicion_inicial = cv2.resize(condicion_inicial, (50,50)) 
condicion_inicial = condicion_inicial * 1.0
condicion_inicial [condicion_inicial != 0] = 2
print(condicion_inicial, condicion_inicial.shape, condicion_inicial.dtype, print(condicion_inicial[20:30,20:30]))


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
vel=7
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


print(np.sum(condicion_inicial))
fig = pyplot.figure()
ax = fig.gca(projection='3d')
X, Y = numpy.meshgrid(x, y)
surf = ax.plot_surface(X, Y, condicion_inicial, rstride=1, cstride=1, cmap=rvb,
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

def FKPP(nt,nx, condicion_inicial):
    
    ### Este primer bloque volvemos a declarar las variables para que el anterior
    ### sea completamente omitible.
    
    u = condicion_inicial
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
u=FKPP(1,nx,condicion_inicial)
fig = pyplot.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, u[:], rstride=1, cstride=1, cmap=rvb,
    linewidth=0, antialiased=True)
ax.set_zlim(0, 10.5)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
title('concentracion bacterias')
pyplot.show()
im = imshow(u,cmap=rvb) # dibujamos la función
# Añadimos las lineas de contorno y las etiquetas a cada una.
cset = contour(u,arange(0.7,2,0.3),linewidths=1,cmap=cm.binary)
clabel(cset,inline=True,fmt='%1.1f',fontsize=10)
colorbar(im) # Añadimos la barra de color a la derecha
# Título
title('concentracion bacterias')
#A parte, podemos salvar la figura Des-comentando la siguiente linea
#savefig('bacteriaslineas')
pyplot.show()


u=FKPP(200,nx, condicion_inicial)
fig = pyplot.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, u[:], rstride=1, cstride=1, cmap=rvb,
    linewidth=0, antialiased=True)
ax.set_zlim(0, 10.5)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
title('concentracion bacterias')
pyplot.show()

#Recogemos los datos de tiempo generados
tiempo_final = time() 
tiempo_ejecucion = tiempo_final - tiempo_inicial
print(tiempo_ejecucion)

from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show,savefig
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
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

#creación del mapa de colores personalizado:
c = mcolors.ColorConverter().to_rgb
rvb = make_colormap(
    [c('c'), c('orange'), c('darkorange')])

###Aquí comienza el bloque de evaluación de la funcion mapeo
### Como decimos, la información de u puede ser cualquier, pero el ide Spyder la 
### extrae de la que esta en memoria al ejecutar el algoritmo de evolucion FKPP

im = imshow(u,cmap=rvb) # dibujamos la función
# Añadimos las lineas de contorno y las etiquetas a cada una.
cset = contour(u,arange(0.7,2,0.3),linewidths=1,cmap=cm.binary)
clabel(cset,inline=True,fmt='%1.1f',fontsize=10)
colorbar(im) # Añadimos la barra de color a la derecha
# Título
title('concentracion bacterias')
#A parte, podemos salvar la figura Des-comentando la siguiente linea
#savefig('bacteriaslineas')
show()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esta funcion permite dibujar el corte trasnversal de la placa 
Tambien permite buscar el que puede ser más represenatativo.
Este corte es puramente teórico y puede ser representativo, pero creemos 
prudente que solo se use para ver la posible validez del modelo.
En futuras adpataciones podemos reformarlo para que se ajuste aún mas a la realidad.
De nuevo este codigo se ejecuta usando el IDE Spyder, por lo que antes debe haberse ejecutado
el codigo principal de la simulación con el fin de obtener los datos.
@author: The Open Bacteria Project
"""
#Funciones auxiliares como esta son mantenidas con el minimo de las librerías

import numpy as np
import matplotlib.pyplot as plt
print("Dependencies loaded...")

#Con esta función podemos encontrar el corte con más cantidad de bacterias
#asumimos que puede ser el más representativo, pero los parámetros pueden cambiarse
#Entra una matriz de datos y devuelve el índice de la fila 

def encontrar_corte(a):
    suma_del_corte=0
    indice=0
    for i in range(0,nx):
        if np.sum(a[i])>suma_del_corte:
           suma_del_corte=np.sum(a[i])
           indice=i
    return indice
            
    
#Con esta funcion recibimos una lista del corte que sumamos. Entra matriz de datos
#devuelve dibujo. 
    

def dibujar_corte(a):

    fig = plt.figure()
    ax = plt.axes()
    x = np.linspace(0, 1, 50)
    ax.plot(x, u[20])
    show()

#ejecutamos para nuestra simulacion:
indice=encontrar_corte(u)
print ('Indice del corte extraido: {0}'.format(indice))
dibujar_corte(u[indice])