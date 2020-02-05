# DSP first lab 6 part 3 Filtering a Stair-Step Signal
# 08/05/2017

import numpy as np
from numpy import cos, exp, abs, angle   # function
from numpy import pi    # constant
import matplotlib.pyplot as plt
import scipy.io
from scipy import signal
from scipy.io import wavfile
import sounddevice as sd

plt_n = 0   # for plotting figure increment only

# ------------------ check frequency response ------------------------
ww_start = -pi
ww_end = pi
ww_step_size = 100
ww_step = (ww_end-ww_start)/ww_step_size
ww = np.arange(ww_start, ww_end, ww_step)  # arrange(start, stop, step); exclusive of ending

# 3.7
mat = scipy.io.loadmat('files\LAB6DAT.MAT')     # load matlab file

print("Available keys in mat file:")
print(mat.keys())   # print all the avaiable keys from mat file; dict_keys(['h2', 'xtv', 'x2', 'h1', 'x1'])
# print(mat['x1'])    # access stored data with a key

h1 = mat['h1'][0]   # h1 = low pass
h2 = mat['h2'][0]   # h1 = high pass
W1, H1 = signal.freqz(h1, 1, ww)    # frequency response
W2, H2 = signal.freqz(h2, 1, ww)    # frequency response

H1_mag = np.abs(H1)   # linear scale
H1_phase = np.angle(H1, deg=True)   # angle in degree
H2_mag = np.abs(H2)   # linear scale
H2_phase = np.angle(H2, deg=True)   # angle in degree

plt_n += 1
fig = plt.figure(plt_n, figsize=(20, 12), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle("frequency response")

ax1 = plt.subplot(221)
ax1.set_xlim(ww_start, ww_end)
ax1.set_ylim(0, max(H2_mag)+0.1)
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax1.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax1.set_ylabel('|H|')
ax1.plot(W2, H2_mag, 'r--')
ax1.set_title('h2 magnitude response')

ax2 = plt.subplot(222)
ax2.set_xlim(ww_start, ww_end)
ax2.set_ylim(-180, 180)
ax2.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax2.set_ylabel('angle(H) in deg')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position('right')
ax2.plot(W2, H2_phase, 'b--')
ax2.set_title('h2 phase response')

ax3 = plt.subplot(223)
ax3.set_xlim(ww_start, ww_end)
ax3.set_ylim(0, max(H1_mag)+0.1)
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax3.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax3.set_ylabel('|H|')
ax3.plot(W1, H1_mag, 'r--')
ax3.set_title('h1 magnitude response')

ax4 = plt.subplot(224)
ax4.set_xlim(ww_start, ww_end)
ax4.set_ylim(-180, 180)
ax4.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax4.set_ylabel('angle(H) in deg')
ax4.yaxis.tick_right()
ax4.yaxis.set_label_position('right')
ax4.plot(W1, H1_phase, 'b--')
ax4.set_title('h1 phase response')

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.3, wspace=0)


# --------------- process signal ------------------------------

x2 = np.transpose(mat['x2'])[0]  # speech data sampled at 8000 samples/second
n_x2 = np.arange(0, np.size(x2), 1)     # sample "time scale"
fs = 8000   # sampling rate
sd.play(x2, fs, blocking=True)

y1 = signal.convolve(h1, x2)    # h1 = low pass
sd.play(y1, fs, blocking=True)
n_y1 = np.arange(0, np.size(y1), 1)     # sample "time scale"

y2 = signal.convolve(h2, x2)    # h1 = high pass
sd.play(y2, fs, blocking=True)
n_y2 = np.arange(0, np.size(y2), 1)     # sample "time scale"

y3 = np.add(y1, y2)
sd.play(y3, fs, blocking=True)
n_y3 = np.arange(0, np.size(y3), 1)     # sample "time scale"

h3 = np.add(h1, h2)
y4 = signal.convolve(h3, x2)    # h1 = high pass
sd.play(y4, fs, blocking=True)
n_y4 = np.arange(0, np.size(y4), 1)     # sample "time scale"

plt_n += 1
fig = plt.figure(plt_n, figsize=(12, 20), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle("Filter sound signal")

ax1 = plt.subplot(311)
ax1.set_xlim(0, np.size(n_x2))
ax1.set_ylim(np.min(x2), np.max(x2))
ax1.set_xlabel('n')
ax1.set_ylabel('Amplitude')
ax1.plot(n_x2, x2, 'r-')
ax1.set_title('original signal')

ax2 = plt.subplot(312)
ax2.set_xlim(0, np.size(n_y1))
ax2.set_ylim(np.min(y1), np.max(y1))
ax2.set_xlabel('n')
ax2.set_ylabel('Amplitude')
ax2.plot(n_y1, y1, 'r-')
ax2.set_title('Low pass filtered signal')

ax3 = plt.subplot(313)
ax3.set_xlim(0, np.size(n_y2))
ax3.set_ylim(np.min(y2), np.max(y2))
ax3.set_xlabel('n')
ax3.set_ylabel('Amplitude')
ax3.plot(n_y2, y2, 'r-')
ax3.set_title('High pass filtered signal original signal')

# scaled = np.int16(x2/np.max(np.abs(x2)) * 32767)    # scale output audio
# wavfile.write('test.wav', 8000, scaled)     # sample rate given by the problem

plt.show()
