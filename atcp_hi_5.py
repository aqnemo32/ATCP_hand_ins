#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 12:55:56 2022

@author: achilequarante
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 5, 100)
t = [-5, -2,-1, 0, 1, 3, 5]
def P(x,t):
    return 1/(x**2 + 1)*np.sin(np.sqrt(x**2+1)*t/2)    

col = ['k', 'r', 'b', 'c', 'y', 'g', 'm']
for i in range(len(t)):
    plt.plot(x, P(x,t[i]), color = col[i], label = f't = {t[i]}')
    plt.xlabel('$\Omega^2$/($\omega_0 - \omega$)')
    plt.ylabel('P')
    plt.title('Random Title')
plt.legend()   
plt.show()

