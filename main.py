# 
# Name:Grating Diffraction Simulation
# Copyright:Seeyu Yuan
# Date:2021.12.12
#


import numpy as np
import matplotlib as m

m.use('TkAgg')
m.interactive(True)

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.widgets import Slider
from numpy import pi, linspace, sin, meshgrid
N = 800

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.45)
# Package some image display preferences in a dictionary object, for use below:
#myargs = {'interpolation': 'nearest', 'origin': 'lower', 'cmap': cm.nipy_spectral}
myargs = {'interpolation': 'nearest', 'origin': 'lower', 'cmap': cm.gray}


def desity(l_i,h_i,a_i,b_i,f_i,n_i):
    l_i= l_i *1.E-9
    h_i= h_i *1.E-3
    a_i= a_i *1.E-6
    b_i= b_i *1.E-6
    k = (2. * pi) / l_i
    X_Mmax = h_i / 2.
    X_Mmin = -h_i / 2.
    Y_Mmax = X_Mmax
    Y_Mmin = X_Mmin
    X = linspace(X_Mmin, X_Mmax, N)
    Y = X  # coordinates of screen
    # 2D & 3 D representation
    XX, YY = meshgrid(X, Y)
    B = (k * b_i * XX) / (2. * f_i)
    A = (k * a_i * XX) / (2. * f_i)  # intermediate variable
    # 1D representation
    I = (1 / n_i**2) * ((sin(B) / B)**2) * (sin(n_i * A) / sin(A))**2 #distribution of light
    return [I,X_Mmax,X_Mmin]


#set initial values
l_i= 632 
h_i= 15 
a_i= 2400 
b_i= 100 
f_i= 3
n_i= 20

I= desity(l_i,h_i,a_i,b_i,f_i,n_i)[0]

t = plt.imshow(I, **myargs)

ax = plt.axes([0.25,0.1,0.65,0.03])
l = Slider(ax, 'wavelength(nm)', 400, 780, valinit=l_i)  #set input slider

ax = plt.axes([0.25,0.15,0.65,0.03])
n = Slider(ax, 'number of slits', 1, 500, valinit=n_i, valstep=1)

ax = plt.axes([0.25,0.20,0.65,0.03])
h = Slider(ax, 'width of screen(m)', 5, 50, valinit=h_i)

ax = plt.axes([0.25,0.25,0.65,0.03])
f = Slider(ax, 'focal length(mm)', 1, 50, valinit=f_i)

ax = plt.axes([0.25,0.30,0.65,0.03])
b = Slider(ax, 'width of slit(µm)', 1, 1000, valinit=b_i)

ax = plt.axes([0.25,0.35,0.65,0.03])
a = Slider(ax, 'distance between slits(µm)', 100, 5000, valinit=a_i)


#read the value 
def update(val):
    l_i = l.val 
    n_i = n.val 
    h_i = h.val 
    f_i = f.val
    b_i = b.val   
    a_i = a.val 
    
    I= desity(l_i,h_i,a_i,b_i,f_i,n_i)[0]

    t.set_data(I)
    fig.canvas.draw_idle()


#refresh
l.on_changed(update)
n.on_changed(update)
h.on_changed(update)
f.on_changed(update)
b.on_changed(update)
a.on_changed(update)

plt.show(block=True)
