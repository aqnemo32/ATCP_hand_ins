#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:28:03 2022

@author: achilequarante
"""

import numpy as np
import matplotlib.pyplot as plt
from math import pi

from matplotlib.widgets import Slider

def re_psi_x_12(x,t):
    return (np.sin(11*pi*x)+np.sin(12*pi*x))*np.cos(23*t)
#1.506*10**(-8)*
#1.767*10**(-8)*
def im_psi_x_12(x,t):
    return (np.sin(11*pi*x)+np.sin(12*pi*x))*np.sin(23*t)

def re_psi_x_13(x,t):
    return np.sin(11*pi*x)*np.cos(48*t)+np.sin(13*pi*x)*np.cos(48*t)
#1.506*10**(-8)*
#1.767*10**(-8)*
def im_psi_x_13(x,t):
    return np.sin(11*pi*x)*np.sin(48*t)+np.sin(13*pi*x)*np.sin(48*t)
def main():
    t = np.linspace(0,3, 1000)
    x = np.linspace(0,1, 1000)
    
    
    fig, ax = plt.subplots()
    #line, = ax.plot(x, (re_psi_x_12(x,t)**2+im_psi_x_12(x, t)**2)**0.5, lw=2)
    axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
    fig.subplots_adjust(bottom=0.25)
   
    freq_slider = Slider(
    ax=axfreq,
    label='n',
    valmin = 0,
    valmax=3,
    valinit=0,
    valstep=0.1)
    line_0, = ax.plot(x, (re_psi_x_12(x,0)**2+im_psi_x_12(x, 0)**2)**0.5)

    
    def update(val):
        line_0.set_ydata((re_psi_x_12(
            x,freq_slider.val)**2+im_psi_x_12(x, freq_slider.val)**2)**0.5)
        fig.canvas.draw_idle()

    print(f"XXXXXXXXXXXX\n {freq_slider.val}\n XXXXXXXXXXXX")
    # register the update function with each slider
    freq_slider.on_changed(update)
    ax.set_xlabel('x')
    ax.set_ylabel('Psi^2')
    plt.show()
    # plt.plot(t,((re_psi_x_12(x,t)**2+im_psi_x_12(x, t)**2)**0.5))
    # plt.plot(t,((re_psi_x_13(x,t)**2+im_psi_x_13(x, t)**2)**0.5))
    # plt.show()

main()