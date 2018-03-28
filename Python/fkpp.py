# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:39:46 2017

@author: booort
"""
from math import *
from matplotlib import *
from scipy import *
from numpy import *
import matplotlib.pyplot as plt
import time
start_time = time.time()


r=1
h=1
k=0.05
T=800
D=1
def u_0(x):
    return 0.05*math.e**(-5*x**2)

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
u=[]
x=[]
u_f=[]
for i in my_range(-50, 50, h):
    x.append(i)
    u.append(u_0(i))
    
plt.plot(x, u, 'ro')
plt.axis([-51, 51, 0, 0.5])
plt.show()
u_aux=u
u_matr=[]
for t  in range (1,4000):
    u_f.append(u_aux[0])
    for j in range(1,100):
        uu=u_aux[j]+((k*D)/h**2)*(u_aux[j+1]-2*u_aux[j]+u_aux[j-1])+k*r*u_aux[j]-k*r*(u_aux[j])**2
        u_f.append(uu)
    u_f.append(u_aux[100])
    u_matr.append(u_f)
    u_aux=u_f
    u_f=[]  

    t=t+1
plt.plot(x, u_aux, 'ro')
plt.axis([-51, 51, 0, 1])
plt.show()    
plt.savefig('foo.png')    
print("--- %s seconds ---" % (time.time() - start_time))    
    
    
    
    
    
    
    
    
    
    
    
    
    
