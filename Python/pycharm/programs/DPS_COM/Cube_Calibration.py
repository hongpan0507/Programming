import socket
import serial
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from time import time

startTime = time()

server_address = ('165.91.209.114',5025)
def initialize():
    pna.send('CALC:PAR:DEL:ALL\n')
    sleep(1)
    pna.send('CALC:PAR \'CH1_S12_1\',S12\n')
    pna.send('DISP:WIND1:TRAC1:FEED \'CH1_S12_1\'\n')
    pna.send('DISP:WIND1:TRAC1:Y:RPOS MAX\n')
    pna.send('DISP:WIND1:TRAC1:Y:RLEV 0\n')
    pna.send('DISP:WIND1:TRAC1:Y:PDIV 10\n')
    pna.send('CALC:PAR:SEL \'CH1_S12_1\'\n')
    pna.send('CALC:FORM MLOG\n')
    pna.send('CALC:MARK ON\n')
    pna.send('CALC:MARK:X 2460 MHz\n')
    pna.send('CALC:PAR \'CH1_S12_2\',S12\n')
    pna.send('DISP:WIND2:TRAC1:FEED \'CH1_S12_2\'\n')
    pna.send('CALC:PAR:SEL \'CH1_S12_2\'\n')
    pna.send('CALC:FORM PHAS\n')
    pna.send('CALC:MARK2 ON\n')
    pna.send('CALC:MARK2:X 2460 MHz\n')
    pna.send('SENS:AVER ON\n')
    pna.send('SENS:AVER:MODE SWEEP\n')
    pna.send('SENS:AVER:COUN 2\n')
    sleep(1)

def readMarker(num):
    pna.send('SENS:AVER:CLE\n')
    sleep(3)
    command = 'CALC:PAR:SEL \'CH1_S12_'+str(num)+'\'\n'
    pna.send(command)
    command = 'CALC:MARK'+str(num)+':Y?\n'
    pna.send(command)
    result = pna.recv(100)
    result = result.split(',')
    result = float(result[0])
    return result

pna = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pna.connect(server_address)
pna.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

y = readMarker(1)
y = readMarker(1)


pna.close()

endTime = time()

totalTime = endTime-startTime

minutes = int(totalTime/60)

seconds = int(np.round(totalTime - (minutes*60)))

print('\nCalibration Completed in '+str(minutes)+' min '+str(seconds)+' sec')

# f = open('../../CalibrationResults/Cube/Calibration_'+str(deviceNumber)+'.txt','w')
#
# f.write('Vmi = '+str(Vmi)+'V\n')
# f.write('Vmq = '+str(Vmq)+'V\n')
# f.write('Gmax = '+str(maxGain)+'dB, '+str(pow(10,maxGain/20))+'\n')
# f.write('Phase Offset = '+str(phaseOffset)+'\n\n')
#
# f.write('Vrange = '+str(Vrange)+'V\n')
# f.write('Gnull = '+str(Gnull)+'dB, '+str(pow(10,Gnull/20))+'\n\n')
#
# f.write('copy for arduino code:\n')
# f.write('const double Gmax = '+str(np.round(pow(10,maxGain/20),5))+';\n')
# f.write('const double Gnull = '+str(np.round(pow(10,Gnull/20),5))+';\n')
# f.write('const float phase_offset = '+str(phaseOffset)+';\n')
# f.write('const float Vmi = '+str(Vmi)+';\n')
# f.write('const float Vmq = '+str(Vmq)+';\n')
# f.write('const float Vr = '+str(Vrange)+';')
#
# f.close()
