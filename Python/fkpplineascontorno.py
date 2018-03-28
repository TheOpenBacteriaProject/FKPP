# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 23:24:33 2017

@author: booort
"""

from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show

# the function that I'm going to plot
def z_func(x,y):
 return 0.05*exp(-5*x**2)*exp(-5*y**2)
 
x = arange(-3.0,3.0,0.1)
y = arange(-3.0,3.0,0.1)
X,Y = meshgrid(x, y) # grid of point
Z = z_func(X, Y) # evaluation of the function on the grid




im = imshow(u,cmap=cm.plasma) # drawing the function
# adding the Contour lines with labels
cset = contour(u,arange(0,1,0.3),linewidths=1,cmap=cm.Set1)
clabel(cset,inline=True,fmt='%1.1f',fontsize=10)
colorbar(im) # adding the colobar on the right
# latex fashion title
title('concetracion bacterias')
show()
