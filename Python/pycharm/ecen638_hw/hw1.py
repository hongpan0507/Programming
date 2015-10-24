__author__ = 'hpan'
#availabe colors: b:blue; g:green; r:red; c:cyan; m:magenta; y:yellow; k:black; w:white

import numpy as np
import matplotlib.pyplot as pyplot
import math

pi = math.pi
mu_0 = 4*pi*1e-7    #permeability
epsilon_0 = 1e-9/(36*pi)    #permitivity
eta = 120*pi    #intrinsic impedance
dB_Np = 20/math.log(10,math.exp(1))     # 8.68 db per Np

# hw 1 problem 1.a: free space path loss
freq = 2.45e9
c = 3e8
wave_len = c/freq

#free space path loss functions; return loss in dB scale
def FSPL_func(d, wave_len):
    temp1 = 4*math.pi*d/wave_len
    FSPL = math.pow(temp1,2)
    FSPL_dB = 10*math.log10(FSPL)
    return FSPL_dB

resolution = 10000
d = np.linspace(1e3, 1e7, resolution)

FSPL_dB_array = np.zeros(resolution)    # to create mutli-dimensional array = np.zeros((x,y))
nor_factor = FSPL_func(d[0],wave_len)
i = 0
while i < np.size(d):
    FSPL_dB_array[i] = FSPL_func(d[i],wave_len)
    FSPL_dB_array[i] = FSPL_dB_array[i] - nor_factor  # normalize
    i += 1

pyplot.figure(1)
pyplot.title('hw 1 prob 1 a to f')
pyplot.xscale('log')
pyplot.xlabel('distance in m')
pyplot.ylim(0, 200)
pyplot.ylabel('Attenuation dB/m')
pyplot.plot(d, FSPL_dB_array, color="yellow")   # plot(x-axis, y-axis)

# hw 1 problem 1.b: LMR-400 attenuation @ 2.45GHz = 22dB/100m
# online calculator: http://www.timesmicrowave.com/calculator/?productId=52#form
# formula available on the datasheet
atten_dB = 22/100
LMR_400_dB_array = np.zeros(resolution)
nor_factor = atten_dB * d[0]
i = 0
while i < np.size(d):
    LMR_400_dB_array[i] = atten_dB * d[i]
    LMR_400_dB_array[i] = LMR_400_dB_array[i] - nor_factor     #normalize
    i += 1

#pyplot.figure(2)
#pyplot.title('hw 1 prob 1 b to e')
#pyplot.xscale('log')
#pyplot.xlabel('distance in m')
#pyplot.ylabel('Attenuation dB/m')
pyplot.plot(d, LMR_400_dB_array, color="blue")

# hw 1 problem 1.c: Attenuation of circular wave guide = dielectric loss + conductor loss
# formula at Polzar book: conductor loss page 125; dielectric loss page 102
# Fundamental mode = TE11 Polzar book page 127 figure 3.13
#freq = 14e9
r = 0.044   #radius
E_r = 1     #dielectric constant; assume air filled
p11 = 1.841     #Polzar book page 123 table 3.3
cond = 3.816e7    #Polzar book page 719
loss_tan = 0    #air loss tangent
wave_num = 2*pi*freq*math.sqrt(E_r)/3e8
prop_const = math.sqrt(pow(wave_num,2) - (p11/r)*(p11/r))
die_a_dB = pow(wave_num,2)*loss_tan/(2*prop_const)*dB_Np     #dielectric loss
R_surf = math.sqrt(2*pi*freq*mu_0/(2*cond))      #surface resistance
k_c = p11 / r
cond_a_dB = R_surf/(r*wave_num*eta/math.sqrt(E_r)*prop_const)*(pow(k_c,2)+pow(wave_num,2)/(pow(p11,2)-1)) * dB_Np  #conductor loss
atten_dB =  cond_a_dB + die_a_dB

atten_dB_array = np.zeros(resolution)
nor_factor = atten_dB * d[0]
i = 0
while i < np.size(d):
    atten_dB_array[i] = atten_dB * d[i]
    atten_dB_array[i] = atten_dB_array[i] - nor_factor  #normalize
    i += 1

pyplot.plot(d, atten_dB_array, color="red")

# hw 1 problem 1.d: Attenuation of WR-340 (aluminum) wave guide = dielectric loss + conductor loss
# WR-340 wave guide = 86.36 by 43.18 in mm
# Polzar Book: conductor loss page 115; dielectric loss page 117
# fundamental mode = TE10 mode; page 116, figure 3.8
cond = 3.816e7    #Polzar book page 719
a = 86.36 * 1e-3
b = 43.18 * 1e-3
m = 1
n = 0
#freq = 15 * 1e9
E_r = 1 #assume air filled
loss_tan = 0 # assume air-filled
w = 2 * pi * freq
k = w * math.sqrt(E_r*epsilon_0*mu_0)
k_c = math.sqrt(pow(m*pi/a,2)+pow(n*pi/b,2))
prop_const = math.sqrt(pow(k,2)-pow(k_c,2))
prop_const_temp = prop_const        # for problem 3
die_a_dB = pow(k,2)*loss_tan/(2*prop_const)*dB_Np     #dielectric loss
R_surf = math.sqrt(2*pi*freq*mu_0/(2*cond))      #surface resistance
cond_a_dB = R_surf/(pow(a,3)*b*prop_const*k*eta/math.sqrt(E_r))*(2*b*pow(pi,2)+pow(a,3)*pow(k,2)) * dB_Np # conductor loss

atten_dB =  cond_a_dB + die_a_dB

atten_dB_array = np.zeros(resolution)
nor_factor = atten_dB * d[0]
i = 0
while i < np.size(d):
    atten_dB_array[i] = atten_dB * d[i]
    atten_dB_array[i] = atten_dB_array[i] - nor_factor    #normalize
    i += 1

pyplot.plot(d, atten_dB_array, color="black")

# hw 1 problem 1.e:
atten_dB = 0.35e-3

atten_dB_array = np.zeros(resolution)
nor_factor = atten_dB * d[0]
i = 0
while i < np.size(d):
    atten_dB_array[i] = atten_dB * d[i]
    atten_dB_array[i] = atten_dB_array[i] - nor_factor    #normalize
    i += 1

pyplot.plot(d, atten_dB_array, color="green")

# hw 1 problem 1.f:
# Polzar Book: conductor loss page 143; dielectric loss page 102
Z_0 = 50
t = 0.01e-3     #conductor thickness

#b = 1e-3   #seperation of ground planes
b = 0.32e-2   #seperation of ground planes###########
cond = 5.813e7  #conductivity
c = 3e8
freq = 10e9
E_r = 2.2
k = 2 * pi * freq * math.sqrt(E_r) / c
#loss_tan = 0.0009
loss_tan = 0.001
die_a_dB = k*loss_tan/2 * dB_Np      #dielectric loss
R_surf = math.sqrt(2*pi*freq*mu_0/(2*cond))      #surface resistance

x = 30*pi/(math.sqrt(E_r)*Z_0)-0.441

if (Z_0*math.sqrt(E_r) < 120):
    w = b * x
else:
    w = b * (0.85-math.sqrt(0.6-x))

A = 1 + 2*w/(b-t) + 1/pi*(b+t)/(b-t)*math.log((2*b-t)/t)     #log() = ln() in python
B = 1 + b/(0.5*w+0.7*t) * (0.5 + 0.414*t/w + 1/(2*pi)*math.log(4*pi*w/t))

if (Z_0*math.sqrt(E_r) < 120):
    cond_a_dB = 2.7e-3*R_surf*E_r*Z_0/(30*pi*(b-t))*A
else:
    cond_a_dB = 0.16*R_surf/(Z_0*b) * B

print('x = %f' % x)
print('w = %f' % w)
print('A = %f' % A)
print('R_surf = %f' % R_surf)
print('E_r = %f' % E_r)
print('Z_0 = %f' % Z_0)
print('w = %f' % w)
print('t = %f' % t)
print('cond_db = %f' % cond_a_dB)

atten_dB = die_a_dB + cond_a_dB

atten_dB_array = np.zeros(resolution)
nor_factor = atten_dB * d[0]
i = 0
while i < np.size(d):
    atten_dB_array[i] = atten_dB * d[i]
    atten_dB_array[i] = atten_dB_array[i] - nor_factor    #normalize
    i += 1

pyplot.plot(d, atten_dB_array, color="magenta")



# hw 1 problem 3:
freq = 2.45e9
v = 1/math.sqrt(mu_0*epsilon_0)     #air
v1 = v * 0.85   #lmr-400 from datasheet
v2 = 2*pi*freq/prop_const_temp  #waveguide

delay_array = np.zeros(resolution)
i = 0
while i < np.size(d):
    delay_array[i] = d[i]/v
    i += 1

pyplot.figure(3)
pyplot.title('hw 1 prob 3')
pyplot.xscale('log')
pyplot.xlabel('distance in m')
pyplot.ylabel('delay in S')
pyplot.plot(d, delay_array, color="green")

delay_array = np.zeros(resolution)
i = 0
while i < np.size(d):
    delay_array[i] = d[i]/v1
    i += 1

pyplot.plot(d, delay_array, color="blue")

delay_array = np.zeros(resolution)
i = 0
while i < np.size(d):
    delay_array[i] = d[i]/v2
    i += 1

pyplot.plot(d, delay_array, color="red")

# hw 1 problem 4:
# power density of hertzian dipole
# with far field approximation: formula found on page 421 of 322 book
I = 1
L = 0.1 #multiples of wavelength
resolution = 10000
dist = np.linspace(0.1, 100, resolution)  #multiples of wavelength

s_max_array = np.zeros(resolution)
i = 0
while i < np.size(d):
    s_max_array[i] = eta/8 * pow(I*L,2)*pow(1/dist[i],2)
    i += 1

fig4 = pyplot.figure(4)
pyplot.title('hw 1 prob 4')
pyplot.xscale('log')
pyplot.xlabel('distance in term of wave length')
pyplot.ylabel('Maximum Power Density (w/m^2)')
pyplot.plot(dist, s_max_array, color="green")

s_max_array = np.zeros(resolution, complex)
i = 0
while i < np.size(d):
    #s_max_RE = eta/8 * pow(I*L,2)*pow(1/dist[i],2)
    #s_max_IM = eta/8 * pow(I*L,2)*pow(1/dist[i],2)*pow(1/(2*pi*dist[i]),3) * 1j
    s_max_array[i] = eta/8 * pow(I*L,2)*pow(1/dist[i],2) * (1+ 1j* pow(1/(2*pi*dist[i]),3))
    #s_max_array[i] = s_max_RE+s_max_IM
    i += 1

print(s_max_array)
pyplot.plot(dist, s_max_array.__abs__(), color="red")
pyplot.show()
