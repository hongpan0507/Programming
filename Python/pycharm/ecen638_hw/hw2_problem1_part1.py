__author__ = 'hpan'


import numpy as np
import matplotlib.pyplot as pyplot
from scipy.integrate import quad

import cmath
import math
from math import sin
from math import cos


#---------------------Constants-------------------------
c = 3E8
pi = math.pi
mu_0 = 4*pi*1e-7    #permeability
epsilon_0 = 1e-9/(36*pi)    #permitivity
eta = 120*pi    #intrinsic impedance
dB_Np = 20/math.log(10,math.exp(1))     # 8.68 db per Np
#-----------------------------------------------------------
# hw 2 problem 1 part 1:
# hw 2 problem 1.a:
I_m = 1
resolution = 70
theta_array = np.linspace(0, 2*pi, resolution)  #theta = 2*pi for plot; to calculate radiation impedance, use theta = pi
L = np.linspace(-1/4, 1/4, resolution)

def A_theta_real_z(z_prime, theta):  # -1/4 <= z_prime <= 1/4; 0 <= theta <= pi
    complex = cmath.exp(1j*2*pi*cos(theta)*z_prime)
    A_theta_r = -1*sin(theta) * sin(2*pi*(1/4-abs(z_prime))) * complex.real
    return A_theta_r

def A_theta_img_z(z_prime, theta):  # -1/4 <= z_prime <= 1/4; 0 <= theta <= pi
    complex = cmath.exp(1j*2*pi*cos(theta)*z_prime)
    A_theta_i = -1*sin(theta) * sin(2*pi*(1/4-abs(z_prime))) * complex.imag
    return A_theta_i

def A_theta_mag(A_theta_r, A_theta_i):
    return math.sqrt(pow(A_theta_r,2)+pow(A_theta_i,2))

A_theta_r = np.zeros([resolution,resolution])
A_theta_r_size = np.shape(A_theta_r)    #get the size of a 2d array; row_size = [0]; column_size = [1]

#print('row size = %f' %A_theta_r_size[0])
#print('column size = %f' %A_theta_r_size[1])
i = 0
while i < A_theta_r_size[0]:   #row size; phi from 0 to 2*pi
    j = 0
    while j < A_theta_r_size[1]:    #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        A_theta_r_buff = quad(A_theta_real_z, -1/4, 1/4, args=(theta_temp))
        A_theta_r[i,j] = A_theta_r_buff[0]
        j+=1
    i+=1

A_theta_i = np.zeros([resolution,resolution])
A_theta_i_size = np.shape(A_theta_r)    #get the size of a 2d array; row_size = [0]; column_size = [1]
i = 0
while i < A_theta_r_size[0]:   #row size; phi from 0 to 2*pi
    j = 0
    while j < A_theta_r_size[1]:    #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        A_theta_i_buff = quad(A_theta_img_z, -1/4, 1/4, args=(theta_temp))
        A_theta_i[i][j] = A_theta_i_buff[0]
        j+=1
    i+=1

E_theta_m = np.zeros(resolution)
norm_factor = 0
i = 0
while i < np.size(E_theta_m):
    E_theta_m[i] = pow(A_theta_mag(A_theta_r[0][i], A_theta_i[0][i]), 2)
    if norm_factor < E_theta_m[i]:  #Finding max and use it to normalize
        norm_factor = E_theta_m[i]
    i+=1

P_density_max = norm_factor     #does not have constants included; used for directivity calculation

i = 0
while i < np.size(E_theta_m):
    E_theta_m[i] = E_theta_m[i]/norm_factor #normalize
    i+=1

pyplot.figure(1)
ax = pyplot.subplot(111, polar=True)
ax.set_theta_zero_location('N')
ax.set_theta_direction('clockwise')
ax.plot(theta_array, E_theta_m, color='r', linewidth=2)
ax.set_rmax(1)
ax.set_xticks(np.array([0, -45, -90, -135, 180, 135, 90, 45])/180*pi)
ax.set_title('hw 2 prob 1; Y-Z and X-Z plane')

E_theta_m = np.zeros(resolution)    #for X-Y plane
phi_array = np.linspace(0, 2*pi, resolution)
norm_factor = 0
i = 0
while i < np.size(E_theta_m):
    E_theta_m[i] = pow(A_theta_mag(A_theta_r[i][24], A_theta_i[i][24]), 2)  # 1/4 of 2*pi = pi/2
    if norm_factor < E_theta_m[i]:  #Finding max and use it to normalize
        norm_factor = E_theta_m[i]
    i+=1


i = 0
while i < np.size(E_theta_m):
    E_theta_m[i] = E_theta_m[i]/norm_factor #normalize
    i+=1

pyplot.figure(2)
ax = pyplot.subplot(111, polar=True)
ax.set_theta_zero_location('N')
ax.set_theta_direction('clockwise')
ax.plot(phi_array, E_theta_m, color='r', linewidth=3)
ax.set_rmax(1)
ax.set_xticks(np.array([0, -45, -90, -135, 180, 135, 90, 45])/180*pi)
ax.set_title('hw 2 prob 1; X-Y plane')


resolution = 100
theta_array = np.linspace(0, pi, resolution)  #theta = 2*pi for plot; to calculate radiation impedance, use theta = pi
phi_array = np.linspace(0, 2*pi, resolution)

A_theta_r = np.zeros([resolution,resolution])
A_theta_r_size = np.shape(A_theta_r)    #get the size of a 2d array; row_size = [0]; column_size = [1]

i = 0
while i < A_theta_r_size[0]:   #row size; phi from 0 to 2*pi
    j = 0
    while j < A_theta_r_size[1]:    #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        A_theta_r_buff = quad(A_theta_real_z, -1/4, 1/4, args=(theta_temp))
        A_theta_r[i,j] = A_theta_r_buff[0]
        j+=1
    i+=1

A_theta_i = np.zeros([resolution,resolution])
A_theta_i_size = np.shape(A_theta_r)    #get the size of a 2d array; row_size = [0]; column_size = [1]

i = 0
while i < A_theta_i_size[0]:   #row size; phi from 0 to 2*pi
    j = 0
    while j < A_theta_i_size[1]:    #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        A_theta_i_buff = quad(A_theta_img_z, -1/4, 1/4, args=(theta_temp))
        A_theta_i[i][j] = A_theta_i_buff[0]
        j+=1
    i+=1

P_rad = 0
for i in range(0, np.size(phi_array)):
    for j in range(0, np.size(theta_array)):
        P_rad = P_rad + pow((A_theta_r[i][j]),2)*sin(theta_array[j])*pi/resolution*2*pi/resolution

P_rad_total = P_rad # does not have the constants included; use for directivity calculation

P_rad = P_rad * 1/2 * (2*pi)**2 * eta / (4*pi)**2
R_rad = P_rad * 2
print('Radiation resistance: %f' %R_rad + ' ohms')

directivity_max = P_density_max*4*pi/P_rad_total  #max power density found in the previous step
print('Maximum directivity: %f' %directivity_max)

#assume operating at 2.4GHz
freq = 2.4e9
wave_len = c/freq
cross_section = wave_len**2 / (4*pi) * directivity_max
print('Antenna cross section at 2.4Ghz: %f' %cross_section + ' m^2') #cross section = effective aperture

pyplot.show()