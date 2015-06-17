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


freq = 2.5e9
wave_len = c/freq
a = 0.005*wave_len
beta = 2*pi/wave_len
const = 1/(1j*2*pi*freq*epsilon_0*4*pi)
L = wave_len*0.47

def pock_int_diff_real(z_prime_n, z_m):
    r_mn = math.sqrt(a**2 + (z_m - z_prime_n)**2) #distance between z and z_prime
    complex = const*exp(-1j*beta*r_mn)*((1+1j*beta*r_mn)*(2*(r_mn**2)-3*(a**2))+(beta*a*r_mn)**2)/(r_mn**5)
    return complex.real

def pock_int_diff_img(z_prime_n, z_m):
    r_mn = math.sqrt(a**2 + (z_m - z_prime_n)**2) #distance between z and z_prime
    complex = const*exp(-1j*beta*r_mn)*((1+1j*beta*r_mn)*(2*(r_mn**2)-3*(a**2))+(beta*a*r_mn)**2)/(r_mn**5)
    return complex.imag

#-------------------------------------N = 11; current distribution------------------------------
resolution = 11
del_z = L/resolution
z_mn = np.zeros([resolution,resolution], dtype=complex)
len = np.linspace(-1*L/2,L/2,resolution)

v = np.zeros(resolution)
mid = math.floor(resolution/2)
v[mid] = 1

for m in range (0, resolution):
    for n in range (0, resolution):
        real = nquad(pock_int_diff_real,[[-1*L/2 + del_z*n,-1*L/2 + del_z*(n+1)],[-1*L/2 + del_z*m,-1*L/2 + del_z*(m+1)]])
        img = nquad(pock_int_diff_img,[[-1*L/2 + del_z*n,-1*L/2 + del_z*(n+1)],[-1*L/2 + del_z*m,-1*L/2 + del_z*(m+1)]])
        z_mn[m,n] = real[0] + 1j*img[0]

z_mn_inv = inv(z_mn)
I = -1*z_mn_inv.dot(v)
I_mag1 = abs(I)

z_feed = v[mid]/I[mid]
print(z_feed)

pyplot.figure(1)
pyplot.plot(len, I_mag1, color="red")

#-------------------------------------N = 51; current distribution------------------------------
resolution = 51
del_z = L/resolution
z_mn = np.zeros([resolution,resolution], dtype=complex)
len = np.linspace(-1*L/2,L/2,resolution)

v = np.zeros(resolution)
mid = math.floor(resolution/2)
v[mid] = 1

for m in range (0, resolution):
    for n in range (0, resolution):
        real = nquad(pock_int_diff_real,[[-1*L/2 + del_z*n,-1*L/2 + del_z*(n+1)],[-1*L/2 + del_z*m,-1*L/2 + del_z*(m+1)]])
        img = nquad(pock_int_diff_img,[[-1*L/2 + del_z*n,-1*L/2 + del_z*(n+1)],[-1*L/2 + del_z*m,-1*L/2 + del_z*(m+1)]])
        z_mn[m,n] = real[0] + 1j*img[0]


z_mn_inv = inv(z_mn)
I = z_mn_inv.dot(v)
I_mag2 = abs(I)

z_feed = -1*v[mid]/I[mid]
print(z_feed)
pyplot.plot(len, I_mag2, color="blue")

#-------------------------------------N = 101; current distribution------------------------------
resolution = 101
del_z = L/resolution
z_mn = np.zeros([resolution,resolution], dtype=complex)
len = np.linspace(-1*L/2,L/2,resolution)

v = np.zeros(resolution)
mid = math.floor(resolution/2)
v[mid] = 1

for m in range (0, resolution):
    for n in range (0, resolution):
        real = nquad(pock_int_diff_real,[[-1*L/2 + del_z*n,-1*L/2 + del_z*(n+1)],[-1*L/2 + del_z*m,-1*L/2 + del_z*(m+1)]])
        img = nquad(pock_int_diff_img,[[-1*L/2 + del_z*n,-1*L/2 + del_z*(n+1)],[-1*L/2 + del_z*m,-1*L/2 + del_z*(m+1)]])
        z_mn[m,n] = real[0] + 1j*img[0]

#z_mn_inv = linalg.inv(z_mn)
z_mn_inv = inv(z_mn)
I = -1*z_mn_inv.dot(v)
I_mag3 = abs(I)

z_feed = v[mid]/I[mid]
print(z_feed)
pyplot.plot(len, I_mag3, color="green")

#-------------------------------------power pattern------------------------------
def A_theta_real(primed,theta, phi, I_mag, I_seg):
    complex = cmath.exp(1j*2*pi/wave_len*(primed*cos(theta)))    # only z' changes
    A_theta_r = -1*sin(theta) * I_mag[I_seg] * complex.real
    return A_theta_r

def A_theta_img(primed,theta, phi, I_mag, I_seg):
    complex = cmath.exp(1j*2*pi/wave_len*(primed*cos(theta)))    # only z' changes
    A_theta_i = -1*sin(theta) * I_mag[I_seg] * complex.imag
    return A_theta_i

def mag(A_theta_r, A_theta_i):
    return pow(math.sqrt(pow(A_theta_r,2)+pow(A_theta_i,2)),2)

theta_phi = 100     #theta and phi resolution
theta_array = np.linspace(0, 2*pi, theta_phi)  #theta = 2*pi for plot; to calculate radiation impedance, use theta = pi
phi_array = np.linspace(0, 2*pi, theta_phi)
#-------------------------------------N = 11; power pattern------------------------------
resolution = 11     #current resolution

A_theta_r = np.zeros([theta_phi,theta_phi])
A_theta_r_size = np.shape(A_theta_r)    #get the size of a 2d array; row_size = [0]; column_size = [1]
A_theta_r_temp = np.zeros([theta_phi,theta_phi])

A_theta_i = np.zeros([theta_phi,theta_phi])
A_theta_i_size = np.shape(A_theta_i)    #get the size of a 2d array; row_size = [0]; column_size = [1]
A_theta_i_temp = np.zeros([theta_phi,theta_phi])

for k in range(0, resolution):
    lower_bound = -L/2 + L/resolution*k   #Length of the dipole = 0.47*wave length
    upper_bound = -L/2 + L/resolution*(k+1)
    for i in range(0, A_theta_r_size[0]):   #row size; phi from 0 to 2*pi
        for j in range(0, A_theta_r_size[1]):   #column size: theta from 0 to 2*pi
            theta_temp = theta_array[j]
            phi_temp = phi_array[i]
            A_theta_r_buff = quad(A_theta_real, lower_bound, upper_bound, args=(theta_temp,phi_temp, I_mag1,k))
            A_theta_r_temp[i,j] = A_theta_r_buff[0]
            A_theta_i_buff = quad(A_theta_img, lower_bound, upper_bound, args=(theta_temp,phi_temp, I_mag1,k))
            A_theta_i_temp[i,j] = A_theta_i_buff[0]
    A_theta_r = A_theta_r + A_theta_r_temp
    A_theta_i = A_theta_i + A_theta_i_temp
    A_theta_i_temp = np.zeros([theta_phi,theta_phi])

## no A_phi term

A_theta_m_11 = np.zeros([theta_phi,theta_phi])
for i in range(0, theta_phi):   #row size; phi from 0 to 2*pi
    for j in range(0, theta_phi):   #column size: theta from 0 to pi
        A_theta_m_11[i,j] = mag(A_theta_r[i,j], A_theta_i[i,j])

#-------------------------------------N = 51; power pattern------------------------------
resolution = 51     #current resolution

A_theta_r = np.zeros([theta_phi,theta_phi])
A_theta_r_size = np.shape(A_theta_r)    #get the size of a 2d array; row_size = [0]; column_size = [1]
A_theta_r_temp = np.zeros([theta_phi,theta_phi])

A_theta_i = np.zeros([theta_phi,theta_phi])
A_theta_i_size = np.shape(A_theta_i)    #get the size of a 2d array; row_size = [0]; column_size = [1]
A_theta_i_temp = np.zeros([theta_phi,theta_phi])

for k in range(0, resolution):
    lower_bound = -L/2 + L/resolution*k   #Length of the dipole = 0.47*wave length
    upper_bound = -L/2 + L/resolution*(k+1)
    for i in range(0, A_theta_r_size[0]):   #row size; phi from 0 to 2*pi
        for j in range(0, A_theta_r_size[1]):   #column size: theta from 0 to 2*pi
            theta_temp = theta_array[j]
            phi_temp = phi_array[i]
            A_theta_r_buff = quad(A_theta_real, lower_bound, upper_bound, args=(theta_temp,phi_temp, I_mag2,k))
            A_theta_r_temp[i,j] = A_theta_r_buff[0]
            A_theta_i_buff = quad(A_theta_img, lower_bound, upper_bound, args=(theta_temp,phi_temp, I_mag2,k))
            A_theta_i_temp[i,j] = A_theta_i_buff[0]
    A_theta_r = A_theta_r + A_theta_r_temp
    A_theta_i = A_theta_i + A_theta_i_temp
    A_theta_i_temp = np.zeros([theta_phi,theta_phi])

## no A_phi term

A_theta_m_51 = np.zeros([theta_phi,theta_phi])
for i in range(0, theta_phi):   #row size; phi from 0 to 2*pi
    for j in range(0, theta_phi):   #column size: theta from 0 to pi
        A_theta_m_51[i,j] = mag(A_theta_r[i,j], A_theta_i[i,j])

#-------------------------------------N = 101; power pattern------------------------------
resolution = 101     #current resolution

A_theta_r = np.zeros([theta_phi,theta_phi])
A_theta_r_size = np.shape(A_theta_r)    #get the size of a 2d array; row_size = [0]; column_size = [1]
A_theta_r_temp = np.zeros([theta_phi,theta_phi])

A_theta_i = np.zeros([theta_phi,theta_phi])
A_theta_i_size = np.shape(A_theta_i)    #get the size of a 2d array; row_size = [0]; column_size = [1]
A_theta_i_temp = np.zeros([theta_phi,theta_phi])

for k in range(0, resolution):
    lower_bound = -L/2 + L/resolution*k   #Length of the dipole = 0.47*wave length
    upper_bound = -L/2 + L/resolution*(k+1)
    for i in range(0, A_theta_r_size[0]):   #row size; phi from 0 to 2*pi
        for j in range(0, A_theta_r_size[1]):   #column size: theta from 0 to 2*pi
            theta_temp = theta_array[j]
            phi_temp = phi_array[i]
            A_theta_r_buff = quad(A_theta_real, lower_bound, upper_bound, args=(theta_temp,phi_temp, I_mag3,k))
            A_theta_r_temp[i,j] = A_theta_r_buff[0]
            A_theta_i_buff = quad(A_theta_img, lower_bound, upper_bound, args=(theta_temp,phi_temp, I_mag3,k))
            A_theta_i_temp[i,j] = A_theta_i_buff[0]
    A_theta_r = A_theta_r + A_theta_r_temp
    A_theta_i = A_theta_i + A_theta_i_temp
    A_theta_i_temp = np.zeros([theta_phi,theta_phi])

## no A_phi term

A_theta_m_101 = np.zeros([theta_phi,theta_phi])
for i in range(0, theta_phi):   #row size; phi from 0 to 2*pi
    for j in range(0, theta_phi):   #column size: theta from 0 to pi
        A_theta_m_101[i,j] = mag(A_theta_r[i,j], A_theta_i[i,j])
#---------------------------------Normalize------------------------------------------------

norm_factor_array = np.array([A_theta_m_11.max(),A_theta_m_51.max(), A_theta_m_101.max()])
norm_factor = norm_factor_array.max()

for i in range(0, theta_phi):   #row size; phi from 0 to 2*pi
    for j in range(0, theta_phi):   #column size: theta from 0 to pi
        A_theta_m_11[i,j] = A_theta_m_11[i,j]/norm_factor
        A_theta_m_51[i,j] = A_theta_m_51[i,j]/norm_factor
        A_theta_m_101[i,j] = A_theta_m_101[i,j]/norm_factor

pyplot.figure(2)
ax = pyplot.subplot(111, polar=True)
ax.set_theta_zero_location('N')
ax.set_theta_direction('clockwise')
ax.set_yticks(np.array([0, 0.5, 1, 1.5]))
ax.set_xticks(np.array([0, -45, -90, -135, 180, 135, 90, 45])/180*pi)
ax.set_title('hw 3 prob 2; E_theta at X-Z plane')

ax.plot(theta_array, A_theta_m_11[0,:], color='r', linewidth=2)
ax.plot(theta_array, A_theta_m_51[0,:], color='b', linewidth=2)
ax.plot(theta_array, A_theta_m_101[0,:], color='g', linewidth=2)

pyplot.figure(3)
ax = pyplot.subplot(111, polar=True)
ax.set_theta_zero_location('N')
ax.set_theta_direction('clockwise')
ax.set_yticks(np.array([0, 0.5, 1, 1.5]))
ax.set_xticks(np.array([0, -45, -90, -135, 180, 135, 90, 45])/180*pi)
ax.set_title('hw 3 prob 2; E_theta at Y-Z plane')

ax.plot(theta_array, A_theta_m_11[24,:], color='r', linewidth=2)
ax.plot(theta_array, A_theta_m_51[24,:], color='b', linewidth=2)
ax.plot(theta_array, A_theta_m_101[24,:], color='g', linewidth=2)

pyplot.figure(4)
ax = pyplot.subplot(111, polar=True)
ax.set_theta_zero_location('N')
ax.set_theta_direction('clockwise')
ax.set_yticks(np.array([0, 0.5, 1, 1.5]))
ax.set_xticks(np.array([0, -45, -90, -135, 180, 135, 90, 45])/180*pi)
ax.set_title('hw 3 prob 2; E_theta at X-Y plane')

ax.plot(theta_array, A_theta_m_11[:,24], color='r', linewidth=2)
ax.plot(theta_array, A_theta_m_51[:,24], color='b', linewidth=2)
ax.plot(theta_array, A_theta_m_101[:,24], color='g', linewidth=2)
# pyplot.polar(theta_array, A_theta_m_11[:,24], color='r', linewidth=2)
# pyplot.plot(theta_array, A_theta_m_51[:,24], color='b', linewidth=2)
# pyplot.plot(theta_array, A_theta_m_101[:,24], color='g', linewidth=2)

pyplot.show()
