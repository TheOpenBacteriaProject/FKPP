#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Repertorio de funciones útiles para datos auxiliares

De nuevo este codigo se ejecuta usando el IDE Spyder, por lo que antes debe haberse ejecutado
el codigo principal de la simulación con el fin de obtener los datos.

@author: The Open Bacteria Project
"""




##Esta funcion permite conocer el porcentaje de la placa (aproximacion circular)
## y experimento (malla cuadriculada) que está cubierto de
## bacterias, como medida de la posible cantidad de bacterias.
## Entra la matriz resultande de la simulacion y salen 2 porcentajes.
def surface_cover(a):
    contador=0
    for i in range(0,50):
        for j in range(0,50):
            if a[i][j]!=0:
                contador += 1
    porcentaje1=contador/18.0864
    porcentaje2=contador/25
    return (porcentaje1,porcentaje2)

#Llamada de las funciones
surf_co=surface_cover(u)
print('Cantidad de placa de petri con bacterias: {0}%\nCantidad de superfice experimental con bacterias: {1}%'.format(surf_co[0],surf_co[1]))
                
                