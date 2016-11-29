import serial
import time
import numpy as np

port = "COM4"  # bluetooth comm port
baud = 9600     # baud rate of UART

ser = serial.Serial(port, baud, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=1)

if ser.isOpen():
    print(ser.name + " is open")

    while True:
        cmd_in_str = input("TX >>  ")  # user input
        cmd_in_int = int(cmd_in_str, 16)   # parse the string as hex and convert to int
        # print(cmd_in_int.to_bytes(1, byteorder='big'))    #Debugging
        ser.write(cmd_in_int.to_bytes(1, byteorder='big'))  # send the byte thru com port
        print('RX << ' + str(ser.read().hex()))  # receive sent byte as feedback
        time.sleep(0.1)

        # TX_cmd = DAC_cmd(CMD_WU_all, DAC_B, temp)
        # for j in range(0, len(TX_cmd)):
        #     ser.write(bytes([TX_cmd[j]]))  # send the byte thru com port
        #     print('RX << ' + str(ser.read().hex()))   # receive sent byte as feedback
        #     time.sleep(0.1)
        print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))

else:
    print("fail to connect to " + ser.name)

ser.close()
