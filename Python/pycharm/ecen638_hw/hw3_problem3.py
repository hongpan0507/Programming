from pathlib import _Accessor

__author__ = 'hpan'


import matplotlib.pyplot as pyplot

import math
from math import sin
from math import cos

import cmath
from cmath import exp

import numpy as np
from numpy.linalg import inv

from scipy.integrate import nquad
from scipy.integrate import quad

#---------------------Constants-------------------------
pi = math.pi
mu_0 = 4*pi*1e-7    #permeability
epsilon_0 = 1e-9/(36*pi)    #permitivity
eta = 120*pi    #intrinsic impedance
dB_Np = 20/math.log(10,math.exp(1))     # 8.68 db per Np
c = 3e8
#-----------------------------------------------------------

freq_const = 2.5e9
wave_len_const = c/freq_const
L = wave_len_const*0.47
a = 0.005*wave_len_const

z_0 = 75
z_in = []
VSWR = []
freq_array = []

resolution = 101
del_z = L/resolution
z_mn = np.zeros([resolution,resolution], dtype=complex)
len = np.linspace(-1*L/2,L/2,resolution)

v = np.zeros(resolution)
mid = math.floor(resolution/2)
v[mid] = 1

#-------------------------------------N = 101; 2-3GHz; 25MHz per step------------------------------
for k in range (0, 41):
    freq = 2e9 + k*25e6
    freq_array.append(freq)
    wave_len = c/freq
    beta = 2*pi/wave_len
    const = 1/(1j*2*pi*freq*epsilon_0*4*pi)

    def pock_int_diff_real(z_prime_n, z_m):
        r_mn = math.sqrt(a**2 + (z_m - z_prime_n)**2) #distance between z and z_prime
        complex = const*exp(-1j*beta*r_mn)*((1+1j*beta*r_mn)*(2*(r_mn**2)-3*(a**2))+(beta*a*r_mn)**2)/(r_mn**5)
        return complex.real

    def pock_int_diff_img(z_prime_n, z_m):
        r_mn = math.sqrt(a**2 + (z_m - z_prime_n)**2) #distance between z and z_prime
        complex = const*exp(-1j*beta*r_mn)*((1+1j*beta*r_mn)*(2*(r_mn**2)-3*(a**2))+(beta*a*r_mn)**2)/(r_mn**5)
        return complex.imag

    for m in range (0, resolution):
        for n in range (0, resolution):
            real = nquad(pock_int_diff_real,[[-1*L/2 + del_z*n,-1*L/2 + del_z*(n+1)],[-1*L/2 + del_z*m,-1*L/2 + del_z*(m+1)]])
            img = nquad(pock_int_diff_img,[[-1*L/2 + del_z*n,-1*L/2 + del_z*(n+1)],[-1*L/2 + del_z*m,-1*L/2 + del_z*(m+1)]])
            z_mn[m,n] = real[0] + 1j*img[0]

    z_mn_inv = inv(z_mn)
    I = -1*z_mn_inv.dot(v)
    z_feed = v[mid]/I[mid]
    z_in.append(z_feed)

    z_norm = z_feed/z_0
    gamma = (z_norm - 1)/(z_norm + 1)
    S = (1+abs(gamma))/(1-abs(gamma))
    VSWR.append(S)

    print('Frequency in MHz = %f ' %(freq/1e6))
    if z_feed.imag < 0 :
        print('Zin = %f - %fj' %(z_feed.real, z_feed.imag*-1))
    else:
        print('Zin = %f + %fj' %(z_feed.real, z_feed.imag))
    # print('Zin real = %f' %z_feed.real)
    # print('Zin img = %f' %z_feed.imag)
    print('VSWR = %f' %S)

pyplot.figure(1)
pyplot.title('hw 3 prob 3')
pyplot.xlabel('Frequency (GHz)')
pyplot.ylabel('Zin (ohm)')
pyplot.plot(freq_array,z_in,color="green")

pyplot.figure(2)
pyplot.title('hw 3 prob 3')
pyplot.xlabel('Frequency (GHz)')
pyplot.ylabel('VSWR')
pyplot.ylim(ymin = 1)
pyplot.plot(freq_array,VSWR,color="green")

pyplot.show()

