# DSP first lab 5 part 1, FIR filter frequency response
# 05/18/2017

import numpy as np
from numpy import cos, exp, abs, angle   # function
from numpy import pi    # constant
import matplotlib.pyplot as plt
plt_n = 0   # for plotting figure increment only

# ----------------------------------------------------------
# implement (9) found by hand calculation
ww_start = -pi
ww_end = pi
ww_sample_size = 400
ww_step = (ww_end-ww_start)/ww_sample_size
ww = np.arange(ww_start, ww_end, ww_step)  # arange(start, stop, step); exclusive of ending
plt_ww_tick = (ww_end-ww_start)/10  # for plotting only

H = 1/3*exp(-1j*ww)*(1+2*cos(ww))   # 3-point average FIR filter frequency response based on hand calculation
H_mag = abs(H)  # magnitude
H_phase = angle(H)*180/pi   # angle in degree

# plotting
plt_n += 1
fig = plt.figure(plt_n, figsize=(12, 12), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle('3-point averager frequency response, hand calculation', fontsize=15)

ax1 = plt.subplot(211)
ax1.set_xlim(ww_start, ww_end)
ax1.set_ylim(0, max(H_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax1.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax1.set_ylabel('|H|')
ax1.plot(ww, H_mag, 'r-')
ax1.set_title('magnitude response')

ax2 = plt.subplot(212)
ax2.set_xlim(ww_start, ww_end)
ax2.set_ylim(-180, 180)
ax2.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax2.set_ylabel('angle(H) in deg')
ax2.plot(ww, H_phase, 'b-')
ax2.set_title('phase response')

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.3, wspace=0)
# plt.show()
# ----------------------------------------------------------

# ----------------------------------------------------------
# computer frequency calculation using (1)
from scipy import signal

ww_start = -pi
ww_end = pi
ww_sample_size = 400
ww_step = (ww_end-ww_start)/ww_sample_size
ww = np.arange(ww_start, ww_end, ww_step)  # arange(start, stop, step); exclusive of ending

# bb = 1/3*np.ones(3)    # FIR filter coefficient
# bb = [1, -1]
bb = [1, -2*cos(1/4*pi), 1]
W2, H2 = signal.freqz(bb, 1, ww)  # (numerator, denominator, frequency range)
H2_mag = abs(H2)  # magnitude
H2_phase = angle(H2)*180/pi   # angle in degree

plt_n += 1
fig = plt.figure(plt_n, figsize=(12, 12), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle('3-point averager frequency response, computer calculation', fontsize=15)

ax1 = plt.subplot(211)
ax1.set_xlim(ww_start, ww_end)
ax1.set_ylim(0, max(H2_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax1.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax1.set_ylabel('|H|')
ax1.plot(W2, H2_mag, 'r--')
ax1.set_title('magnitude response')

ax2 = plt.subplot(212)
ax2.set_xlim(ww_start, ww_end)
ax2.set_ylim(-180, 180)
ax2.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax2.set_ylabel('angle(H) in deg')
ax2.plot(W2, H2_phase, 'b--')
ax2.set_title('phase response')

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.3, wspace=0)

plt.show()
