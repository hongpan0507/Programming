# import sys
# sys.path.insert(0, 'D:\Github\Programming\Python\pycharm')

import csv
import matplotlib.pyplot as plot

# Reading CSV file
hfss_file1 = open('hfss_ECEN_452_Lab1a_s_para.csv', 'rb')   # open csv file
hfss_file2 = open('hfss_ECEN_452_Lab1b_s_para.csv', 'rb')   # open csv file
z0lver_file1 = open('z0lver_ECEN_452_Lab1a.csv', 'rb')   # open csv file
z0lver_file2 = open('z0lver_ECEN_452_Lab1b.csv', 'rb')   # open csv file
hfss_a_s_para = csv.DictReader(hfss_file1, delimiter=',')   # convert csv file to python DictReader object
hfss_b_s_para = csv.DictReader(hfss_file2, delimiter=',')   # convert csv file to python DictReader object
z0lver_a_s_para = csv.DictReader(z0lver_file1, delimiter=',')   # convert csv file to python DictReader object
z0lver_b_s_para = csv.DictReader(z0lver_file2, delimiter=',')   # convert csv file to python DictReader object

# array to hold all the data
# a = with de-embedding
# b = without de-embedding
hfss_a_freq = []
hfss_a_s11 = []
hfss_a_s12 = []
hfss_a_s21 = []
hfss_a_s22 = []

hfss_b_freq = []
hfss_b_s11 = []
hfss_b_s12 = []
hfss_b_s21 = []
hfss_b_s22 = []

z0lver_a_freq = []
z0lver_a_s11 = []
z0lver_a_s12 = []
z0lver_a_s21 = []
z0lver_a_s22 = []

z0lver_b_freq = []
z0lver_b_s11 = []
z0lver_b_s12 = []
z0lver_b_s21 = []
z0lver_b_s22 = []

# parse the data and store in the list
for a_s_row in hfss_a_s_para:  # row is a python list that contains the data
    # read the column that matches the name 'Freq [GHz]' from a_s_row list
    # then convert to float and store in a array for future processing
    hfss_a_freq.append(float(a_s_row['Freq [GHz]']))
    hfss_a_s11.append(float(a_s_row['dB(S(1,1)) []']))
    hfss_a_s12.append(float(a_s_row['dB(S(1,2)) []']))
    hfss_a_s21.append(float(a_s_row['dB(S(2,1)) []']))
    hfss_a_s22.append(float(a_s_row['dB(S(2,2)) []']))

for b_s_row in hfss_b_s_para:  # row is a python list that contains the data
    # read the column that matches the name 'Freq [GHz]' from a_s_row list
    # then convert to float and store in a array for future processing
    hfss_b_freq.append(float(b_s_row['Freq [GHz]']))
    hfss_b_s11.append(float(b_s_row['dB(S(1,1)) []']))
    hfss_b_s12.append(float(b_s_row['dB(S(1,2)) []']))
    hfss_b_s21.append(float(b_s_row['dB(S(2,1)) []']))
    hfss_b_s22.append(float(b_s_row['dB(S(2,2)) []']))

for a_s_row in z0lver_a_s_para:  # row is a python list that contains the data
    # read the column that matches the name 'frequency' from a_s_row list
    # then convert to float and store in a array for future processing
    z0lver_a_freq.append(round(float(a_s_row['frequency'])/1e9, 3))
    z0lver_a_s11.append(float(a_s_row[' S11']))
    z0lver_a_s12.append(float(a_s_row[' S12']))
    z0lver_a_s21.append(float(a_s_row[' S21']))
    z0lver_a_s22.append(float(a_s_row[' S22']))

for b_s_row in z0lver_b_s_para:  # row is a python list that contains the data
    # read the column that matches the name 'frequency' from a_s_row list
    # then convert to float and store in a array for future processing
    z0lver_b_freq.append(round(float(b_s_row['frequency'])/1e9, 3))
    z0lver_b_s11.append(float(b_s_row[' S11']))
    z0lver_b_s12.append(float(b_s_row[' S12']))
    z0lver_b_s21.append(float(b_s_row[' S21']))
    z0lver_b_s22.append(float(b_s_row[' S22']))

# plotting
plot.plot(hfss_a_freq, hfss_a_s11, 'r--')
plot.plot(hfss_b_freq, hfss_b_s11, 'b-')
plot.plot(z0lver_a_freq, z0lver_a_s11, 'g--')
plot.plot(z0lver_b_freq, z0lver_b_s11, 'y-')
plot.axis([2, 3, -15, -10])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('Magnitude (dB)')
plot.show()
# plot.figure(1)  # create empty figure
# ax1 = plot.subplot(111)     # create axes handle for figure 1

print len(hfss_a_freq)
print len(hfss_b_freq)
print len(z0lver_a_freq)
print len(z0lver_b_freq)
print hfss_a_freq
print hfss_b_freq
print z0lver_a_freq
print z0lver_b_freq


