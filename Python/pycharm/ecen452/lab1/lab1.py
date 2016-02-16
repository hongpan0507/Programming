# import sys
# sys.path.insert(0, 'D:\Github\Programming\Python\pycharm')

import csv

# Reading CSV file
hfss_file1 = open('hfss_ECEN_452_Lab1a_s_para.csv', 'rb')   # open csv file
hfss_file2 = open('hfss_ECEN_452_Lab1b_s_para.csv', 'rb')   # open csv file
hfss_a_s_para = csv.DictReader(hfss_file1, delimiter=',')   # convert csv file to python DictReader object
hfss_b_s_para = csv.DictReader(hfss_file2, delimiter=',')   # convert csv file to python DictReader object

# array to hold all the data
# a_s_para = with de-embedding
# b_s_para = without de-embedding
a_s_para = []   # [[freq], [s11], [s12], [s21], [s22]]
hfss_a_freq = []
hfss_a_s11 = []
hfss_a_s12 = []
hfss_a_s21 = []
hfss_a_s22 = []

b_s_para = []   # [[freq], [s11], [s12], [s21], [s22]]
hfss_b_freq = []
hfss_b_s11 = []
hfss_b_s12 = []
hfss_b_s21 = []
hfss_b_s22 = []

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

# combine all the lists
a_s_para.append(hfss_a_freq)    # a_s_para = with de-embedding
a_s_para.append(hfss_a_s11)
a_s_para.append(hfss_a_s12)
a_s_para.append(hfss_a_s21)
a_s_para.append(hfss_a_s22)

b_s_para.append(hfss_b_freq)    # b_s_para = without de-embedding
b_s_para.append(hfss_b_s11)
b_s_para.append(hfss_b_s12)
b_s_para.append(hfss_b_s21)
b_s_para.append(hfss_b_s22)

for i in xrange(0, len(a_s_para)):
    print a_s_para[i]

for i in xrange(0, len(b_s_para)):
    print b_s_para[i]




