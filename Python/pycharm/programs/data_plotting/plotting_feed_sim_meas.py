# Program Function:
#   plots the s parameter data

import csv
from matplotlib import pyplot as plot
import numpy as np

# ***************************** Simulated Data *****************************
file1 = open('simulated_state_0_s11.csv', 'rb')  # open the file for reading
sim_csv_s11_mag_state0 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
# *************************************************************************

# ***************************** Measured Data *****************************
file2 = open('state_0.csv', 'rb')  # open the file for reading
measured_csv_s11_mag_state0 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
# *************************************************************************

# extract information from csv and store in the following lists for plotting and processing
freq = []
constant_0dB = []
sim_s11_mag_state0 = []
measured_s11_mag_state0 = []


# ***************************** Simulated Data *****************************
# *************************************************************************

# ***************************** Measured Data *****************************
for row in measured_csv_s11_mag_state0:   # row contains the row data
    if measured_csv_s11_mag_state0.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        freq.append(row[0])
        constant_0dB.append(0)
        measured_s11_mag_state0.append(row[1])

for row in sim_csv_s11_mag_state0:   # row contains the row data
    if sim_csv_s11_mag_state0.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        sim_s11_mag_state0.append(row[1])

print sim_s11_mag_state0.__sizeof__()
print measured_s11_mag_state0.__sizeof__()
print freq.__sizeof__()
# *************************************************************************

plot.figure(1)
ax0 = plot.subplot(111)
ax0.plot(freq, constant_0dB, 'g--', label="0dB reference")
ax0.plot(freq, measured_s11_mag_state0, 'r-', label="measured |s11|")
ax0.plot(freq, sim_s11_mag_state0, 'b-', label="simulated |s11|")
ax0.axis([1e9, 5e9, -40, 5])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('|S11| (dB)')
plot.title('State 0 |S11|')
plot.legend(loc=3)  # loc=4 => bottom right corner
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1)
plot.show()

# file1.close()
file2.close()
