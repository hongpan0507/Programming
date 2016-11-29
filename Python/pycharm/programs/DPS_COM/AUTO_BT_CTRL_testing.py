import serial
import time
import struct
import numpy as np

port = "COM4"  # bluetooth comm port
baud = 9600     # baud rate of UART

ser = serial.Serial(port, baud, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=1)

if ser.isOpen():
    print(ser.name + " is open")
    print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))

    for board in range(1,6):
        print("Testing board #" + str(board) + ":")
        for port in range(1,5):
            print(("Testing port #" + str(port) + ":"))
            for phase in range(0, 16):
                print(("Board #" + str(board) + "; port #" + str(port) + "; phase shifte = " + str(phase*22.5) + "deg"))
                ser.write(struct.pack('>B', 0xFF))  # start of cmd
                print('RX << ' + str(ser.read().hex()))  # receive sent byte as feedback
                time.sleep(0.1)
                ser.write(struct.pack('>B', board))  # select board
                print('RX << ' + str(ser.read().hex()))  # receive sent byte as feedback
                time.sleep(0.1)
                ser.write(struct.pack('>B', port))  # select port
                print('RX << ' + str(ser.read().hex()))  # receive sent byte as feedback
                time.sleep(0.1)
                ser.write(struct.pack('>B', phase))    # phase shift
                print('RX << ' + str(ser.read().hex()))  # receive sent byte as feedback
                time.sleep(2)
                # wait = input("Press Enter to Continue")

else:
    print("fail to connect to " + ser.name)

print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))
ser.close()
