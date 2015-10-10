from pathlib import _Accessor

__author__ = 'hpan'

import numpy as np
from numpy.linalg import inv
from numpy.linalg import eig

import matplotlib.pyplot as pyplot

import math

from cmath import exp

from scipy.integrate import nquad

#---------------------Constants-------------------------
pi = math.pi
mu_0 = 4*pi*1e-7    #permeability
epsilon_0 = 1e-9/(36*pi)    #permitivity
eta = 120*pi    #intrinsic impedance
dB_Np = 20/math.log(10,math.exp(1))     # 8.68 db per Np
c = 3e8
#-----------------------------------------------------------

resolution = 51
freq = 280e6
wave_len = c/freq
a = 1e-3
beta = 2*pi/wave_len
const = 1/(1j*2*pi*freq*epsilon_0*4*pi)
L = 0.5
del_z = L/resolution
len = np.linspace(-1*L/2,L/2,resolution)
seg = np.linspace(0,100,resolution)
z_mn = np.zeros([resolution,resolution], dtype=complex)

def pock_int_diff_real(z_prime_n, z_m):
    r_mn = math.sqrt(a**2 + (z_m - z_prime_n)**2) #distance between z and z_prime
    complex = const*exp(-1j*beta*r_mn)*((1+1j*beta*r_mn)*(2*(r_mn**2)-3*(a**2))+(beta*a*r_mn)**2)/(r_mn**5)
    return complex.real

def pock_int_diff_img(z_prime_n, z_m):
    r_mn = math.sqrt(a**2 + (z_m - z_prime_n)**2) #distance between z and z_prime
    complex = const*exp(-1j*beta*r_mn)*((1+1j*beta*r_mn)*(2*(r_mn**2)-3*(a**2))+(beta*a*r_mn)**2)/(r_mn**5)
    return complex.imag

v = np.zeros(resolution)
mid = math.floor(resolution/2)
v[mid] = 1

for m in range (0, resolution):
    for n in range (0, resolution):
        real = nquad(pock_int_diff_real,[[-1*L/2 + del_z*n,-1*L/2 + del_z*(n+1)],[-1*L/2 + del_z*m,-1*L/2 + del_z*(m+1)]])
        img = nquad(pock_int_diff_img,[[-1*L/2 + del_z*n,-1*L/2 + del_z*(n+1)],[-1*L/2 + del_z*m,-1*L/2 + del_z*(m+1)]])
        z_mn[m,n] = real[0] + 1j*img[0]

# z_mn_inv = inv(z_mn)
# I = -1*z_mn_inv.dot(v)
# I_mag = abs(I)

z_real = z_mn.real
z_img = z_mn.imag

z_real_inv = inv(z_real)

eig_val, eig_vector = eig(z_real_inv.dot(z_img))

#eig_val = eig_val/eig_val.max()

MS = abs(1/(1+1j*eig_val[resolution-1])) #modal significance

a_n = 180 - math.atan(eig_val[resolution-1])*180/pi

print("Eigen Value of J1:")
print(eig_val[resolution-1])
print("Modal Significance of J1:")
print(MS)
print("Characteristic Angle of J1:")
print(a_n)

pyplot.figure(2)

pyplot.title('hw 4 prob 1; frequency = 280MHz; N = 101')

pyplot.xlabel('Segments')
pyplot.ylabel('Eigen Value')

pyplot.plot(seg, eig_val, color = 'red')

pyplot.figure(1)

# for k in range (0,4):
#     pyplot.plot(len, eig_vector[:,resolution-k-1])
pyplot.title('hw 4 prob 1; frequency = 280MHz; N = 101')

pyplot.xlabel('Segments')
pyplot.ylabel('Eigen Currents (Jn)')

pyplot.plot(seg, eig_vector[:,resolution-1], color = 'red', label="J1")
pyplot.plot(seg, eig_vector[:,resolution-2], color = 'blue', label="J2")
pyplot.plot(seg, eig_vector[:,resolution-3], color = 'green', label="J3")
pyplot.plot(seg, eig_vector[:,resolution-4], color = 'black', label="J4")

pyplot.legend(loc='upper right', shadow=True)
pyplot.show()