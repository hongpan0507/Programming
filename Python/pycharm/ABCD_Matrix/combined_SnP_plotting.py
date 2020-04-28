import skrf as rf
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)


# ---------------------User Input--------------------------------
# Frequency Range
freq_lower = 1e9
freq_upper = 9e9

# plot attributes
freq_step = 1e9
plt_ylim = [-30, 0]     # y axis limit: 0 to -20dB
plt_ytick = np.arange(-30, 5, 5)
plt_xlim = [freq_lower, freq_upper]
plt_xtick = np.arange(freq_lower, freq_upper+freq_step, freq_step)
plt_title_s_para = 'ADS vs Python S-Parameter 1; ' + str(int(freq_lower/1e9)) + '-' + str(int(freq_upper/1e9)) + 'Ghz'
plt_title2 = ''
plt_title_s_para = plt_title_s_para + plt_title2
plt_title_smith = 'ADS vs Python Smith Chart 1; ' + str(int(freq_lower/1e9)) + '-' + str(int(freq_upper/1e9)) + 'Ghz'
plt_title_smith = plt_title_smith + plt_title2
# -----------------------------------------------------------------

# reading file
# TouchStone File Path = Current directory + file name
ADS_combined_TS_file = os.getcwd() + "\\S Parameter\\ADS_combined_test_file.s2p"
ADS_combined_network = rf.Network(ADS_combined_TS_file)   # open touch stone file

Python_combined_TS_file = os.getcwd() + "\\S Parameter\\Python_combined_test_file.s2p"
Python_combined_network = rf.Network(Python_combined_TS_file)   # open touch stone file

# change network parameter
ADS_combined_network.crop(freq_lower, freq_upper, "Hz")   # only use data from 1-6Ghz
ADS_combined_network.frequency.unit = 'GHz'

Python_combined_network.crop(freq_lower, freq_upper, "Hz")   # only use data from 1-6Ghz
Python_combined_network.frequency.unit = 'GHz'

# plot data
fig1, ax1 = plt.subplots(1)
# ADS_combined_network.plot_s_db(m=0, n=0, label='ADS s11', color='r')     # zero indexing; 0 refers to port 1
# ADS_combined_network.plot_s_db(m=1, n=0, label='ADS s21', color='b')     # zero indexing; 0 refers to port 1
# ADS_combined_network.plot_s_db(m=0, n=1, label='ADS s12', color='g')     # zero indexing; 0 refers to port 1
# ADS_combined_network.plot_s_db(m=1, n=1, label='ADS s22', color='y')     # zero indexing; 0 refers to port 1

Python_combined_network.plot_s_db(m=0, n=0, label='Python s11', color='r', linestyle='--')     # zero indexing; 0 refers to port 1
Python_combined_network.plot_s_db(m=1, n=0, label='Python s21', color='b', linestyle='--')     # zero indexing; 0 refers to port 1
Python_combined_network.plot_s_db(m=0, n=1, label='Python s12', color='g', linestyle='--')     # zero indexing; 0 refers to port 1
Python_combined_network.plot_s_db(m=1, n=1, label='Python s22', color='y', linestyle='--')     # zero indexing; 0 refers to port 1

ax1.set_ylim(plt_ylim)
ax1.yaxis.set_ticks(plt_ytick)
ax1.set_xlim(plt_xlim)
ax1.xaxis.set_ticks(plt_xtick)
ax1.yaxis.set_minor_locator(AutoMinorLocator())      # show minor tick
ax1.xaxis.set_minor_locator(AutoMinorLocator())      # show minor tick
ax1.grid(True, which='major', linestyle='-')
ax1.grid(True, which='minor', linestyle=':')
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))  # loc='legend box ref position'
ax1.set_title(plt_title_s_para)
fig1.set_size_inches(12, 6)
plt.subplots_adjust(left=0.1, right=0.8)
plt.savefig(fname=plt_title_s_para, dpi=300, bbox_inches='tight')

fig1, ax1 = plt.subplots(1)
ADS_combined_network.plot_s_smith(m=0, n=0, label='ADS s11', color='r')
ADS_combined_network.plot_s_smith(m=1, n=1, label='ADS s22', color='y')

Python_combined_network.plot_s_smith(m=0, n=0, label='Python s11', color='r', linestyle='--')     # zero indexing; 0 refers to port 1
Python_combined_network.plot_s_smith(m=1, n=1, label='Python s22', color='y', linestyle='--')     # zero indexing; 0 refers to port 1

ax1.set_title(plt_title_smith)
ax1.legend(loc='upper left', bbox_to_anchor=(0.9, 0.9))  # loc='legend box ref position'
fig1.set_size_inches(6, 6)
plt.savefig(fname=plt_title_smith, dpi=300, bbox_inches='tight')

plt.show()
