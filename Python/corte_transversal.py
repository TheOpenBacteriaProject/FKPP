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

#ejecutamos para nuestra simulacion:
indice=encontrar_corte(u)
print ('Indice del corte extraido: {0}'.format(indice))
dibujar_corte(u[indice])



