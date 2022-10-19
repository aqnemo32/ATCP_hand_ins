#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 16:48:44 2022

@author: achilequarante
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math import pi

def psi_sq (p,n):
    p_ = 2*pi*p
    return np.sin(13*pi*p) #+ 
            #((np.sin(11*pi*p)+np.sin(12*pi*p))*np.sin(-23*n))**2)
#((1/pi)*(((n/2)/((n/2)**2 - p**2))*(1-(-1)**n * np.cos(p_)))**2 +
#           (((n/2)/((n/2)**2 - p**2))*(-(-1)**n * np.sin(p_)))**2)**0.5

def main():
    n_init = 0
    p = np.arange(0,1,0.001)
    fig, ax = plt.subplots()
    axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
    fig.subplots_adjust(bottom=0.25)
   
    freq_slider = Slider(
    ax=axfreq,
    label='n',
    valmin = 0,
    valmax=6.0,
    valinit=0,
    valstep=0.1)
    line_0, = ax.plot(p, psi_sq(p,n_init))

    
    def update(val):
        line_0.set_ydata(psi_sq(p, freq_slider.val))
        fig.canvas.draw_idle()

    print(f"XXXXXXXXXXXX\n {freq_slider.val}\n XXXXXXXXXXXX")
    # register the update function with each slider
    freq_slider.on_changed(update)
    ax.set_xlabel('x')
    ax.set_ylabel('\Psi (x)')
    ax.set_title("LUMO+1 Eigenfunction")
    plt.show()
    

main()
