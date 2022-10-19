#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:33:19 2022

@author: achilequarante
"""
import numpy as np
import matplotlib.pyplot as plt
from math import pi


def re_psi_x(x,t):
    return np.sin(12*pi*x)*np.cos(1.506*10*(-18)*t)+np.sin(13*pi*x)*np.cos(1.767*10*(-18)*t)

def im_psi_x(x,t):
    return np.sin(12*pi*x)*np.sin(1.506*10*(-18)*t)+np.sin(13*pi*x)*np.sin(1.767*10*(-18)*t)

def psi_sq(a,b):
    return (a**2+b**2)**0.5

def main():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    t = np.linspace(0,2.0, 1000)
    x = np.linspace(0,1.0, 1000)
    T,X = np.meshgrid(t,x)
    # print(X.shape)
    Z = (re_psi_x(X, T)**2 + im_psi_x(X,T)**2)**0.5
    # print(Z.shape)
    ax.contour3D(T, X, Z, 50, cmap = 'binary')#, rstride=10, cstride=10)
    ax.set_xlabel('Time')
    ax.set_ylabel('X')
    ax.set_zlabel('Psi_sq')
    plt.show()   
    
main()
    
