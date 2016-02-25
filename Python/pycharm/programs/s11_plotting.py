import csv
import matplotlib.pyplot as plot
from math import log10 as log10

# read csv file
measured_file_0_r = open('measured_0_modified.csv', 'rb')   # open csv file
measured_s11_0_read = csv.DictReader(measured_file_0_r, delimiter=',')   # convert csv file to python reader object
measured_file_1_r = open('measured_1_modified.csv', 'rb')   # open csv file
measured_s11_1_read = csv.DictReader(measured_file_1_r, delimiter=',')   # convert csv file to python reader object
simulated_file_0_r = open('simulated_0.csv', 'rb')   # open csv file
simulated_s11_0_read = csv.DictReader(simulated_file_0_r, delimiter=',')   # convert csv file to python reader object
simulated_file_1_r = open('simulated_1.csv', 'rb')   # open csv file
simulated_s11_1_read = csv.DictReader(simulated_file_1_r, delimiter=',')   # convert csv file to python reader object

freq = []
measured_s11_log_0 = []
measured_s11_log_1 = []
simulated_s11_log_0 = []
simulated_s11_log_1 = []

for row in measured_s11_0_read:
    freq.append(float(row['Freq(GHz)']))
    measured_s11_log_0.append(float(row['S11 Log Mag(dB)']))

for row in measured_s11_1_read:
    measured_s11_log_1.append(float(row['S11 Log Mag(dB)']))

for row in simulated_s11_0_read:
    simulated_s11_log_0.append(float(row['dB(S(1,1)) []']))

for row in simulated_s11_1_read:
    simulated_s11_log_1.append(float(row['dB(S(1,1)) []']))

measured_file_0_r.close()
measured_file_1_r.close()
simulated_file_0_r.close()
simulated_file_1_r.close()

plot.figure(1)
ax0 = plot.subplot(211)
ax0.plot(freq, measured_s11_log_0, 'r-', label="measured_s11")
ax0.plot(freq, simulated_s11_log_0, 'b-', label="simulated_s11")
ax0.axis([1.5, 4.5, -45, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('S11 Magnitude (dB)')
plot.title('state 0')
plot.legend(loc=4)  # loc=4 => bottom right corner

ax1 = plot.subplot(212)
ax1.plot(freq, measured_s11_log_1, 'r-', label="measured_s11")
ax1.plot(freq, simulated_s11_log_1, 'b-', label="simulated_s11")
ax1.axis([1.5, 4.5, -45, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('S11 Magnitude (dB)')
plot.title('state 1')
plot.legend(loc=4)  # loc=4 => bottom right corner
plot.show()



