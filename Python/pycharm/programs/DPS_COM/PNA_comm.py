import socket
import serial
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from time import time
import csv
import struct

startTime = time()

# connect to network analyzer server
server_address = ('165.91.209.113',5025)
pna = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pna.connect(server_address)
pna.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

# python 3 requires encoding string for bit encoding
pna.send('CALC:PAR:DEL:ALL\n'.encode())  # delete all measurement
sleep(1)    # wait for 1 second

# creates a measurement, but does not display it
# define a s21 measurement using channel1, 'CH1_S21_MEAS'
pna.send('CALC1:PAR:DEF:EXT \'CH1_S21_MEAS\',S21\n'.encode())

# select "CH1_S21_MEAS" measurement
pna.send('CALC1:PAR:SEL \'CH1_S21_MEAS\'\n'.encode())

# create a new trace and associate "CH1_S21_MEAS" with the a window
pna.send('DISP:WIND1:TRAC1:FEED \'CH1_S21_MEAS\'\n'.encode())

pna.send('DISP:WIND1:TRAC1:Y:RPOS MAX\n'.encode())  # set trace display reference postion
pna.send('DISP:WIND1:TRAC1:Y:RLEV 0\n'.encode())    # set trace display Y axis reference postion
pna.send('DISP:WIND1:TRAC1:Y:PDIV 10\n'.encode())   # set Y axis division

pna.send('CALC1:FORM UPH\n'.encode())   # measure uwrapped phase

pna.send('FORM:DATA ASCII\n'.encode())    # return data format

################################ ASCII format, save as CSV ###############################
# defined by user when calibrating the network analyzer
freq_start = 2e9    # start frequency in Hz
freq_stop = 4e9    # stop frequency in Hz
data_point = 2001     # defined by user when calibrating the network analyzer
freq_step = (freq_stop-freq_start)/(data_point-1)

for i in range(0, 5):
    print(pna.send('CALC1:DATA? FDATA \n'.encode()))  # quarry for data
    # data returned by the analyzer
    data_size = 20  # fixed number for ASCII format; trial and error
    byte_array = pna.recv(data_size*data_point)     # returns byte object
    str_array = byte_array.decode()     # return a string of data separated by commas
    data_array = str_array.split(',')   # turn into list of string
    print(data_array)  # receive byte object, then decode into string

    csv_file = open('data.csv', 'w', newline='')   # create and open csv file for writing, no additional newline
    csv_w = csv.writer(csv_file, delimiter=',')   # open csv file with csv writer

    # column header
    csv_w.writerow(['Freq(Hz)', 's21 unwrapped phase(Deg)'])
    data_row = []
    # freq_plot = []
    # data_plot = []
    for i in range(0, len(data_array)):
        freq = freq_start + freq_step*i     # increment frequency point
        data_row.append(freq)   # save frequency point
        data_row.append(float(data_array[i]))   # save data point
        csv_w.writerow(data_row)  # [freq, data]; save data into csv
        data_row = []   # erase temp row data and restart

    csv_file.close()
# wait = input("Press Enter to Continue")

###########################################################################################


######################### working, but real 32 need more decoding #######################
# pna.send('FORM:DATA REAL,32\n'.encode())    # return data format; REAL,32 or REAL,64 or ASCII
# print(pna.send('CALC1:DATA? FDATA \n'.encode()))    # quarry for data
# # PNA returns byte object
# header_start = pna.recv(1) # data byte starts with #
# print(header_start)
# header_num_b = pna.recv(1)  # second byte tells how many more bytes will follow
# header_num_str = header_num_b.decode()  # decode byte object to string
# header_num_int = int(header_num_str)
# # receive the number of bytes based on header_num_int and extract the data
# data_num_b = pna.recv(header_num_int)
# data_num_str = data_num_b.decode()  # decode byte object to string
# data_num_int = int(data_num_str)
# print(data_num_int)
#
# data_point = data_num_int/4    # divide by 4 because using real 64 data format
# print(data_point)
#
# for i in range(0,11):
#     ++i
#     print(pna.recv(4))
##############################################################################################

# wait = input("Press Enter to Continue")

pna.close()
