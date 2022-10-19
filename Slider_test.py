#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:05:15 2022

@author: achilequarante
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


# The parametrized function to be plotted
def f(t, L, n):
    return L * np.sin(2 * np.pi * n * t)

t = np.linspace(0, 1, 1000)

# Define initial parameters
init_amplitude = 1
init_frequency = 1

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
line, = ax.plot(t, f(t, init_amplitude, init_frequency), lw=2)
ax.set_xlabel('Time [s]')
n_list =[]
for i in range(1,21):
    n_list.append(i)
x=0
n_list=np.array(n_list)
# adjust the main plot to make room for the sliders
fig.subplots_adjust(bottom=0.25)

# Make a horizontal slider to control the frequency.
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label='Frequency [Hz]',
    valmin = 0,
    valmax=20,
    valinit=init_frequency,
    valstep=n_list)

# Make a vertically oriented slider to control the amplitude
#axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])



# The function to be called anytime a slider's value changes
def update(val):
    line.set_ydata(f(t,init_amplitude, freq_slider.val))
    fig.canvas.draw_idle()


# register the update function with each slider
freq_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')



plt.show()