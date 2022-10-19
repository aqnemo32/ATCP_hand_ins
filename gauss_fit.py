#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:36:26 2022

@author: achilequarante
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import erf
filename = 'Dataset1.csv'#input('filename:')
dummy = []
f = open(filename, 'r')
for i in f:
    dummy.append(f.readline().split(','))
N = len(dummy)
print(N)
xdata = np.zeros(N)
ydata = np.zeros(N)    
for i in range(N):
    xdata[i] = dummy[i][0]
    ydata[i] = dummy[i][1]
    

  
# Define the fit function
def Gauss(t,sig,T,A):
    #sig = 50
    y = A/2 * np.exp(-t/T) * np.exp(-sig**2/(2*T**2)) * (
        1 + erf(1/np.sqrt(2) *(t/sig - sig/T)))
    return y

popt, pcov = curve_fit(Gauss, xdata, ydata)

print(popt)
print(popt[0]/(np.sqrt(2)))
fit_y = Gauss(xdata, popt[0], popt[1], popt[2])
r_squared = 1 - (np.sum((ydata- fit_y)**2)/(np.sum((ydata-np.mean(ydata))**2)))

plt.scatter(xdata, ydata, s = 1.0 ,c = 'k' , linewidth = 0.5, label='Data')
plt.plot(xdata, fit_y, '-', label='Fit')
plt.text(850, 0.7,f'$R^2$ = {r_squared:.5}\nFit Parameters:\n$\sigma_{{isol}}$ [fs] = {popt[0]/np.sqrt(2):.5}\n T  [fs]= {popt[1]:.5}\nA= {popt[2]:.5}',
     horizontalalignment='center',
     verticalalignment='center')
plt.xlabel('Time [fs]')
plt.ylabel('I(t) [Arbitrary unit]')
plt.title('Intensity versus Time (fs)')
plt.legend()
plt.show()