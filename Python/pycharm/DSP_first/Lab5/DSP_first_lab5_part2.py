# DSP first lab 5 part 2, linearity
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
x_n = A*cos(ww*n+phi)   # x[n]

b0 = 5
b1 = -5
h = np.ones(2)   # (11), first order difference filter
h[0] = b0*h[0]
h[1] = b1*h[1]
filt_L = len(h)
n_filt = np.arange(0, L+filt_L-1)     # arange is exclusive, default step = 1

y_n = signal.convolve(x_n, h, mode='full')

plt_n += 1
fig = plt.figure(plt_n, figsize=(12, 18), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle('convolution operation', fontsize=15)

ax1 = plt.subplot(311)
# ax1.set_xlim(0, (L-1)*ww)
# ax1.set_ylim(0, max(H2_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax1.set_xlabel('n')
ax1.set_ylabel('y[n]')
ax1.plot(n, x_n, 'r-', label='x[n]')
ax1.plot(n_filt, y_n, 'b-', label='y[n]')
ax1.set_title('x[n] vs y[n], 2*pi*f0/fs*n = 0.125*pi*n')
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

# ax2 = plt.subplot(212)
# # ax2.set_xlim(ww_start, ww_end)
# # ax2.set_ylim(-180, 180)
# ax1.set_xlabel('n+len(h)-1')
# ax1.set_ylabel('y[n]')
# ax2.plot(n_filt, y_n, 'b-')
# ax2.set_title('y[n], 2*pi*f0/fs*n = 0.125*pi*n')

# plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)
# plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.1, hspace=0.3, wspace=0)
# plt.show()
# ----------------------------------------------------------


# ----------------------------------------------------------
# 3.3 (a)->(g); linearity
xa_n = 2*x_n
ya_n = signal.convolve(xa_n, h, mode='full')

A = 8
ww = 0.25*pi
phi = 0
xb_n = A*cos(ww*n+phi)
yb_n = signal.convolve(xb_n, h, mode='full')

# run input to the filter first, then sum the output
sum_ya_yb_n = ya_n + yb_n

# sum input first, then run it through the filter
sum_xa_xb_n = xa_n+xb_n
yc_n = signal.convolve(sum_xa_xb_n, h, mode='full')


# plt_n += 1
# fig = plt.figure(plt_n, figsize=(12, 12), dpi=80, facecolor='w', edgecolor='k')
# fig.suptitle('convolution operation', fontsize=15)

ax2 = plt.subplot(312)
# ax1.set_xlim(0, (L-1)*ww)
# ax1.set_ylim(0, max(H2_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax2.set_xlabel('n')
ax2.set_ylabel('ya[n]')
ax2.plot(n, xa_n, 'r-', label='xa[n]')
ax2.plot(n_filt, ya_n, 'b-', label='ya[n]')
ax2.set_title('xa[n] vs ya[n], 2*pi*f0/fs*n = 0.125*pi*n')
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

ax3 = plt.subplot(313)
# ax1.set_xlim(0, (L-1)*ww)
# ax1.set_ylim(0, max(H2_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax3.set_xlabel('n')
ax3.set_ylabel('yb[n]')
ax3.plot(n, xb_n, 'r-', label='xb[n]')
ax3.plot(n_filt, yb_n, 'b-', label='yb[n]')
ax3.set_title('xb[n] vs yb[n], 2*pi*f0/fs*n = 0.25*pi*n')
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.1, hspace=0.3, wspace=0)
# plt.show()


plt_n += 1
fig = plt.figure(plt_n, figsize=(12, 12), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle('linearity', fontsize=15)

ax2 = plt.subplot(211)
# ax1.set_xlim(0, (L-1)*ww)
# ax1.set_ylim(0, max(H2_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax2.set_xlabel('n')
ax2.set_ylabel('ya[n]+yb[n]')
# ax2.plot(n, xa_n, 'r-', label='xa[n]')
ax2.plot(n_filt, sum_ya_yb_n, 'b-', label='ya[n]+yb[n]')
# ax2.set_title('xa[n] vs ya[n], 2*pi*f0/fs*n = 0.125*pi*n')
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

ax3 = plt.subplot(212)
# ax1.set_xlim(0, (L-1)*ww)
# ax1.set_ylim(0, max(H2_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax3.set_xlabel('n')
ax3.set_ylabel('yc[n]')
# ax3.plot(n, xb_n, 'r-', label='xb[n]')
ax3.plot(n_filt, yc_n, 'b-', label='yc[n]')
# ax3.set_title('xb[n] vs yb[n], 2*pi*f0/fs*n = 0.25*pi*n')
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.1, hspace=0.3, wspace=0)
plt.show()

