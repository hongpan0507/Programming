# Program Function:
#   plots the s parameter data

import csv
from matplotlib import pyplot as plot
import numpy as np

# ***************************** Simulated Data *****************************
# *************************************************************************

# ***************************** Measured Data *****************************
file2 = open('reflect_port1.csv', 'rb')  # open the file for reading
measured_csv_reflect_s11_mag_port1 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('reflect_port2.csv', 'rb')  # open the file for reading
measured_csv_reflect_s11_mag_port2 = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('thru.csv', 'rb')  # open the file for reading
measured_csv_thru_s_para = csv.reader(file2, delimiter=',')   # convert cvs file to python list
file2 = open('line.csv', 'rb')  # open the file for reading
measured_csv_line_s_para = csv.reader(file2, delimiter=',')   # convert cvs file to python list
# *************************************************************************

# extract information from csv and store in the following lists for plotting and processing
freq = []
constant_0 = []
constant_neg_90 = []
# sim_s11_mag_on = []
# sim_s11_mag_off = []
# sim_s21_mag_on = []
# sim_s21_mag_off = []

measured_reflect_s11_mag_port1 = []
measured_reflect_s11_mag_port2 = []
measured_thru_s11_mag = []
measured_thru_s21_mag = []
measured_thru_s21_phase = []
measured_line_s11_mag = []
measured_line_s21_mag = []
measured_line_s21_phase = []

# ***************************** Simulated Data *****************************
# *************************************************************************

# ***************************** Measured Data *****************************
for row in measured_csv_reflect_s11_mag_port1:   # row contains the row data
    if measured_csv_reflect_s11_mag_port1.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        freq.append(row[0])
        constant_0.append(0)
        constant_neg_90.append(-90)
        measured_reflect_s11_mag_port1.append(row[1])

for row in measured_csv_reflect_s11_mag_port2:   # row contains the row data
    if measured_csv_reflect_s11_mag_port2.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_reflect_s11_mag_port2.append(row[1])
        
for row in measured_csv_thru_s_para:   # row contains the row data
    if measured_csv_thru_s_para.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_thru_s11_mag.append(row[1])
        measured_thru_s21_mag.append(row[2])
        measured_thru_s21_phase.append(row[3])

for row in measured_csv_line_s_para:   # row contains the row data
    if measured_csv_line_s_para.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        measured_line_s11_mag.append(row[1])
        measured_line_s21_mag.append(row[2])
        measured_line_s21_phase.append(row[3])
# *************************************************************************

fig = plot.figure(1)
ax0 = plot.subplot(111)
ax0.plot(freq, constant_0, 'b--', label="0dB reference")
ax0.plot(freq, measured_reflect_s11_mag_port1, 'r-', label="|s11| port 1")
ax0.plot(freq, measured_reflect_s11_mag_port2, 'b-', label="|s11| port 2")
ax0.axis([1e9, 5e9, -10, 10])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('|S11| (dB)')
plot.title('Measured Reflect Standard |S11|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
fig.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1)
# fig.savefig('reflect.png', dpi=300)

fig = plot.figure(2)
ax0 = plot.subplot(311)
ax0.plot(freq, constant_0, 'b--', label="0dB reference")
ax0.plot(freq, measured_thru_s11_mag, 'r-', label="|s11| port 1")
ax0.axis([1e9, 5e9, -60, 10])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('|S11| (dB)')
plot.title('Measured Thru Standard |S11|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
ax0 = plot.subplot(312)
ax0.plot(freq, constant_0, 'b--', label="0dB reference")
ax0.plot(freq, measured_thru_s21_mag, 'r-', label="|s21|")
ax0.axis([1e9, 5e9, -2, 2])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('|S21| (dB)')
plot.title('Measured Thru Standard |S21|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
ax0 = plot.subplot(313)
ax0.plot(freq, constant_0, 'b--', label="0deg reference")
ax0.plot(freq, measured_thru_s21_phase, 'r-', label="s21 phase")
ax0.axis([1e9, 5e9, -10, 10])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('S21 phase (deg)')
plot.title('Measured Thru Standard S21 Phase')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
fig.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1)
# fig.savefig('thru.png', dpi=300)

fig = plot.figure(3)
ax0 = plot.subplot(311)
ax0.plot(freq, constant_0, 'b--', label="0dB reference")
ax0.plot(freq, measured_line_s11_mag, 'r-', label="|s11| port 1")
ax0.axis([1e9, 5e9, -60, 10])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('|S11| (dB)')
plot.title('Measured Line Standard |S11|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
ax0 = plot.subplot(312)
ax0.plot(freq, constant_0, 'b--', label="0dB reference")
ax0.plot(freq, measured_line_s21_mag, 'r-', label="|s21|")
ax0.axis([1e9, 5e9, -2, 2])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('|S21| (dB)')
plot.title('Measured Line Standard |S21|')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
ax0 = plot.subplot(313)
ax0.plot(freq, constant_neg_90, 'b--', label="-90deg reference")
ax0.plot(freq, measured_line_s21_phase, 'r-', label="s21 phase")
ax0.axis([1e9, 5e9, -160, -20])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (Hz)')
plot.ylabel('S21 phase (deg)')
plot.title('Measured line Standard S21 Phase')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
fig.tight_layout(pad=0.15, w_pad=0, h_pad=0)
fig.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1)

plot.show()

# file1.close()
file2.close()
