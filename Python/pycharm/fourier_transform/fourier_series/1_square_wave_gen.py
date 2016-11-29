# generate one period of square wave

from math import pi
import numpy as np
from matplotlib import pyplot as plt

# square wave properties
A = 1   # upper amplitude
B = 0   # Lower amplitude
T = 2    # period
t_step = 1000     # number of points in square wave function
t = np.linspace(0, 2, t_step)    # time increments for one period


def square_wave_func(t):     # Generate square wave
    if t < T/2:
        return A
    else:
        return B

sw = [square_wave_func(i) for i in t]

# print(sw)

n = 0
fig = plt.figure(n, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
ax0 = plt.subplot(111)
ax0.plot(t, sw, 'b-', label='Square Wave')
ax0.axis([-1.5*T, 1.5*T, B*1.5, A*1.5])     # [xmin, xmax, ymin, ymax]
plt.xlabel('t')
plt.ylabel('Amplitude')
# plt.title(' ')
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plt.savefig('plotting/square_wave', dpi=100, facecolor='w', edgecolor='k')

plt.show()

