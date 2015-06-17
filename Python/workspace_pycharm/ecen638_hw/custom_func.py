__author__ = 'hpan'

import math

#-------------------------hw 1--------------------------
#free space path loss functions; return loss in dB scale
def FSPL_func(d, wave_len):
    temp1 = 4*math.pi*d/wave_len
    FSPL = math.pow(temp1,2)
    FSPL_dB = 10*math.log10(FSPL)
    return FSPL_dB
#------------------------------------------------------

#-------------------------hw 2--------------------------


#------------------------------------------------------

def update_line(num, data, line):
    line.set_data(data[...,:num])
    return line,