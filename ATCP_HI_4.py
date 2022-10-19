#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 14:38:22 2022

@author: achilequarante
"""
import numpy as np
from scipy.special import erf
import matplotlib.pyplot as plt

def I_t(t, sig, T):
    return 1/2 * np.exp(-t/T) * np.exp(-sig**2/(2*T**2)) * (
        1 + erf(1/2**0.5 *(t/sig - sig/T)))


t = np.linspace(-3, 5, 1000)
sig_in = np.linspace(0.1,1.0,6)
T_in = 1.0
colors = ['k', 'b' , 'g', 'r' ,'c', 'm']
fig, ax = plt.subplots()
for i in range(6):
    ax.plot(t, I_t(t, sig_in[i], T_in), lw=0.5, color = colors[i],
                    label = f'$\sigma$/T = {sig_in[i]/T_in:.5}')
ax.set_xlabel('Time [fs]')
ax.set_ylabel('I(t) [Arbitrary unit]')
ax.set_title('Intensity versus Time (fs)')
ax.legend()

# fig.subplots_adjust(left=0.25, bottom=0.25)

# axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])

# sig_slider = Slider(
#     ax=axfreq,
#     label='sigma',
#     valmin=0.01,
#     valmax=1,
#     valinit=sig_in,
# )

# axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
# T_slider = Slider(
#     ax=axamp,
#     label="T",
#     valmin=0.01,
#     valmax=1,
#     valinit=T_in,
#     orientation="vertical"
# )
# def update(val):
#     line.set_ydata(I_t(t, sig_slider.val, T_slider.val))
#     fig.canvas.draw_idle()


# # register the update function with each slider
# sig_slider.on_changed(update)
# T_slider.on_changed(update)
plt.show()