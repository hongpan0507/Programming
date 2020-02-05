# DSP first lab 6 part 3 Filtering a Stair-Step Signal
# 08/05/2017

import numpy as np
from numpy import cos, exp, abs, angle   # function
from numpy import pi    # constant
import matplotlib.pyplot as plt
import scipy.io
from scipy import signal

plt_n = 0   # for plotting figure increment only

# ------------------ check frequency response ------------------------
ww_start = -pi
ww_end = pi
ww_step_size = 100
ww_step = (ww_end-ww_start)/ww_step_size
ww = np.arange(ww_start, ww_end, ww_step)  # arrange(start, stop, step); exclusive of ending

# 3.1 (a)
b1 = [1, -1]    # first difference
b2 = np.ones(5)
b2 = 1/np.size(b2) * b2     # 5-point averager

W1, H1 = signal.freqz(b1, 1, ww)    # frequency response
W2, H2 = signal.freqz(b2, 1, ww)    # frequency response

H1_mag = np.abs(H1)   # linear scale
H1_phase = np.angle(H1, deg=True)   # angle in degree
H2_mag = np.abs(H2)   # linear scale
H2_phase = np.angle(H2, deg=True)   # angle in degree

plt_n += 1
fig = plt.figure(plt_n, figsize=(20, 12), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle("frequency response")

ax1 = plt.subplot(221)
ax1.set_xlim(ww_start, ww_end)
ax1.set_ylim(0, max(H2_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax1.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax1.set_ylabel('|H|')
ax1.plot(W2, H2_mag, 'r--')
ax1.set_title('5-point average magnitude response')

ax2 = plt.subplot(222)
ax2.set_xlim(ww_start, ww_end)
ax2.set_ylim(-180, 180)
ax2.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax2.set_ylabel('angle(H) in deg')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position('right')
ax2.plot(W2, H2_phase, 'b--')
ax2.set_title('5-point average phase response')

ax3 = plt.subplot(223)
ax3.set_xlim(ww_start, ww_end)
ax3.set_ylim(0, max(H1_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax3.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax3.set_ylabel('|H|')
ax3.plot(W2, H1_mag, 'r--')
ax3.set_title('first difference magnitude response')

ax4 = plt.subplot(224)
ax4.set_xlim(ww_start, ww_end)
ax4.set_ylim(-180, 180)
ax4.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax4.set_ylabel('angle(H) in deg')
ax4.yaxis.tick_right()
ax4.yaxis.set_label_position('right')
ax4.plot(W1, H1_phase, 'b--')
ax4.set_title('first difference phase response')

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.3, wspace=0)

# --------------- process signal ------------------------------
# 3.2 5-point averager
mat = scipy.io.loadmat('files\LAB6DAT.MAT')     # load matlab file

print("Available keys in mat file:")
print(mat.keys())   # print all the avaiable keys from mat file; dict_keys(['h2', 'xtv', 'x2', 'h1', 'x1'])
# print(mat['x1'])    # access stored data with a key

v1 = signal.convolve(b2, mat['x1'][0])  # convolution with 5-point averager

n_x1 = np.arange(0, np.size(mat['x1']), 1)     # sample "time scale"
n_v1 = np.arange(0, np.size(v1), 1)     # sample "time scale"

# print(n)
# print(mat['x1'][0])
plt_n += 1
fig = plt.figure(plt_n, figsize=(12, 12), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle("Filter stair step signal by 5-point averager")

ax1 = plt.subplot(211)
ax1.set_xlim(0, np.size(n_x1))
ax1.set_ylim(np.min(mat['x1']), np.max(mat['x1']))
ax1.set_xlabel('n')
ax1.set_ylabel('Amplitude')
ax1.plot(n_x1, mat['x1'][0], 'r-')
ax1.set_title('original signal')

ax2 = plt.subplot(212)
ax2.set_xlim(0, np.size(n_v1))
ax2.set_ylim(np.min(v1), np.max(v1))
ax2.set_xlabel('n')
ax2.set_ylabel('Amplitude')
ax2.plot(n_v1, v1, 'b-')
ax2.set_title('Filtered Signal')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.3, wspace=0)

# 3.3 first difference
v2 = signal.convolve(b1, mat['x1'][0])
n_v2 = np.arange(0, np.size(v2), 1)     # sample "time scale"

plt_n += 1
fig = plt.figure(plt_n, figsize=(12, 12), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle("Filter stair step signal by first difference")

ax1 = plt.subplot(211)
ax1.set_xlim(0, np.size(n_x1))
ax1.set_ylim(np.min(mat['x1']), np.max(mat['x1']))
ax1.set_xlabel('n')
ax1.set_ylabel('Amplitude')
ax1.plot(n_x1, mat['x1'][0], 'r-')
ax1.set_title('original signal')

ax2 = plt.subplot(212)
ax2.set_xlim(0, np.size(n_v1))
ax2.set_ylim(np.min(v2), np.max(v2))
ax2.set_xlabel('n')
ax2.set_ylabel('Amplitude')
ax2.plot(n_v2, v2, 'b-')
ax2.set_title('Filtered Signal')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.3, wspace=0)

# 3.4 cascade two systems; 5-point averager->first difference
v_temp = signal.convolve(b2, mat['x1'][0])
y1 = signal.convolve(b1, v_temp)
n_v3 = np.arange(0, np.size(y1), 1)     # sample "time scale"

# 3.5 cascade two systems; first difference->5-point averager
v_temp = signal.convolve(b1, mat['x1'][0])
y2 = signal.convolve(b2, v_temp)
n_v4 = np.arange(0, np.size(y2), 1)     # sample "time scale"

plt_n += 1
fig = plt.figure(plt_n, figsize=(12, 20), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle("Filter stair step signal")

ax1 = plt.subplot(311)
ax1.set_xlim(0, np.size(n_x1))
ax1.set_ylim(np.min(mat['x1']), np.max(mat['x1']))
ax1.set_xlabel('n')
ax1.set_ylabel('Amplitude')
ax1.plot(n_x1, mat['x1'][0], 'r-')
ax1.set_title('original signal')

ax2 = plt.subplot(312)
ax2.set_xlim(0, np.size(n_v3))
ax2.set_ylim(np.min(y1), np.max(y1))
ax2.set_xlabel('n')
ax2.set_ylabel('Amplitude')
ax2.plot(n_v3, y1, 'b-')
ax2.set_title('Filtered Signal (5-point averager then first difference)')

ax3 = plt.subplot(313)
ax3.set_xlim(0, np.size(n_v4))
ax3.set_ylim(np.min(y2), np.max(y2))
ax3.set_xlabel('n')
ax3.set_ylabel('Amplitude')
ax3.plot(n_v4, y2, 'b-')
ax3.set_title('Filtered Signal (first difference then 5-point averager)')

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.3, wspace=0)

plt.show()

y_error = np.multiply(y1-y2, y1-y2)
y_error_sum = np.sum(y_error)   # in theory, there is no difference, but in real implementation, minute error exists

print(y_error_sum)
