#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CODIGO PARA EJECUCION DENTRO DEL BACKEND DE LA WEB
Presentamos  la funcion con el algoritmo mediante el cual podemos generar la simulacion en 3d
de la ecuacion FKPP. El proceso seguido es el que se puede encontrar en la
documentacion del proyecto.
Este codigo nos sirve para interactuar con la web y la base de datos de forma óptima, dejando
para la inspección los otros códigos. Todos los que tenga esto como fin vendrán marcados
con el identificativo: WEB
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
import sys

#Describimos el algoritmo prinicipal.
#La funcion recibe tres parametros
#1º u  => Matriz de datos
#2º nt => Tiempo del experimento
#3º v  => Velocidad del experimento
def FKPP(u,nt,v):
    nx = 50
    ny = 50
    vel= v
    nu = .02
    dx = 10.0 / (nx - 1) #discretizaciones
    dy = 10.0 / (ny - 1)
    sigma = .01
    dt = sigma * dx * dy / nu

    x = numpy.linspace(-5, 5, nx)
    y = numpy.linspace(-5, 5, ny)

    if u == 0:
        u = numpy.ones((50,50))

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
