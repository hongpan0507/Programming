from pathlib import _Accessor

__author__ = 'hpan'

import numpy as np
import matplotlib.pyplot as pyplot
import math

from scipy import linalg
from cmath import exp
from numpy.linalg import inv
from scipy.integrate import nquad

#---------------------Constants-------------------------
pi = math.pi
mu_0 = 4*pi*1e-7    #permeability
epsilon_0 = 1e-9/(36*pi)    #permitivity
eta = 120*pi    #intrinsic impedance
dB_Np = 20/math.log(10,math.exp(1))     # 8.68 db per Np
c = 3e8
#-----------------------------------------------------------
pyplot.figure(1)

freq = 2.5e9
wave_len = c/freq
a = 0.005*wave_len
beta = 2*pi/wave_len

L = wave_len*0.47

resolution_array = np.linspace(11,231,21)
print(resolution_array)

for k in range (0, np.size(resolution_array)):
    resolution = resolution_array[k]
    del_z = L/resolution
    len = np.linspace(-1*L/2,L/2,resolution)
    z_mn = np.zeros([resolution,resolution], dtype=complex)

    def pock_int_diff_real(z_prime_n, z_m):
        const = 1/(1j*2*pi*freq*epsilon_0*4*pi)
        r_mn = math.sqrt(a**2 + (z_m - z_prime_n)**2) #distance between z and z_prime
        complex = const*exp(-1j*beta*r_mn)*((1+1j*beta*r_mn)*(2*(r_mn**2)-3*(a**2))+(beta*a*r_mn)**2)/(r_mn**5)
        return complex.real

    def pock_int_diff_img(z_prime_n, z_m):
        const = 1/(1j*2*pi*freq*epsilon_0*4*pi)
        r_mn = math.sqrt(a**2 + (z_m - z_prime_n)**2) #distance between z and z_prime
        complex = const*exp(-1j*beta*r_mn)*((1+1j*beta*r_mn)*(2*(r_mn**2)-3*(a**2))+(beta*a*r_mn)**2)/(r_mn**5)
        return complex.imag

    v = np.zeros(resolution)
    mid = math.floor(resolution/2)
    v[mid] = 1

    resolution = int(resolution)
    for m in range (0, resolution):
        for n in range (0, resolution):
            real = nquad(pock_int_diff_real,[[-1*L/2 + del_z*n,-1*L/2 + del_z*(n-1)],[-1*L/2 + del_z*m,-1*L/2 + del_z*(m-1)]])
            img = nquad(pock_int_diff_img,[[-1*L/2 + del_z*n,-1*L/2 + del_z*(n-1)],[-1*L/2 + del_z*m,-1*L/2 + del_z*(m-1)]])
            z_mn[m,n] = real[0] + 1j*img[0]

    #z_mn_inv = linalg.inv(z_mn)
    z_mn_inv = inv(z_mn)
    I = z_mn_inv.dot(v)
    I_mag = abs(I)

    z_feed = v[mid]/I[mid]
    print(z_feed)

    pyplot.plot(len, I_mag)

pyplot.show()

