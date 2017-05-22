# DSP first lab 5 part 2, time-invariance
# 05/18/2017

import numpy as np
from numpy import cos, exp, abs, angle   # function
from numpy import pi    # constant
from scipy import signal
import matplotlib.pyplot as plt
plt_n = 0   # for plotting figure increment only


# ----------------------------------------------------------
# 3.2 (a)->(g)
A = 7
phi = pi/3
ww = 0.125*pi
L = 50
n = np.arange(0, L)     # arange is exclusive, default step = 1
x1_n = A*cos(ww*n+phi)   # x[n]

x2_n = A*cos(ww*(n-3)+phi)   # x[n]

b0 = 5
b1 = -5
h = np.ones(2)   # (11), first order difference filter
h[0] = b0*h[0]
h[1] = b1*h[1]
filt_L = len(h)
n_filt = np.arange(0, L+filt_L-1)     # arange is exclusive, default step = 1

y1_n = signal.convolve(x1_n, h, mode='full')    # input = original signal
y2_n = signal.convolve(x2_n, h, mode='full')    # input = original signal shifted by 3

plt_n += 1
fig = plt.figure(plt_n, figsize=(12, 12), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle('convolution operation', fontsize=15)

ax1 = plt.subplot(211)
# ax1.set_xlim(0, (L-1)*ww)
# ax1.set_ylim(0, max(H2_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax1.set_xlabel('n')
ax1.set_ylabel('y[n]')
ax1.plot(n_filt, y1_n, 'r-', label='y1[n]')
ax1.plot(n_filt, y2_n, 'b-', label='y2[n]')
ax1.set_title('y1[n] vs y2[n], (non-shifted input, non-shifted output)vs (shifted input, non-shifted output)')
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

ax2 = plt.subplot(212)
# ax1.set_xlim(0, (L-1)*ww)
# ax1.set_ylim(0, max(H2_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax2.set_xlabel('n')
ax2.set_ylabel('y[n]')
ax2.plot(n_filt+3, y1_n, 'r-', label='y1[n]')
ax2.plot(n_filt, y2_n, 'b-', label='y2[n]')
ax2.set_title('y1[n] vs y2[n], (non-shifted input, shifted output)vs (shifted input, non-shifted output)')
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.1, hspace=0.3, wspace=0)
plt.show()
# ----------------------------------------------------------


