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

resolution = 11
a = 0.5e-3
L = 0.5     #wire length

freq_start = 100e6
freq_stop = 1000e6
freq_step = 50

freq_array = np.linspace(freq_start,freq_stop, freq_step)

eig_value_array1 = []
MS_array1 = []
a_n_array1 = []

eig_value_array2 = []
MS_array2 = []
a_n_array2 = []

eig_value_array3 = []
MS_array3 = []
a_n_array3 = []

eig_value_array4 = []
MS_array4 = []
a_n_array4 = []

for k in range (0, np.size(freq_array)):
    freq = freq_array[k]
    wave_len = c/freq

    beta = 2*pi/wave_len
    const = 1/(1j*2*pi*freq*epsilon_0*4*pi)
    print('Frequency in MHz = %f ' %(freq/1e6))

    del_z = L/resolution
    len = np.linspace(-1*L/2,L/2,resolution)
    seg = np.linspace(0,100,resolution)
    z_mn = np.zeros([resolution,resolution], dtype=complex)

    def pock_int_diff_real(z_m, z_prime_n):
        r_mn = math.sqrt(a**2 + (z_m-z_prime_n)**2) #distance between z and z_prime
        complex = const*exp(-1j*beta*r_mn)*((1+1j*beta*r_mn)*(2*(r_mn**2)-3*(a**2))+(beta*a*r_mn)**2)/(r_mn**5)
        return complex.real

    def pock_int_diff_img(z_m, z_prime_n):
        r_mn = math.sqrt(a**2 + (z_m-z_prime_n)**2) #distance between z and z_prime
        complex = const*exp(-1j*beta*r_mn)*((1+1j*beta*r_mn)*(2*(r_mn**2)-3*(a**2))+(beta*a*r_mn)**2)/(r_mn**5)
        return complex.imag

    for m in range (0, resolution):
        for n in range (0, resolution):
            real = nquad(pock_int_diff_real,[[-1*L/2 + del_z*m,-1*L/2 + del_z*(m+1)], [-1*L/2 + del_z*n,-1*L/2 + del_z*(n+1)]])
            img = nquad(pock_int_diff_img,[[-1*L/2 + del_z*m,-1*L/2 + del_z*(m+1)],[-1*L/2 + del_z*n,-1*L/2 + del_z*(n+1)]])
            z_mn[m,n] = real[0] + 1j*img[0]

    # z_mn_inv = inv(z_mn)
    # I = -1*z_mn_inv.dot(v)
    # I_mag = abs(I)

    z_real = z_mn.real
    z_img = z_mn.imag

    z_real_inv = inv(z_real)

    eig_val, eig_vector = eig(z_real_inv.dot(z_img))

    #J1
    eig_value1 = eig_val[resolution-1]
    MS1 = abs(1/(1+1j*eig_val[resolution-1])) #modal significance
    a_n1 = 180 - math.atan(eig_val[resolution-1])*180/pi
    eig_value_array1.append(eig_value1)
    MS_array1.append(MS1)
    a_n_array1.append(a_n1)

    #J2
    eig_value2 = eig_val[resolution-2]
    MS2 = abs(1/(1+1j*eig_val[resolution-2])) #modal significance
    a_n2 = 180 - math.atan(eig_val[resolution-2])*180/pi
    eig_value_array2.append(eig_value2)
    MS_array2.append(MS2)
    a_n_array2.append(a_n2)
    #J3
    eig_value3 = eig_val[resolution-3]
    MS3 = abs(1/(1+1j*eig_val[resolution-3])) #modal significance
    a_n3 = 180 - math.atan(eig_val[resolution-3])*180/pi
    eig_value_array3.append(eig_value3)
    MS_array3.append(MS3)
    a_n_array3.append(a_n3)
    #J4
    eig_value4 = eig_val[resolution-4]
    MS4 = abs(1/(1+1j*eig_val[resolution-4])) #modal significance
    a_n4 = 180 - math.atan(eig_val[resolution-4])*180/pi
    eig_value_array4.append(eig_value4)
    MS_array4.append(MS4)
    a_n_array4.append(a_n4)



    print('Eigen Value of J1 = %f ' %eig_value1)
    print('Modal Significance of J1 = %f ' %MS1)
    print('Characteristic Angle of J1 = %f ' %a_n1)

eig_value_array1 = np.reshape(eig_value_array1,(np.size(eig_value_array1),1))
eig_value_array2 = np.reshape(eig_value_array2,(np.size(eig_value_array2),1))
eig_value_array3 = np.reshape(eig_value_array3,(np.size(eig_value_array3),1))
eig_value_array4 = np.reshape(eig_value_array4,(np.size(eig_value_array4),1))
freq_array = freq_array/1e6

pyplot.figure(2)
pyplot.title('hw 4 prob 1; frequency = 280MHz; N = 101')
pyplot.xlabel('Frequency in MHz')
pyplot.ylabel('Eigen Value')

pyplot.plot(freq_array, eig_value_array1, color = 'red')
pyplot.plot(freq_array, eig_value_array2, color = 'red')
pyplot.plot(freq_array, eig_value_array3, color = 'red')
pyplot.plot(freq_array, eig_value_array4, color = 'red')

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

# z_feed = v[mid]/I[mid]
# print(z_feed)
#
# pyplot.figure(1)
# pyplot.plot(len, I_mag, color="magenta")
# pyplot.show()