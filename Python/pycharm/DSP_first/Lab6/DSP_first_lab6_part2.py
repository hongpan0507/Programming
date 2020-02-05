# DSP first lab 6 part 2
# 08/05/2017

import numpy as np
from numpy import cos, exp, abs, angle   # function
from numpy import pi    # constant
import matplotlib.pyplot as plt
import scipy.io
from scipy import signal

plt_n = 0   # for plotting figure increment only

mat = scipy.io.loadmat('files\LAB6DAT.MAT')     # load matlab file

print("Available keys in mat file:")
print(mat.keys())   # print all the avaiable keys from mat file; dict_keys(['h2', 'xtv', 'x2', 'h1', 'x1'])
# print(mat['x1'])    # access stored data with a key

# 2.1 (b) polynomial multiplication
p1 = [0, 1, 1/2, -2]    # 1st polynomial
p2 = [1, 1, 0, -1/4]    # 2nd polynomial

p3 = signal.convolve(p1, p2)    # convolve = polynomial multiplication = digital filtering
print("Polynomial Multiplication: ")
print(p3)   # check result against hand calculation

# 2.1 (c) frequency response of two cascaded system
FIR1 = [1/3, 1/3, 1/3, 0, 0]      # 3-point average filter
FIR2 = [1/5, 1/5, 1/5, 1/5, 1/5]      # 5-point average filter

FIR3 = signal.convolve(FIR1, FIR2)  # cascade two systems
print("Cascaded FIR filter: ")
print(FIR3)

ww_start = -3*pi    # extend the normalized frequency range beyond -pi to verify the periodicity of frequency response
ww_end = 3*pi   # extend the normalized frequency range beyond +pi to verify the periodicity of frequency response
ww_sample_size = 400
ww_step = (ww_end-ww_start)/ww_sample_size
ww = np.arange(ww_start, ww_end, ww_step)  # arange(start, stop, step); exclusive of ending

W, H = signal.freqz(FIR3, 1, ww) # (numerator, denominator, frequency range)

H_mag = np.abs(H)   # linear scale
H_phase = np.angle(H, deg=True)   # angle in degree

fig = plt.figure(plt_n, figsize=(12, 12), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle("Cascaded FIR filter frequency response")

ax1 = plt.subplot(211)
ax1.set_xlim(ww_start, ww_end)
ax1.set_ylim(0, max(H_mag))
# ax1.set_xticks(np.arange(ww_start, ww_end, plt_ww_tick))
ax1.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax1.set_ylabel('|H|')
ax1.plot(W, H_mag, 'r--')
ax1.set_title('magnitude response')

ax2 = plt.subplot(212)
ax2.set_xlim(ww_start, ww_end)
ax2.set_ylim(-180, 180)
ax2.set_xlabel('normalized frequency (2*pi*f0/fs)')
ax2.set_ylabel('angle(H) in deg')
ax2.plot(W, H_phase, 'b--')
ax2.set_title('phase response')

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.3, wspace=0)

plt.show()
