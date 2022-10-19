#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 18:18:11 2022

@author: achilequarante
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks

filename = input('File Name: ')
f = open(filename, 'r')

labels = f.readline().split(',')

dummy = []
for i in f:
    dummy.append(f.readline().split(','))

N = len(dummy)
print(N)
time = np.zeros(N)
volt = np.zeros(N)

for i in range(len(dummy)):
    time[i] = float(dummy[i][0])
    volt[i] = float(dummy[i][1])

time_f = fftfreq(N, (time[1]-time[0])/N)[:N//2]
volt_f = fft(volt)

if labels[0][0] == 's' or labels[0][0] == 'S':
    plt.title('Voltage (V) versus Time (s) (110 Hz)')
    plt.plot(time, volt)
else:
    plt.title('dBV versus Frequency (Hz)')
    plt.plot(time,(volt+60))
plt.xlabel(f'Time (s)')
plt.ylabel(f'Votage (V)')
plt.show()
volt_f_abs = 2/N * np.absolute(volt_f[:N//2])
# peak, _ = find_peaks(volt_f_abs,height = 0.1)
# print(peak)
plt.plot(time_f/1000, volt_f_abs*400)
plt.title('FFT versus Frequency (Hz)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('FFT (dBV)')
plt.show()