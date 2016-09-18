import socket
import serial
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from time import time

startTime = time()

server_address = ('165.91.209.113',5025)
pna = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pna.connect(server_address)
pna.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

pna.send('CALC:PAR \'CH1_S12_1\',S12\n')

temp = input("Press Enter to Continue")

pna.close()
