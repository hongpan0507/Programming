__author__ = 'hpan'


import numpy as np
import matplotlib.pyplot as pyplot
from scipy.integrate import quad

import cmath
import math
from math import sin
from math import cos
from mpl_toolkits.mplot3d.axes3d import Axes3D
#---------------------Constants-------------------------
pi = math.pi
mu_0 = 4*pi*1e-7    #permeability
epsilon_0 = 1e-9/(36*pi)    #permitivity
eta = 120*pi    #intrinsic impedance
dB_Np = 20/math.log(10,math.exp(1))     # 8.68 db per Np
#-----------------------------------------------------------
# hw 2 problem 1 part 2:
# hw 2 problem 1.a:

##--------------------------first section: (0,0,L/4) to (0,L/8,L/4)--------------------------------------
def A_theta_real_sect_1(primed,theta, phi):  
    complex = cmath.exp(1j*2*pi*(primed*sin(theta)*sin(phi)+1/8*cos(theta)))    # y' changes, but z'=1/8
    A_theta_r = cos(theta)*sin(phi)*sin(2*pi*(abs(primed))) * complex.real
    return A_theta_r

def A_theta_img_sect_1(primed,theta, phi):  
    complex = cmath.exp(1j*2*pi*(primed*sin(theta)*sin(phi)+1/8*cos(theta)))    # y' changes, but z'=1/8
    A_theta_i = cos(theta)*sin(phi)*sin(2*pi*(abs(primed))) * complex.imag
    return A_theta_i

def A_phi_real_sect_1(primed,theta, phi):  
    complex = cmath.exp(1j*2*pi*(primed*sin(theta)*sin(phi)+1/8*cos(theta)))    # y' changes, but z'=1/8
    A_phi_r = cos(phi)*sin(2*pi*(abs(primed))) * complex.real
    return A_phi_r

def A_phi_img_sect_1(primed,theta, phi):  
    complex = cmath.exp(1j*2*pi*(primed*sin(theta)*sin(phi)+1/8*cos(theta)))    # y' changes, but z'=1/8
    A_phi_i = cos(phi)*sin(2*pi*(abs(primed))) * complex.imag
    return A_phi_i
##-------------------------------------------------------------------------------------------------------

##--------------------------second section: (0,0,L/4) to (0,L/8,L/4)--------------------------------------
def A_theta_real_sect_2(primed,theta, phi):   
    complex = cmath.exp(1j*2*pi*(primed*cos(theta)+1/16*sin(theta)*sin(phi)))    # z' changes, but y'=1/16
    A_theta_r = -1*sin(theta) * sin(2*pi*(3/16-abs(primed))) * complex.real
    return A_theta_r

def A_theta_img_sect_2(primed,theta, phi):   
    complex = cmath.exp(1j*2*pi*(primed*cos(theta)+1/16*sin(theta)*sin(phi)))    # z' changes, but y'=1/16
    A_theta_i = -1*sin(theta) * sin(2*pi*(3/16-abs(primed))) * complex.imag
    return A_theta_i

# no A_phi component because J_z is the only current
##------------------------------------------------------------------------------------------------------

##--------------------------third section: (0,0,L/8) to (0,L/8,L/8)--------------------------------------
def A_theta_real_sect_3(primed,theta, phi):    
    complex = cmath.exp(1j*2*pi*(primed*sin(theta)*sin(phi)+1/16*cos(theta)))    # y' changes, but z'=1/16
    A_theta_r = cos(theta)*sin(phi)*sin(2*pi*(3/16-abs(primed))) * complex.real
    return A_theta_r

def A_theta_img_sect_3(primed,theta, phi):    
    complex = cmath.exp(1j*2*pi*(primed*sin(theta)*sin(phi)+1/16*cos(theta)))    # y' changes, but z'=1/16
    A_theta_i = cos(theta)*sin(phi)*sin(2*pi*(3/16-abs(primed))) * complex.imag
    return A_theta_i

def A_phi_real_sect_3(primed,theta, phi):    
    complex = cmath.exp(1j*2*pi*(primed*sin(theta)*sin(phi)+1/16*cos(theta)))    # y' changes, but z'=1/16
    A_phi_r = cos(phi)*sin(2*pi*(3/16-abs(primed))) * complex.real
    return A_phi_r

def A_phi_img_sect_3(primed,theta, phi):    
    complex = cmath.exp(1j*2*pi*(primed*sin(theta)*sin(phi)+1/16*cos(theta)))    # y' changes, but z'=1/16
    A_phi_i = cos(phi)*sin(2*pi*(3/16-abs(primed))) * complex.imag
    return A_phi_i
##-------------------------------------------------------------------------------------------------------

##--------------------------fourth section: (0,0,L/8) to (0,0,-L/4)--------------------------------------
def A_theta_real_sect_4(primed,theta, phi):    
    complex = cmath.exp(1j*2*pi*(primed*cos(theta)))    # only z' changes
    A_theta_r = -1*sin(theta) * sin(2*pi*(1/4-abs(primed))) * complex.real
    return A_theta_r

def A_theta_img_sect_4(primed,theta, phi):    
    complex = cmath.exp(1j*2*pi*(primed*cos(theta)))    # only z' changes
    A_theta_i = -1*sin(theta) * sin(2*pi*(1/4-abs(primed))) * complex.imag
    return A_theta_i

# no A_phi component because J_z is the only current
##------------------------------------------------------------------------------------------------------

##--------------------------fifth section: (0,0,-L/4) to (L/4,0,-L/4)--------------------------------------
def A_theta_real_sect_5(primed,theta, phi):    
    complex = cmath.exp(1j*2*pi*(primed*sin(theta)*cos(phi)-1/8*cos(theta)))    # x' changes, but z'= -1/8
    A_theta_r = cos(theta)*cos(phi)*sin(2*pi*(1/8-abs(primed))) * complex.real
    return A_theta_r

def A_theta_img_sect_5(primed,theta, phi):     
    complex = cmath.exp(1j*2*pi*(primed*sin(theta)*cos(phi)-1/8*cos(theta)))    # x' changes, but z'= -1/8
    A_theta_i = cos(theta)*cos(phi)*sin(2*pi*(1/8-abs(primed))) * complex.imag
    return A_theta_i

def A_phi_real_sect_5(primed,theta, phi):     
    complex = cmath.exp(1j*2*pi*(primed*sin(theta)*cos(phi)-1/8*cos(theta)))    # x' changes, but z'= -1/8
    A_phi_r = -1*sin(phi)*sin(2*pi*(1/8-abs(primed))) * complex.real
    return A_phi_r

def A_phi_img_sect_5(primed,theta, phi):     
    complex = cmath.exp(1j*2*pi*(primed*sin(theta)*cos(phi)-1/8*cos(theta)))    # x' changes, but z'= -1/8
    A_phi_i = -1*sin(phi)*sin(2*pi*(1/8-abs(primed))) * complex.imag
    return A_phi_i
##-------------------------------------------------------------------------------------------------------

def mag(A_theta_r, A_theta_i):
    return math.sqrt(pow(A_theta_r,2)+pow(A_theta_i,2))

I_m = 1
resolution = 100
theta_array = np.linspace(0, 2*pi, resolution)  #theta = 2*pi for plot; to calculate radiation impedance, use theta = pi
phi_array = np.linspace(0, 2*pi, resolution)

##--------------------------first section: (0,0,L/4) to (0,L/8,L/4)--------------------------------------
A_theta_r_sect_1 = np.zeros([resolution,resolution])
A_theta_r_size = np.shape(A_theta_r_sect_1)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_theta_r_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_theta_r_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_theta_r_buff = quad(A_theta_real_sect_1, 0, 1/16, args=(theta_temp,phi_temp))
        A_theta_r_sect_1[i,j] = A_theta_r_buff[0]

A_theta_i_sect_1 = np.zeros([resolution,resolution])
A_theta_i_size = np.shape(A_theta_i_sect_1)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_theta_i_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_theta_i_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_theta_i_buff = quad(A_theta_img_sect_1, 0, 1/16, args=(theta_temp,phi_temp))
        A_theta_i_sect_1[i,j] = A_theta_i_buff[0]

A_phi_r_sect_1 = np.zeros([resolution,resolution])
A_phi_r_size = np.shape(A_phi_r_sect_1)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_phi_r_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_phi_r_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_phi_r_buff = quad(A_phi_real_sect_1, 0, 1/16, args=(theta_temp,phi_temp))
        A_phi_r_sect_1[i,j] = A_phi_r_buff[0]

A_phi_i_sect_1 = np.zeros([resolution,resolution])
A_phi_i_size = np.shape(A_phi_i_sect_1)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_phi_i_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_phi_i_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_phi_i_buff = quad(A_phi_img_sect_1, 0, 1/16, args=(theta_temp,phi_temp))
        A_phi_i_sect_1[i,j] = A_phi_i_buff[0]
##-------------------------------------------------------------------------------------------------------

##--------------------------second section: (0,0,L/4) to (0,L/8,L/4)--------------------------------------
A_theta_r_sect_2 = np.zeros([resolution,resolution])
A_theta_r_size = np.shape(A_theta_r_sect_2)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_theta_r_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_theta_r_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_theta_r_buff = quad(A_theta_real_sect_2, 2/16, 1/16, args=(theta_temp,phi_temp))
        A_theta_r_sect_2[i,j] = A_theta_r_buff[0]

A_theta_i_sect_2 = np.zeros([resolution,resolution])
A_theta_i_size = np.shape(A_theta_i_sect_2)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_theta_i_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_theta_i_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_theta_i_buff = quad(A_theta_img_sect_2, 2/16, 1/16, args=(theta_temp,phi_temp))
        A_theta_i_sect_2[i,j] = A_theta_i_buff[0]

## no A_phi term
##-------------------------------------------------------------------------------------------------------

##--------------------------third section: (0,0,L/8) to (0,L/8,L/8)--------------------------------------
A_theta_r_sect_3 = np.zeros([resolution,resolution])
A_theta_r_size = np.shape(A_theta_r_sect_3)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_theta_r_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_theta_r_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_theta_r_buff = quad(A_theta_real_sect_3, 1/16, 0, args=(theta_temp,phi_temp))
        A_theta_r_sect_3[i,j] = A_theta_r_buff[0]

A_theta_i_sect_3 = np.zeros([resolution,resolution])
A_theta_i_size = np.shape(A_theta_i_sect_3)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_theta_i_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_theta_i_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_theta_i_buff = quad(A_theta_img_sect_3, 1/16, 0, args=(theta_temp,phi_temp))
        A_theta_i_sect_3[i,j] = A_theta_i_buff[0]

A_phi_r_sect_3 = np.zeros([resolution,resolution])
A_phi_r_size = np.shape(A_phi_r_sect_3)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_phi_r_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_phi_r_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_phi_r_buff = quad(A_phi_real_sect_3, 1/16, 0, args=(theta_temp,phi_temp))
        A_phi_r_sect_3[i,j] = A_phi_r_buff[0]

A_phi_i_sect_3 = np.zeros([resolution,resolution])
A_phi_i_size = np.shape(A_phi_i_sect_3)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_phi_i_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_phi_i_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_phi_i_buff = quad(A_phi_img_sect_3, 1/16, 0, args=(theta_temp,phi_temp))
        A_phi_i_sect_3[i,j] = A_phi_i_buff[0]
##-------------------------------------------------------------------------------------------------------

##--------------------------fourth section: (0,0,L/8) to (0,0,-L/4)--------------------------------------
A_theta_r_sect_4 = np.zeros([resolution,resolution])
A_theta_r_size = np.shape(A_theta_r_sect_4)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_theta_r_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_theta_r_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_theta_r_buff = quad(A_theta_real_sect_4, 1/16, -1/8, args=(theta_temp,phi_temp))
        A_theta_r_sect_4[i,j] = A_theta_r_buff[0]

A_theta_i_sect_4 = np.zeros([resolution,resolution])
A_theta_i_size = np.shape(A_theta_i_sect_4)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_theta_i_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_theta_i_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_theta_i_buff = quad(A_theta_img_sect_4, 1/16, -1/8, args=(theta_temp,phi_temp))
        A_theta_i_sect_4[i,j] = A_theta_i_buff[0]

## no A_phi term
##-------------------------------------------------------------------------------------------------------

##--------------------------fifth section: (0,0,-L/4) to (L/4,0,-L/4)--------------------------------------
A_theta_r_sect_5 = np.zeros([resolution,resolution])
A_theta_r_size = np.shape(A_theta_r_sect_5)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_theta_r_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_theta_r_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_theta_r_buff = quad(A_theta_real_sect_5, 0, 1/8, args=(theta_temp,phi_temp))
        A_theta_r_sect_5[i,j] = A_theta_r_buff[0]

A_theta_i_sect_5 = np.zeros([resolution,resolution])
A_theta_i_size = np.shape(A_theta_i_sect_5)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_theta_i_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_theta_i_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_theta_i_buff = quad(A_theta_img_sect_5, 0, 1/8, args=(theta_temp,phi_temp))
        A_theta_i_sect_5[i,j] = A_theta_i_buff[0]

A_phi_r_sect_5 = np.zeros([resolution,resolution])
A_phi_r_size = np.shape(A_phi_r_sect_5)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_phi_r_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_phi_r_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_phi_r_buff = quad(A_phi_real_sect_5, 0, 1/8, args=(theta_temp,phi_temp))
        A_phi_r_sect_5[i,j] = A_phi_r_buff[0]

A_phi_i_sect_5 = np.zeros([resolution,resolution])
A_phi_i_size = np.shape(A_phi_i_sect_5)    #get the size of a 2d array; row_size = [0]; column_size = [1]

for i in range(0, A_phi_i_size[0]):   #row size; phi from 0 to 2*pi
    for j in range(0, A_phi_i_size[1]):   #column size: theta from 0 to pi
        theta_temp = theta_array[j]
        phi_temp = phi_array[i]
        A_phi_i_buff = quad(A_phi_img_sect_5, 0, 1/8, args=(theta_temp,phi_temp))
        A_phi_i_sect_5[i,j] = A_phi_i_buff[0]
##-------------------------------------------------------------------------------------------------------

##------------combine all the contribution from each section at every combination of (theta, phi)---------
##------------then turn into power density term, and find the max------------------------------------------
A_theta_r = np.zeros([resolution,resolution])
A_theta_i = np.zeros([resolution,resolution])
A_phi_r = np.zeros([resolution,resolution])
A_phi_i = np.zeros([resolution,resolution])

for i in range(0, resolution):   #row size; phi from 0 to 2*pi
    for j in range(0, resolution):   #column size: theta from 0 to pi
        A_theta_r[i,j] = A_theta_r_sect_1[i,j] + A_theta_r_sect_2[i,j] + A_theta_r_sect_3[i,j] + A_theta_r_sect_4[i,j] + A_theta_r_sect_5[i,j]
        A_theta_i[i,j] = A_theta_i_sect_1[i,j] + A_theta_i_sect_2[i,j] + A_theta_i_sect_3[i,j] + A_theta_i_sect_4[i,j] + A_theta_i_sect_5[i,j]
        A_phi_r[i,j] = A_phi_r_sect_1[i,j] + A_phi_r_sect_3[i,j] + A_phi_r_sect_5[i,j]
        A_phi_i[i,j] = A_phi_i_sect_1[i,j] + A_phi_i_sect_3[i,j] + A_phi_i_sect_5[i,j]

theta_norm_factor = 0
A_theta_m = np.zeros([resolution,resolution])
for i in range(0, resolution):   #row size; phi from 0 to 2*pi
    for j in range(0, resolution):   #column size: theta from 0 to pi
        A_theta_m[i,j] = mag(A_theta_r[i,j], A_theta_i[i,j])
        A_theta_m[i,j] = pow(A_theta_m[i,j],2)
        if theta_norm_factor < A_theta_m[i,j]:  #Finding max and use it to normalize
            theta_norm_factor = A_theta_m[i,j]

phi_norm_factor = 0
A_phi_m = np.zeros([resolution,resolution])
for i in range(0, resolution):   #row size; phi from 0 to 2*pi
    for j in range(0, resolution):   #column size: theta from 0 to pi
        A_phi_m[i,j] = mag(A_phi_r[i,j], A_phi_i[i,j])
        A_phi_m[i,j] = pow(A_phi_m[i,j],2)
        if phi_norm_factor < A_phi_m[i,j]:  #Finding max and use it to normalize
            phi_norm_factor = A_phi_m[i,j]
##-------------------------------------------------------------------------------------------------------

##---------------normalize and turn to log scale-------------------------------------------------------------------------------
if phi_norm_factor >= theta_norm_factor:
    norm_factor = phi_norm_factor
else:
    norm_factor = theta_norm_factor

for i in range(0, resolution):   #row size; phi from 0 to 2*pi
    for j in range(0, resolution):   #column size: theta from 0 to pi
        A_theta_m[i,j] = A_theta_m[i,j]/norm_factor
        A_phi_m[i,j] = A_phi_m[i,j]/norm_factor
        A_theta_m[i,j] = 10*math.log10(A_theta_m[i,j])
        A_phi_m[i,j] = 10*math.log10(A_phi_m[i,j])

##-------------------------------------------------------------------------------------------------------

pyplot.figure(1)
ax = pyplot.subplot(111, polar=True)
ax.set_theta_zero_location('N')
ax.set_theta_direction('clockwise')
#ax = pyplot.subplot(311, polar=True)
ax.plot(theta_array, A_theta_m[24,:], color='r', linewidth=2)
ax.set_yticks(np.array([-20, -12, -6, 0]))
ax.set_xticks(np.array([0, -45, -90, -135, 180, 135, 90, 45])/180*pi)
ax.set_title('hw 2 prob 1 part 2; E_theta at Y-Z plane')

pyplot.figure(2)
ax = pyplot.subplot(111, polar=True)
ax.set_theta_zero_location('N')
ax.set_theta_direction('clockwise')
#ax = pyplot.subplot(312, polar=True)
ax.plot(theta_array, A_theta_m[0,:], color='r', linewidth=2)
ax.set_yticks(np.array([-20, -12, -6, 0]))
ax.set_xticks(np.array([0, -45, -90, -135, 180, 135, 90, 45])/180*pi)
ax.set_title('hw 2 prob 1 part 2; E_theta at X-Z plane')

pyplot.figure(3)
ax = pyplot.subplot(111, polar=True)
ax.set_theta_zero_location('N')
ax.set_theta_direction('clockwise')
#ax = pyplot.subplot(313, polar=True)
ax.plot(phi_array, A_theta_m[:,24], color='r', linewidth=2)
ax.set_yticks(np.array([-20, -12, -6, 0]))
ax.set_xticks(np.array([0, -45, -90, -135, 180, 135, 90, 45])/180*pi)
ax.set_title('hw 2 prob 1 part 2; E_theta at X-Y plane')

pyplot.figure(4)
ax = pyplot.subplot(111, polar=True)
ax.set_theta_zero_location('N')
ax.set_theta_direction('clockwise')
#ax = pyplot.subplot(311, polar=True)
ax.plot(theta_array, A_phi_m[24,:], color='r', linewidth=2)
ax.set_yticks(np.array([-20, -12, -6, 0]))
ax.set_xticks(np.array([0, -45, -90, -135, 180, 135, 90, 45])/180*pi)
ax.set_title('hw 2 prob 1 part 2; E_phi at Y-Z plane')

pyplot.figure(5)
ax = pyplot.subplot(111, polar=True)
ax.set_theta_zero_location('N')
ax.set_theta_direction('clockwise')
#ax = pyplot.subplot(312, polar=True)
ax.plot(theta_array, A_phi_m[0,:], color='r', linewidth=2)
ax.set_yticks(np.array([-20, -12, -6, 0]))
ax.set_xticks(np.array([0, -45, -90, 135, -180, 135, 90, 45])/180*pi)
ax.set_title('hw 2 prob 1 part 2; E_phi at X-Z plane')

pyplot.figure(6)
ax = pyplot.subplot(111, polar=True)
ax.set_theta_zero_location('N')
ax.set_theta_direction('clockwise')
#ax = pyplot.subplot(313, polar=True)
ax.plot(phi_array, A_phi_m[:,24], color='r', linewidth=2)
ax.set_yticks(np.array([-20, -12, -6, 0]))
ax.set_xticks(np.array([0, -45, -90, -135, 180, 135, 90, 45])/180*pi)
ax.set_title('hw 2 prob 1 part 2; E_phi at X-Y plane')

pyplot.show()