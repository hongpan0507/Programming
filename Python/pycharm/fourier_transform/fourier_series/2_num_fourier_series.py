# numerical fourier series computation

# generate one period of square wave

from math import pi
import numpy as np
import cmath
from matplotlib import pyplot as plt

# square wave properties
A = 1   # upper amplitude
B = 0   # Lower amplitude
T = 2    # period
t_step = 1000     # number of points in square wave function
del_T = T/(t_step-1)
t = np.linspace(0, 2, t_step)    # time increments for one period
print("del T: " + str(del_T))
# print("t array:\n" + str(t))

def square_wave_func(t):     # Generate square wave
    if t < T/2:
        return A
    else:
        return B

sw = [square_wave_func(i) for i in t]
# print("sw:\n" + str(sw))
# print(sw)
#


c0 = 1/T*np.sum(sw)*del_T
print("c0: " + str(c0))

num_co = 50     # number of coefficient
cp = np.zeros(num_co, dtype=complex)   # integer coefficient from 1 to positive infinity
cn = np.zeros(num_co, dtype=complex)   # integer coefficient from negative infinity to -1

for n in range(1, num_co+1):
    for i in range(0, t_step):
        f_exp_p = cmath.exp(-1j*2*pi*n*t[i]/T)  # fourier series positive exponential
        cp[n-1] += 1/T*sw[i]*f_exp_p*del_T      # numerical sum as integration
        f_exp_n = cmath.exp(1j * 2 * pi * n * t[i] / T)  # fourier series negative exponential
        cn[n-1] += 1 / T * sw[i] * f_exp_n * del_T  # numerical sum as integration

print("cp:\n"+str(cp))
print("cn:\n"+str(cn))

y = np.zeros(t_step)    # time increments for one period
for i in range(0, t_step):
    g_1 = 0
    g_2 = 0
    for n in range(1, num_co+1):
        g_1 += cp[n-1]*cmath.exp(1j*2*pi*n*t[i]/T)      # use positive coefficient
        g_2 += cn[n - 1] * cmath.exp(1j * 2 * pi * -1*n * t[i] / T)  # use negative coefficient
    y[i] = c0+np.abs(g_1+g_2)

# print("y[]:\n" + str(y))

n = 0
fig = plt.figure(n, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
ax0 = plt.subplot(111)
ax0.plot(t, y, 'b-', label='Square Wave')
ax0.axis([-1.5*T, 1.5*T, B*1.5, A*1.5])     # [xmin, xmax, ymin, ymax]
plt.xlabel('t')
plt.ylabel('Amplitude')
# plt.title(' ')
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plt.savefig('plotting/square_wave', dpi=100, facecolor='w', edgecolor='k')

plt.show()