import csv
import matplotlib.pyplot as plot
from math import log10 as log10

# read csv file
file_0_r = open('0.csv', 'rb')   # open csv file
s11_0_read = csv.reader(file_0_r, delimiter=',')   # convert csv file to python reader object
file_1_r = open('1.csv', 'rb')   # open csv file
vswr_1_read = csv.reader(file_1_r, delimiter=',')   # convert csv file to python reader object
file_1_w = open('1_modified.csv', 'wb')   # open csv file
s11_1_write = csv.writer(file_1_w, delimiter=',')   # convert csv file to python writer object

freq = []
s11_log_0 = []
s11_log_1 = []

for row in s11_0_read:
    if s11_0_read.line_num >= 9:  # store real data that starts at line #9 into a list
        if row[0] == 'END':     # check if row reaches the last one
            break
        s11_log_0.append(float(row[1]))

for row in vswr_1_read:     # row carries all the row information
    if vswr_1_read.line_num == 8:    # picks up the title
        row[1] = 'S11 Log Mag(dB)'
        s11_1_write.writerow(row)
    if vswr_1_read.line_num >= 9:    # store real data that starts at line #9 into a new csv file
        if row[0] == 'END':     # check if row reaches the last one
            break
        row[0] = float(row[0])/1e9
        row[1] = (float(row[1])-1)/(float(row[1])+1)  # convert from vswr to s11_log_1
        row[1] = 20*log10(row[1])
        freq.append(row[0])
        s11_log_1.append(row[1])
        s11_1_write.writerow(row)

plot.figure(1)
ax = plot.subplot(211)
plot.plot(freq, s11_log_0)
plot.axis([1.5, 4.5, -15, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('Magnitude (dB)')
plot.title('state 0')

ax = plot.subplot(212)
plot.plot(freq, s11_log_1)
plot.axis([1.5, 4.5, -15, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('Magnitude (dB)')
plot.title('state 1')
plot.show()

file_0_r.close()
file_1_r.close()
file_1_w.close()