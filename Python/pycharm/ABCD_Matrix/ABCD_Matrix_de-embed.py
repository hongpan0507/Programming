import skrf as rf
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)


# ---------------------User Input--------------------------------
# Frequency Range
freq_lower = 1e9
freq_upper = 10e9

# plot attributes
freq_step = 1e9
plt_ylim = [-30, 0]     # y axis limit: 0 to -20dB
plt_ytick = np.arange(-30, 5, 5)
plt_xlim = [freq_lower, freq_upper]
plt_xtick = np.arange(freq_lower, freq_upper+freq_step, freq_step)
plt_title_s_para = 'De-embedded S-Parameter 1; ' + str(int(freq_lower/1e9)) + '-' + str(int(freq_upper/1e9)) + 'Ghz'
plt_title2 = '; CTRL=Low; Port 1 = RF2(RX); Port 2 = RFC(ANT)'
plt_title_s_para = plt_title_s_para + plt_title2
plt_title_smith = 'De-embedded Smith Chart 1; ' + str(int(freq_lower/1e9)) + '-' + str(int(freq_upper/1e9)) + 'Ghz'
plt_title_smith = plt_title_smith + plt_title2
# -----------------------------------------------------------------

# reading file
# TouchStone File Path = Current directory + file name
LFCN_6400_TS_file = os.getcwd() + "\\S Parameter\\Minicircuits_LFCN-6400+_1-10Ghz.s2p"
LFCN_6400_network = rf.Network(LFCN_6400_TS_file)   # open touch stone file

ADS_combined_TS_file = os.getcwd() + "\\S Parameter\\ADS_combined_test_file.s2p"
ADS_combined_network = rf.Network(ADS_combined_TS_file)   # open touch stone file

# change network parameter
LFCN_6400_network.crop(freq_lower, freq_upper, "Hz")   # only use data from 1-6Ghz
LFCN_6400_network.frequency.unit = 'GHz'

ADS_combined_network.crop(freq_lower, freq_upper, "Hz")   # only use data from 1-6Ghz
ADS_combined_network.frequency.unit = 'GHz'

DeEmbedded_network = rf.de_embed(LFCN_6400_network, ADS_combined_network)   # remove LFCN_6400 from combined network

# write to a file in TouchStone Format
DeEmbedded_network.write_touchstone('Python_de-embedded_test_file', os.getcwd() + "\\S Parameter\\")

print()
# # plot data
# fig1, ax1 = plt.subplots(1)
# LFCN_6400_network.plot_s_db(m=0, n=0, label='OU s11', color='r')     # zero indexing; 0 refers to port 1
# LFCN_6400_network.plot_s_db(m=1, n=0, label='OU s21', color='b')     # zero indexing; 0 refers to port 1
# LFCN_6400_network.plot_s_db(m=0, n=1, label='OU s12', color='g')     # zero indexing; 0 refers to port 1
# LFCN_6400_network.plot_s_db(m=1, n=1, label='OU s22', color='y')     # zero indexing; 0 refers to port 1
#
# ADS_combined_network.plot_s_db(m=2, n=2, label='pSemi s11', color='r', linestyle='--')     # zero indexing; 0 refers to port 1
# ADS_combined_network.plot_s_db(m=0, n=2, label='pSemi s21', color='b', linestyle='--')     # zero indexing; 0 refers to port 1
# ADS_combined_network.plot_s_db(m=2, n=0, label='pSemi s12', color='g', linestyle='--')     # zero indexing; 0 refers to port 1
# ADS_combined_network.plot_s_db(m=0, n=0, label='pSemi s22', color='y', linestyle='--')     # zero indexing; 0 refers to port 1
#
# ax1.set_ylim(plt_ylim)
# ax1.yaxis.set_ticks(plt_ytick)
# ax1.set_xlim(plt_xlim)
# ax1.xaxis.set_ticks(plt_xtick)
# ax1.yaxis.set_minor_locator(AutoMinorLocator())      # show minor tick
# ax1.xaxis.set_minor_locator(AutoMinorLocator())      # show minor tick
# ax1.grid(True, which='major', linestyle='-')
# ax1.grid(True, which='minor', linestyle=':')
# ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))  # loc='legend box ref position'
# ax1.set_title(plt_title_s_para)
# fig1.set_size_inches(12, 6)
# plt.subplots_adjust(left=0.1, right=0.8)
# plt.savefig(fname=plt_title_s_para, dpi=300, bbox_inches='tight')
#
# fig1, ax1 = plt.subplots(1)
# LFCN_6400_network.plot_s_smith(m=0, n=0, label='OU s11', color='r')
# LFCN_6400_network.plot_s_smith(m=1, n=1, label='OU s22', color='y')
#
# ADS_combined_network.plot_s_smith(m=2, n=2, label='pSemi s11', color='r', linestyle='--')     # zero indexing; 0 refers to port 1
# ADS_combined_network.plot_s_smith(m=0, n=0, label='pSemi s22', color='y', linestyle='--')     # zero indexing; 0 refers to port 1
#
# ax1.set_title(plt_title_smith)
# ax1.legend(loc='upper left', bbox_to_anchor=(0.9, 0.9))  # loc='legend box ref position'
# fig1.set_size_inches(6, 6)
# plt.savefig(fname=plt_title_smith, dpi=300, bbox_inches='tight')
#
# plt.show()
