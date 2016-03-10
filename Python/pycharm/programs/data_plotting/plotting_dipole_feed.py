# Program Function:
#   plots the s parameter data

import csv
from matplotlib import pyplot as plot
import numpy as np

# ***************************** Simulated Data *****************************
# *************************************************************************

# ***************************** Measured Data *****************************
file2 = open('dipole_feed_port1.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state0_port1 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('dipole_feed_port2.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state0_port2 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
# *************************************************************************

# extract information from csv and store in the following lists for plotting and processing
freq = []
constant_0dB = []
# sim_s11_mag_on = []
# sim_s11_mag_off = []
# sim_s21_mag_on = []
# sim_s21_mag_off = []

measured_s11_mag_state0_port1 = []
measured_s11_mag_state0_port2 = []

# ***************************** Simulated Data *****************************
# *************************************************************************

# ***************************** Measured Data *****************************
for row in measured_csv_s11_mag_state0_port1:   # row contains the row data
    if measured_csv_s11_mag_state0_port1.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        freq.append(row[0])
        constant_0dB.append(0)
        measured_s11_mag_state0_port1.append(row[1])

for row in measured_csv_s11_mag_state0_port2:   # row contains the row data
    if measured_csv_s11_mag_state0_port2.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_s11_mag_state0_port2.append(row[1])
# *************************************************************************

plot.figure(1)
ax0 = plot.subplot(111)
ax0.plot(freq, constant_0dB, 'b--', label="0dB reference")
ax0.plot(freq, measured_s11_mag_state0_port1, 'r-', label="|s11| port 1")
ax0.plot(freq, measured_s11_mag_state0_port2, 'b-', label="|s11| port 2")
ax0.axis([1e9, 5e9, -50, 5])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('|S11| (dB)')
plot.title('Measured State 0 |S11|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1)
# plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner

plot.show()

# file1.close()
file2.close()
