# DSP First lab 7 part 1: DTMF Synthesis

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, cos
from scipy import signal


ww_start = -pi
ww_end = pi
ww_step_size = 100
ww_step = (ww_end-ww_start)/ww_step_size
ww = np.arange(ww_start, ww_end, ww_step)  # arrange(start, stop, step); exclusive of ending

w_not = 0.5*pi  # normalized notch filter frequency
b1 = [1, -2*cos(w_not), 1]   # notch filter coefficient
W1, H1 = signal.freqz(b1, 1, ww)

H1_mag = np.abs(H1)   # linear scale
H1_phase = np.angle(H1, deg=True)   # angle in degree

plt_n = 0
plt_n += 1
fig = plt.figure(plt_n, figsize=(12, 12), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle("frequency response")

ax3 = plt.subplot(211)
ax3.set_xlim(ww_start, ww_end)
ax3.set_ylim(0, max(H1_mag)+0.1)
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax3.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax3.set_ylabel('|H|')
ax3.plot(W1, H1_mag, 'r--')
ax3.set_title('h1 magnitude response')

ax4 = plt.subplot(212)
ax4.set_xlim(ww_start, ww_end)
ax4.set_ylim(-180, 180)
ax4.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax4.set_ylabel('angle(H) in deg')
ax4.yaxis.tick_right()
ax4.yaxis.set_label_position('right')
ax4.plot(W1, H1_phase, 'b--')
ax4.set_title('h1 phase response')

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.3, wspace=0)

plt.show()
