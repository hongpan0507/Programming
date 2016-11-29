import socket
import serial
import time
from time import time as current_time
import csv
import struct
from time import sleep
from matplotlib import pyplot

startTime = current_time()

############################### Bluetooth and PC comm ###################################
port = "COM4"  # bluetooth comm port
baud = 9600     # baud rate of UART

ser = serial.Serial(port, baud, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=1)
###########################################################################################

############################### PNA and PC comm ###################################
# connect to network analyzer server
server_address = ('165.91.209.113',5025)
pna = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pna.connect(server_address)
pna.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
print("PNA network connection: ok")
###########################################################################################

############################### PNA setup ###################################
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
print("PNA setup: ok")
###########################################################################################

##################### Data Collection, ASCII format, save as CSV, plot if have time #####################
# defined by user when calibrating the network analyzer
freq_start = 2e9    # start frequency in Hz
freq_stop = 4e9    # stop frequency in Hz
data_point = 2001     # defined by user when calibrating the network analyzer
freq_step = (freq_stop-freq_start)/(data_point-1)

if ser.isOpen():    # check bluetooth connection
    print(ser.name + " is open")
    print("Bluetooth connection: ok")
    print("Start Data Collection @ " + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))

    for board in range(1, 6):
        print("Testing board #" + str(board) + ":")
        for port in range(1, 5):
            print("Testing port #" + str(port) + ":")
            print("Step 1: Connect PNA output port to DPS Board #" + str(board) + " RF input port")
            print("Step 2: Connect PNA input port to DPS Board #" + str(board) + " Port" + str(port))
            wait = input("Press Enter to Continue")

            fig = pyplot.figure(0, figsize=(10, 6), dpi=80, facecolor='w')
            fig.suptitle("Digital Phase Shifter Port 0 to Port 1 Phase")
            # ax0 = pyplot.subplot(111)
            # ax0.set_title("Digital Phase Shifter S21 Phase", y=1.1)
            for phase in range(0, 16):
                # ------------------------------------------ BT sending cmd ----------------------------
                print(("Collectting: Board #" + str(board) + "; port #" + str(port) + "; phase shift = " + str(phase * 22.5) + "deg"))
                ser.write(struct.pack('>B', 0xFF))  # start of cmd
                print('TX >> ' + str(format(0xFF, '02x')))  # receive sent byte as feedback
                print('RX << ' + str(ser.read().hex()))  # receive sent byte as feedback
                time.sleep(0.1)
                ser.write(struct.pack('>B', board))  # select board
                print('TX >> ' + str(format(board, '02x')))  # receive sent byte as feedback
                print('RX << ' + str(ser.read().hex()))  # receive sent byte as feedback
                time.sleep(0.1)
                ser.write(struct.pack('>B', port))  # select port
                print('TX >> ' + str(format(port, '02x')))  # receive sent byte as feedback
                print('RX << ' + str(ser.read().hex()))  # receive sent byte as feedback
                time.sleep(0.1)
                ser.write(struct.pack('>B', phase))  # phase shift
                print('TX >> ' + str(format(phase, '02x')))  # receive sent byte as feedback
                print('RX << ' + str(ser.read().hex()))  # receive sent byte as feedback
                time.sleep(2)   # wait for 2 second for PNA to update measurement
                # -----------------------------------------------------------------------------------------
                # ------------------- PNA collecting data and PC save data as csv----------------------------
                # data returned by the analyzer
                print(pna.send('CALC1:DATA? FDATA \n'.encode()))  # quarry for data
                data_size = 20  # fixed number for ASCII format; trial and error
                byte_array = pna.recv(data_size * data_point)  # returns byte object
                str_array = byte_array.decode()  # return a string of data separated by commas
                data_array = str_array.split(',')  # turn into list of string
                print(data_array)  #receive byte object, then decode into string
                csv_f_name = './data/' + 'B'+ str(board) + 'P' + str(port) + 'PH' + str(phase) + '.csv'
                csv_file = open(csv_f_name, 'w', newline='')  # create and open csv file for writing, no additional newline
                csv_w = csv.writer(csv_file, delimiter=',')  # open csv file with csv writer

                # column header
                csv_w.writerow(['Freq(Hz)', 's21 unwrapped phase(Deg)'])
                data_row = []
                freq_plot = []
                data_plot = []
                for i in range(0, len(data_array)):
                    freq = freq_start + freq_step * i  # increment frequency point
                    data_row.append(freq)  # save frequency point
                    data_row.append(float(data_array[i]))  # save data point
                    freq_plot.append(freq)
                    data_plot.append(float(data_array[i]))

                    csv_w.writerow(data_row)  # [freq, data]; save data into csv
                    data_row = []  # erase temp row data and restart

                csv_file.close()

                pyplot.plot(freq_plot, data_plot, label="phase " + str(phase))
                # ax0.axis([1.5, 4.5, -180, 0])     # [xmin, xmax, ymin, ymax]

                pyplot.xlabel('Frequency (GHz)')
                pyplot.ylabel('S21 Phase (deg)')
                pyplot.subplots_adjust(left=0.2, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)
                pyplot.draw()
                pyplot.pause(0.0001)
                if phase == 15:
                    pyplot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
                    plot_f_name = './Plot/s21_phase_' + 'B' + str(board) + 'P' + str(port)
                    pyplot.savefig(plot_f_name, dpi=200, facecolor='w', edgecolor='k')
                    pyplot.close()
                # -----------------------------------------------------------------------------------------
else:
    print("fail to connect to " + ser.name)

print("Data Collection finished")
print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))


# wait = input("Press Enter to Continue")

###########################################################################################

pna.close()
