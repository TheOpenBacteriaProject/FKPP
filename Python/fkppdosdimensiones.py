# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 00:20:03 2017

@author: booort
"""

import numpy
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D ##library for 3d projection plots
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title
###variable declarations
nx = 50
ny = 50
nt = 17
nu = .05
dx = 10.0 / (nx - 1)
dy = 10.0 / (ny - 1)
sigma = .01
dt = sigma * dx * dy / nu

x = numpy.linspace(-5, 5, nx)
y = numpy.linspace(-5, 5, ny)

u = numpy.ones((ny, nx))  # create a 1xn vector of 1's
un = numpy.ones((ny, nx))

###Assign initial conditions
# set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
u[int(.5/dy):int(1.0/dy),int(.5/dx):int(1.0/dx)] = 2  
u[int(3.5/dy):int(4.0/dy),int(3.5/dx):int(4.0/dx)] = 2
fig = pyplot.figure()
ax = fig.gca(projection='3d')
X, Y = numpy.meshgrid(x, y)
surf = ax.plot_surface(X, Y, u, rstride=1, cstride=1, cmap=cm.viridis,
        linewidth=0, antialiased=False)

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(1, 10.5)

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
title('Condicion inicial');


def diffuse(nt):
    u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2 
    u[int(3.5/dy):int(4.0/dy+1),int(3.5/dx):int(4.0/dx+1)] = 2
    for i in range(0,50):
        for j in range(0,50):
            if u[i][j]!=2:
                u[i][j]=0
    for n in range(nt + 1): 
        un = u.copy()
        u[1:-1, 1:-1] = (un[1:-1,1:-1] + nu * dt / dx**2 *(un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +nu * dt / dy**2 * (un[2:,1: -1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1])+dt*un[1:-1,1:-1]-dt*un[1:-1,1:-1]*un[1:-1,1:-1]/2)
        u[0, :] = 0
        u[-1, :] = 0
        u[:, 0] = 0
        u[:, -1] = 0

    
    fig = pyplot.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, u[:], rstride=1, cstride=1, cmap=cm.viridis,
        linewidth=0, antialiased=True)
    ax.set_zlim(0, 10.5)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    title('concetracion bacterias');

diffuse(700)
