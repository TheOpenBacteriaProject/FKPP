# -*- coding: utf-8 -*-
"""
Presentamos un codigo mediante el cual podemos generar la vision en 2d con lineas de 
contorno de la ecuacion FKPP. El proceso seguido es el que se puede encontrar en la 
documentacion del proyecto.

En este primer acercamiento hemos preferido cierta claridad en el codigo a 
eficiencia. Cuando la web esté operativa, las simulaciones se manejarán de un modo 
optimizado.

En esta parte y como comentamos en otras, está el fragmento para generar la vision en 2d 
con lineas de contorno de cualquier simulación.
Usando el IDE libre Spyder, podemos ejecutar el proceso de creacion de forma completamente independiente 
y plotear el resultado corriendo este sccript despues.

Codigo adaptado de la documentación de pylab y matplotlib.

@author: TheOpenBacteriaProject
"""

#Importamos distintas librerías utiles para el desarrollo del codigo en todos los códigos
#para poder usarlos en el mismo ide simultáneamente y poder desplazar trozos de unos a 
#otros sin preocuparnos por la compatibillidad. El fin de estos códigos es científico pero
#también educativo, por tanto, creemos que este puede ser un bun enfoque.

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
title('concetracion bacterias')
#A parte, podemos salvar la figura Des-comentando la siguiente linea
#savefig('bacteriaslineas')
show()