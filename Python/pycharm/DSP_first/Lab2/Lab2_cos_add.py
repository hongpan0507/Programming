# python 3.5
# 02/25/2017
# lab 2

import numpy as np
from mod_cursor import *
from matplotlib import pyplot
from numpy import cos, pi
from cmath import exp

# 3 cycle
# included negative time to compare phase at t=0
t_start = -1/15
t_stop = 2/15
sample_size = 40
t_step = (1/15)/sample_size  # Period/sample size
t = np.arange(t_start, t_stop, t_step)

amp = 5     # amplitude
freq = 15   # Hz

phi1 = 0.5*pi       # phase
phi2 = -0.25*pi     # phase
phi3 = 0.4*pi       # phase
phi4 = -0.9*pi      # phase

# cosine function with the same frequency but different phase shift
x1_t = amp*cos(2*pi*freq*t + phi1)
x2_t = amp*cos(2*pi*freq*t + phi2)
x3_t = amp*cos(2*pi*freq*t + phi3)
x4_t = amp*cos(2*pi*freq*t + phi4)
x5_t = x1_t + x2_t + x3_t + x4_t

# complex version of the cosine signal
z1 = amp * exp(1j * phi1)
z2 = amp * exp(1j * phi2)
z3 = amp * exp(1j * phi3)
z4 = amp * exp(1j * phi4)
z5 = z1+z2+z3+z4
z = np.array([z1, z2, z3, z4, z5])
# print(z)

n = 0
fig = pyplot.figure(n, figsize=(9, 9), dpi=80, facecolor='w', edgecolor='k')
ax0 = pyplot.subplot(111)
for x in range(len(z)):
    ax0.plot([0, z[x].real], [0, z[x].imag], 'o-', label='z'+str(x+1))
ax0.axis([-amp, amp, -amp, amp])     # [xmin, xmax, ymin, ymax]
pyplot.legend()

n += 1
fig = pyplot.figure(n, figsize=(9, 12), dpi=80, facecolor='w', edgecolor='k')

ax0 = pyplot.subplot(511)
ax0.set_title('x'+r'$_1$'+'(t)', fontsize=14)
ax0.plot(t, x1_t, 'r-', label='x1(t)')
ax0.set_xlabel('t (S)', fontsize=14)
ax0.set_ylabel('Amplitude', fontsize=14)
ax0.axis([t_start, t_stop, -amp, amp])     # [xmin, xmax, ymin, ymax]
ax0.axhline(y=0, color='k')
ax0.axvline(x=0, color='k')
ax0.grid()

ax1 = pyplot.subplot(512)
ax1.set_title('x'+r'$_2$'+'(t)', fontsize=14)
ax1.plot(t, x2_t, 'r-', label='x2(t)')
ax1.set_xlabel('t (S)', fontsize=14)
ax1.set_ylabel('Amplitude', fontsize=14)
ax1.axis([t_start, t_stop, -amp, amp])     # [xmin, xmax, ymin, ymax]
ax1.axhline(y=0, color='k')
ax1.axvline(x=0, color='k')
ax1.grid()

ax2 = pyplot.subplot(513)
ax2.set_title('x'+r'$_3$'+'(t)', fontsize=14)
ax2.plot(t, x3_t, 'r-', label='x3(t)')
ax2.set_xlabel('t (S)', fontsize=14)
ax2.set_ylabel('Amplitude', fontsize=14)
ax2.axis([t_start, t_stop, -amp, amp])     # [xmin, xmax, ymin, ymax]
ax2.axhline(y=0, color='k')
ax2.axvline(x=0, color='k')
ax2.grid()

ax3 = pyplot.subplot(514)
ax3.set_title('x'+r'$_4$'+'(t)', fontsize=14)
ax3.plot(t, x4_t, 'r-', label='x4(t)')
ax3.set_xlabel('t (S)', fontsize=14)
ax3.set_ylabel('Amplitude', fontsize=14)
ax3.axis([t_start, t_stop, -amp, amp])     # [xmin, xmax, ymin, ymax]
ax3.axhline(y=0, color='k')
ax3.axvline(x=0, color='k')
ax3.grid()

ax4 = pyplot.subplot(515)
ax4.set_title('x'+r'$_5$'+'(t)', fontsize=14)
ax4.plot(t, x5_t, 'r-', label='x5(t)')
ax4.set_xlabel('t (S)', fontsize=14)
ax4.set_ylabel('Amplitude', fontsize=14)
ax4.axis([t_start, t_stop, -amp, amp])     # [xmin, xmax, ymin, ymax]
ax4.axhline(y=0, color='k')
ax4.axvline(x=0, color='k')
ax4.grid()

fig.subplots_adjust(hspace=.5)
pyplot.show()
