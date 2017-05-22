# DSP first lab 5 part 3, cascading two systems
# 05/18/2017

import numpy as np
from numpy import cos, exp, abs, angle   # function
from numpy import pi    # constant
from scipy import signal
import matplotlib.pyplot as plt
plt_n = 0   # for plotting figure increment only


# ----------------------------------------------------------
# 3.5
A = 7
phi = pi/3
ww = 0.125*pi
L = 50
n = np.arange(0, L)     # arange is exclusive, default step = 1
x_n = A*cos(ww*n+phi)   # x[n]
w_n = x_n**2
# w2_n = 49/2*cos(2*pi*1/8*n+2*pi/3) + 49/2 # for verification only

h = [1, -1]   # first order difference filter
filt_L = len(h)
n_filt = np.arange(0, L+filt_L-1)     # arange is exclusive, default step = 1
y_n = signal.convolve(w_n, h, mode='full')

h2 = [1, -2*cos(1/4*pi), 1]
filt_L2 = len(h2)
n_filt2 = np.arange(0, L+filt_L2-1)     # arange is exclusive, default step = 1
y2_n = signal.convolve(w_n, h2, mode='full')

plt_n += 1
fig = plt.figure(plt_n, figsize=(12, 18), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle('cascading two systems', fontsize=15)

ax1 = plt.subplot(311)
# ax1.set_xlim(0, (L-1)*ww)
# ax1.set_ylim(0, max(H2_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax1.set_xlabel('n')
ax1.set_ylabel('x[n]')
ax1.plot(n, x_n, 'r-', label='x[n]')
ax1.set_title('n vs x[n]')
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

ax2 = plt.subplot(312)
# ax1.set_xlim(0, (L-1)*ww)
# ax1.set_ylim(0, max(H2_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax2.set_xlabel('n')
ax2.set_ylabel('w[n]')
ax2.plot(n, w_n, 'r-', label='w[n]')
# ax2.plot(n, w2_n, 'b--', label='w2[n]')
ax2.set_title('n vs w[n], w[n]=(x[n]^2)')
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

ax3 = plt.subplot(313)
# ax1.set_xlim(0, (L-1)*ww)
# ax1.set_ylim(0, max(H2_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax3.set_xlabel('n')
ax3.set_ylabel('y[n]')
ax3.plot(n_filt, y_n, 'r-', label='y[n]')
ax3.set_title('n vs y[n], y[n]=h*(x[n]^2)')
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.1, hspace=0.3, wspace=0)
# plt.show()
# ----------------------------------------------------------
plt_n += 1
fig = plt.figure(plt_n, figsize=(12, 18), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle('cascading two systems', fontsize=15)

ax1 = plt.subplot(311)
# ax1.set_xlim(0, (L-1)*ww)
# ax1.set_ylim(0, max(H2_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax1.set_xlabel('n')
ax1.set_ylabel('x[n]')
ax1.plot(n, x_n, 'b-', label='x[n]')
ax1.set_title('n vs x[n]')
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

ax2 = plt.subplot(312)
# ax1.set_xlim(0, (L-1)*ww)
# ax1.set_ylim(0, max(H2_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax2.set_xlabel('n')
ax2.set_ylabel('w[n]')
ax2.plot(n, w_n, 'b-', label='w[n]')
ax2.set_title('n vs w[n], w[n]=(x[n]^2)')
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

ax3 = plt.subplot(313)
# ax1.set_xlim(0, (L-1)*ww)
# ax1.set_ylim(0, max(H2_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax3.set_xlabel('n')
ax3.set_ylabel('y2[n]')
ax3.plot(n_filt2, y2_n, 'b-', label='y2[n]')
ax3.set_title('n vs y[n], y2[n]=h2*(x[n]^2)')
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.1, hspace=0.3, wspace=0)
plt.show()
