# Program Function:
#   plots the s parameter data

import csv
from matplotlib import pyplot as plot
from matplotlib import cm   # color map
from cycler import cycler
import numpy as np

# ***************************** Simulated Data *****************************
# *************************************************************************

# ***************************** Measured Data *****************************
file2 = open('RL_Test_1_t0v.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state0 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('RL_Test_1_t2v.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state2 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('RL_Test_1_t4v_wo_gating.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state4 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('RL_Test_1_t5v_wo_gating.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state5 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('RL_Test_1_t6v_wo_gating.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state6 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('RL_Test_1_t7v_wo_gating.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state7 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
# *************************************************************************

# extract information from csv and store in the following lists for plotting and processing
freq = []
measured_s11_mag_state0 = []
measured_s11_mag_state2 = []
measured_s11_mag_state4 = []
measured_s11_mag_state5 = []
measured_s11_mag_state6 = []
measured_s11_mag_state7 = []

# ***************************** Simulated Data *****************************
# *************************************************************************

# ***************************** Measured Data *****************************
for row in measured_csv_s11_mag_state0:   # row contains the row data
    if measured_csv_s11_mag_state0.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        freq.append(row[0])
        measured_s11_mag_state0.append(20*np.log10(np.sqrt(float(row[1])**2+float(row[2])**2)))

for row in measured_csv_s11_mag_state2:   # row contains the row data
    if measured_csv_s11_mag_state2.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_s11_mag_state2.append(20*np.log10(np.sqrt(float(row[1])**2+float(row[2])**2)))

for row in measured_csv_s11_mag_state4:   # row contains the row data
    if measured_csv_s11_mag_state4.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_s11_mag_state4.append(20*np.log10(np.sqrt(float(row[1])**2+float(row[2])**2)))

for row in measured_csv_s11_mag_state5:   # row contains the row data
    if measured_csv_s11_mag_state5.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_s11_mag_state5.append(20*np.log10(np.sqrt(float(row[1])**2+float(row[2])**2)))

for row in measured_csv_s11_mag_state6:   # row contains the row data
    if measured_csv_s11_mag_state6.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_s11_mag_state6.append(20*np.log10(np.sqrt(float(row[1])**2+float(row[2])**2)))

for row in measured_csv_s11_mag_state7:   # row contains the row data
    if measured_csv_s11_mag_state7.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_s11_mag_state7.append(20*np.log10(np.sqrt(float(row[1])**2+float(row[2])**2)))
# *************************************************************************

# ***************************** plotting **********************************
constant_0dB = np.linspace(0, 0, len(freq))     # constant 0dB reference line

plot.figure(1)
# plot.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y', 'c', 'm'])))
ax0 = plot.subplot(111)
ax0.plot(freq, constant_0dB, 'k--', label="0dB reference")
ax0.plot(freq, measured_s11_mag_state0, '-', label="|s11| state 0; w. gating")
ax0.plot(freq, measured_s11_mag_state2, '-', label="|s11| state 2; w. gating")
ax0.plot(freq, measured_s11_mag_state4, '-', label="|s11| state 4")
ax0.plot(freq, measured_s11_mag_state5, '-', label="|s11| state 5")
ax0.plot(freq, measured_s11_mag_state6, '-', label="|s11| state 6")
ax0.plot(freq, measured_s11_mag_state7, '-', label="|s11| state 7")
ax0.axis([1e9, 5e9, -50, 5])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('|S11| (dB)')
plot.title('Measured |S11|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)
# plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner

plot.show()
# *************************************************************************

file2.close()
