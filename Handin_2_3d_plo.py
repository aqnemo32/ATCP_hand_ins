#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:33:19 2022

@author: achilequarante
"""
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from matplotlib import cm

def re_psi_x(x,t):
    return np.sin(12*pi*x)*np.cos(17/2.5*t)+np.sin(13*pi*x)*np.cos(20/2.5*t)
#1.506*10**(-8)*
#1.767*10**(-8)*
def im_psi_x(x,t):
    return np.sin(12*pi*x)*np.sin(17/2.5*t)+np.sin(13*pi*x)*np.sin(20/2.5*t)

def psi_sq(a,b):
    return (a**2+b**2)**0.5

def main():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    t = np.linspace(0,10, 1000)
    x = np.linspace(0,1, 1000)
    T,L = np.meshgrid(t,x)
    Z = np.absolute(re_psi_x(L, T)+ im_psi_x(L,T))
    #Z = (re_psi_x(L,T)**2+im_psi_x(L, T)**2)**0.5
    
    ax.contour3D(L, T, Z, 80, cmap = cm.viridis)
    ax.set_xlabel('X')
    ax.set_ylabel('T')
    ax.set_zlabel('Psi$^2$')
    plt.show()   
    
    #ax_1.plot_surface(L, T, Z, cmap=cm.coolwarm,
                       #linewidth=0, antialiased=False)
    #plt.show()
main()
    
