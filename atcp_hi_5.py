#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 12:55:56 2022

@author: achilequarante
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
N = 1000

x = np.linspace(-10, 10, N)
om =np.array([1,2,3,4,np.pi+0.1,np.pi,np.pi-0.1])
def P(x,t,om):
    return 1/(x**2 + 1)*np.sin(np.sqrt(x**2+1)*t/2*om)**2  

def P_mb(x,v,alpha):
    return 2 * 1/(x**2 + 1) * (np.sin(np.sqrt(x**2+1)/(2*v*alpha)))**2 * v**3 * np.exp(-v**2)

def P_ram(x,t,T, om):
    om = 1
    a = np.sqrt(x**2+1)
    return 4/a**2 * (np.sin(a*t/2))**2 * (
        np.cos(x*T/2)*np.cos(a*t/2) - x/(
            a)*np.sin(x*T/2)*np.sin(a*t/2))**2

def avg_P_ram_s(x,v):
    return 2 * np.exp(-(v**2)) * v**3 * np.square((np.sin(1/0.3*v))
                                                        ) * np.square(np.cos(x/2*0.3*v))

def avg_P_ram_l(x,v):
    a = np.sqrt(x**2+1)
    return 4/a**2 * np.exp(-(v**2)) * v**3 * (np.sin(a/2*0.3*v)**2) * (
        1 - 1/a**2 * (np.sin(a/2*0.3*v))**2)

col = ['k', 'r', 'b', 'g', 'y', 'b', 'm']
for i in range(len(om)):
    plt.plot(x, P(x,1,om[i]), color = col[i], label = f't = {om[i]:.5}', lw = 0.8)

    plt.xlabel('$\omega_0 - \omega$)/$\Omega$')
    plt.ylabel('P')
    plt.title('P versus $(\omega_0 - \omega$)/$\Omega$')
plt.legend()   
plt.show()
plt.clf()
for i in range(3):
    plt.plot(x, P(x,1,om[i+4]), color = col[i], label = f't= {om[i+4]:.5}', lw = 0.8)
    plt.ylim(0.993, 1.001)
    plt.xlim(-0.2, 0.2)
    plt.xlabel('$\omega_0 - \omega$)/$\Omega$')
    plt.ylabel('P')
    plt.title('P versus $$(\omega_0 - \omega$)/$\Omega$')
plt.legend()   
plt.show()
plt.clf()
alpha = np.array([0.1,0.3,0.5,0.8,1.0])
int_p = np.zeros((len(alpha),1000))
for j in range(len(alpha)):
    
    for i in range(1000):
            the =  quad( lambda v: P_mb(x[i], v, alpha[j]),0, np.inf )
            int_p[j,i] = the[0]

for i in range(len(alpha)):
    plt.plot(x,int_p[i], color = col[i], label = f'a = {alpha[i]:.5}', lw=0.8)
    plt.xlabel('$\omega_0 - \omega$)/$\Omega$')
    plt.ylabel('<P($\Delta\omega$>')
    plt.title('<P($\Delta\omega$> versus $(\omega_0 - \omega$)/$\Omega$')
    plt.legend()
plt.show()
plt.clf()

x_ = np.linspace(-1.5, 1.5, N)
x__ = x_ * 20
T = np.array([10,50,10,50,3,3,1],dtype = 'float')
t = np.array([3,3,1,1,10,50,np.pi],dtype = 'float')
for i in range(len(T)):
    plt.plot(x_, P_ram(x_,t[i], T[i],1),lw=0.8 ,color = col[i], 
              label = f't = {t[i]:.5}\nT = {T[i]:.5}')
    plt.xlabel('($\omega_0 - \omega$)/$\Omega$')
    plt.ylabel('P_ram')
    plt.title('P_ram vesus $(\omega_0 - \omega$)/$\Omega$')
    plt.legend()   
    plt.show()
    plt.clf()

part_e = np.zeros(N)
part_r = np.zeros(N)
for i in range(N):
    th = quad(lambda v: avg_P_ram_s(x_[i]*50, v), 0.001, np.inf )
    thi = quad(lambda v: avg_P_ram_l(x__[i], v), 0.001, np.inf )
    part_e[i] = th[0]
    part_r[i] = thi[0]
plt.plot(x_*50, part_e,lw=0.8 ,color = 'k', label = '$\Delta\omega << \Omega_R$, near')
plt.xlabel('$\omega_0 - \omega$)/$\Omega$')
plt.ylabel('<P_ram>')
plt.title('<P_ram> vesus $(\omega_0 - \omega$)/$\Omega$')
plt.legend()   
plt.show()
plt.clf()
    
plt.plot(x__, part_r,lw=0.8 ,color = 'r', label = 'far')
plt.xlabel('$\omega_0 - \omega$)/$\Omega$')
plt.ylabel('<P_ram>')
plt.title('<P_ram> vesus $(\omega_0 - \omega$)/$\Omega$')
plt.legend()   
plt.show()
plt.clf()
