#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Este codigo es el fragmento utilizado para probar distintos tipos de parametros
a la hora de colorear nuestras simulaciones.
El codigo está basado en esta respuesta de stackoverflow: 
    https://stackoverflow.com/questions/16834861/create-own-colormap-using-matplotlib-and-plot-color-scale
    donde puede consultarse mas opciones

@author: The Open Bacteria Project
"""
#Importamos distintas librerías utiles para el desarrollo del codigo en todos los códigos
#para poder usarlos en el mismo ide simultáneamente y poder desplazar trozos de unos a 
#otros sin preocuparnos por la compatibillidad. El fin de estos códigos es científico pero
#también educativo, por tanto, creemos que este puede ser un bun enfoque.

import numpy
from matplotlib import pyplot
import matplotlib.colors as mcolors


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
opb = make_colormap(
    [c('c'), c('orange'), c('darkorange')])

#Aqui creamos un gradiente de colores para que pueda observarse el resultado
gradient = numpy.linspace(0, 1, 256)
gradient = numpy.vstack((gradient, gradient))
fig, axes = pyplot.subplots(1)
fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
axes.set_title('Open Bacteria project colormap', fontsize=14)
axes.imshow(gradient, aspect='auto', cmap=pyplot.get_cmap(opb))
pyplot.show
