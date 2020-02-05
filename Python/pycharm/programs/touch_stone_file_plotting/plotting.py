import skrf as rf
import numpy as np
import os
from matplotlib import pyplot as plt

# TouchStone file path = Current working directory + file name
TS_file = os.getcwd() + "\\MicroTech Inc Rotary Joint (243073) S parameter.s2p"
RJ = rf.Network(TS_file)    # open touch stone file

freq = RJ.f/1e9                # extract frequency and convert to GHz
# [[[s11, s12], [s21, s22]],
#  [[s11, s12], [s21, s22]],
#  [[s11, s12], [s21, s22]]]
s11 = RJ.s[:, 0, 0]         # extract S11
s12 = RJ.s[:, 0, 1]         # extract S12
s21 = RJ.s[:, 1, 0]         # extract S21
s22 = RJ.s[:, 1, 1]         # extract S22

vswr11 = RJ.s_vswr[:, 0, 0]

fig, ax = plt.subplots(2, 1)
fig.suptitle('Bugdar Rotary Joint')
ax[0].plot(freq, 20*np.log10(np.abs(s11)), label='s11')
ax[0].set_title("S Parameter")
ax[0].plot(freq, 20*np.log10(np.abs(s12)), label='s12')
ax[0].plot(freq, 20*np.log10(np.abs(s21)), label='s21')
ax[0].plot(freq, 20*np.log10(np.abs(s22)), label='s22')
ax[0].set_xlabel('Freq (GHz)')
ax[0].set_ylabel('Mag (dB)')
ax[0].set_xlim([np.min(freq), np.max(freq)])
ax[0].set_ylim([-40, 0])
ax[0].legend()    # make label visible in the plot
ax[0].grid(True)

ax[1].set_title("VSWR")
ax[1].plot(freq, vswr11, label='vswr11')
ax[1].set_xlabel('Freq (GHz)')
ax[1].set_xlim([np.min(freq), np.max(freq)])
ax[1].set_ylim([1, 3])
ax[1].legend()    # make label visible in the plot
ax[1].grid(True)
fig.tight_layout(pad=1.5)

plt.show()
