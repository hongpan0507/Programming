# Program Function:
#   plots the s parameter data

import csv
from matplotlib import pyplot as plot
from matplotlib import cm   # color map
from cycler import cycler
import numpy as np

# ***************************** Simulated Data *****************************
file1 = open('RL_Dipole.csv', 'rb')  # open the file for reading
sim_csv_s11_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list
# file1 = open('simulated_state_0_s11.csv', 'rb')  # open the file for reading
# sim_csv_s11_mag_state0 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
# *************************************************************************

# ***************************** Measured Data *****************************
file2 = open('t0_wo_gating_trial2.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state0 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('t1_wo_gating.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state1 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('t2_wo_gating.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state2 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('t3_wo_gating.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state3 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('t4_wo_gating.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state4 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('t5_wo_gating_trial2.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state5 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('t6_wo_gating.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state6 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('t7_wo_gating.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state7 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
# *************************************************************************

# extract information from csv and store in the following lists for plotting and processing
freq = []

measured_s11_mag_state0 = []
measured_s11_mag_state1 = []
measured_s11_mag_state2 = []
measured_s11_mag_state3 = []
measured_s11_mag_state4 = []
measured_s11_mag_state5 = []
measured_s11_mag_state6 = []
measured_s11_mag_state7 = []

sim_s11_mag_state0 = []
sim_s11_mag_state1 = []
sim_s11_mag_state2 = []
sim_s11_mag_state3 = []
sim_s11_mag_state4 = []
sim_s11_mag_state5 = []
sim_s11_mag_state6 = []
sim_s11_mag_state7 = []

# ***************************** Simulated Data *****************************


for row in sim_csv_s11_mag:   # row contains the row data
    if sim_csv_s11_mag.line_num > 991:    # ignore the first line
        sim_s11_mag_state1.append(row[4])
        sim_s11_mag_state2.append(row[6])
        sim_s11_mag_state3.append(row[8])
        sim_s11_mag_state4.append(row[10])
        sim_s11_mag_state5.append(row[12])
        sim_s11_mag_state6.append(row[14])
        sim_s11_mag_state7.append(row[15])

print sim_s11_mag_state7
print len(sim_s11_mag_state7)

# for row in sim_csv_s11_mag_state0:   # row contains the row data
#     if sim_csv_s11_mag_state0.line_num > 1:    # ignore the first line
#         sim_s11_mag_state0.append(row[1])

# *************************************************************************

# ***************************** Measured Data *****************************
for row in measured_csv_s11_mag_state0:   # row contains the row data
    if measured_csv_s11_mag_state0.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        freq.append(row[0])
        measured_s11_mag_state0.append(20*np.log10(np.sqrt(float(row[1])**2+float(row[2])**2)))

for row in measured_csv_s11_mag_state1:   # row contains the row data
    if measured_csv_s11_mag_state1.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_s11_mag_state1.append(20*np.log10(np.sqrt(float(row[1])**2+float(row[2])**2)))

for row in measured_csv_s11_mag_state2:   # row contains the row data
    if measured_csv_s11_mag_state2.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_s11_mag_state2.append(20*np.log10(np.sqrt(float(row[1])**2+float(row[2])**2)))

for row in measured_csv_s11_mag_state3:   # row contains the row data
    if measured_csv_s11_mag_state3.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_s11_mag_state3.append(20*np.log10(np.sqrt(float(row[1])**2+float(row[2])**2)))

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

print measured_s11_mag_state1
print len(measured_s11_mag_state1)
# *************************************************************************

# ***************************** plotting **********************************
constant_0dB = np.linspace(0, 0, len(freq))     # constant 0dB reference line
n = 1

# plot.figure(n)
# # plot.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y', 'c', 'm'])))
# ax0 = plot.subplot(111)
# ax0.plot(freq, constant_0dB, 'k--', label="0dB reference")
# ax0.plot(freq, measured_s11_mag_state0, 'r-', label="measured |s11| state 0, trial 2")
# ax0.plot(freq, sim_s11_mag_state0, 'b--', label="simulated |s11| state 0")
# ax0.axis([1e9, 5e9, -50, 5])     # [xmin, xmax, ymin, ymax]
# plot.xlabel('Frequency (Hz)')
# plot.ylabel('|S11| (dB)')
# plot.title('Panel 2 Trial 5 measured |S11| vs simulated |S11|')
# plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
# plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
# plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
# plot.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y', 'c', 'm'])))
ax0 = plot.subplot(111)
ax0.plot(freq, constant_0dB, 'k--', label="0dB reference")
ax0.plot(freq, measured_s11_mag_state1, 'r-', label="measured |s11| state 1")
ax0.plot(freq, sim_s11_mag_state1, 'b--', label="simulated |s11| state 1")
ax0.axis([1e9, 5e9, -50, 5])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('|S11| (dB)')
plot.title('Panel 2 Trial 5 measured |S11| vs simulated |S11|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
# plot.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y', 'c', 'm'])))
ax0 = plot.subplot(111)
ax0.plot(freq, constant_0dB, 'k--', label="0dB reference")
ax0.plot(freq, measured_s11_mag_state2, 'r-', label="measured |s11| state 2")
ax0.plot(freq, sim_s11_mag_state2, 'b--', label="simulated |s11| state 2")
ax0.axis([1e9, 5e9, -50, 5])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('|S11| (dB)')
plot.title('Panel 2 Trial 5 measured |S11| vs simulated |S11|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
# plot.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y', 'c', 'm'])))
ax0 = plot.subplot(111)
ax0.plot(freq, constant_0dB, 'k--', label="0dB reference")
ax0.plot(freq, measured_s11_mag_state3, 'r-', label="measured |s11| state 3")
ax0.plot(freq, sim_s11_mag_state3, 'b--', label="simulated |s11| state 3")
ax0.axis([1e9, 5e9, -50, 5])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('|S11| (dB)')
plot.title('Panel 2 Trial 5 measured |S11| vs simulated |S11|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
# plot.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y', 'c', 'm'])))
ax0 = plot.subplot(111)
ax0.plot(freq, constant_0dB, 'k--', label="0dB reference")
ax0.plot(freq, measured_s11_mag_state4, 'r-', label="measured |s11| state 4")
ax0.plot(freq, sim_s11_mag_state4, 'b--', label="simulated |s11| state 4")
ax0.axis([1e9, 5e9, -50, 5])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('|S11| (dB)')
plot.title('Panel 2 Trial 5 measured |S11| vs simulated |S11|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
# plot.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y', 'c', 'm'])))
ax0 = plot.subplot(111)
ax0.plot(freq, constant_0dB, 'k--', label="0dB reference")
ax0.plot(freq, measured_s11_mag_state5, 'r-', label="measured |s11| state 5, trial 2")
ax0.plot(freq, sim_s11_mag_state5, 'b--', label="simulated |s11| state 5")
ax0.axis([1e9, 5e9, -50, 5])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('|S11| (dB)')
plot.title('Panel 2 Trial 5 measured |S11| vs simulated |S11|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
# plot.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y', 'c', 'm'])))
ax0 = plot.subplot(111)
ax0.plot(freq, constant_0dB, 'k--', label="0dB reference")
ax0.plot(freq, measured_s11_mag_state6, 'r-', label="measured |s11| state 6")
ax0.plot(freq, sim_s11_mag_state6, 'b--', label="simulated |s11| state 6")
ax0.axis([1e9, 5e9, -50, 5])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('|S11| (dB)')
plot.title('Panel 2 Trial 5 measured |S11| vs simulated |S11|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
# plot.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y', 'c', 'm'])))
ax0 = plot.subplot(111)
ax0.plot(freq, constant_0dB, 'k--', label="0dB reference")
ax0.plot(freq, measured_s11_mag_state7, 'r-', label="measured |s11| state 7")
ax0.plot(freq, sim_s11_mag_state7, 'b--', label="simulated |s11| state 7")
ax0.axis([1e9, 5e9, -50, 5])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('|S11| (dB)')
plot.title('Panel 2 Trial 5 measured |S11| vs simulated |S11|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

plot.show()
# *************************************************************************
file1.close()
file2.close()
