import numpy as np

# convert s-matrix parameter to y-matrix parameter
# Microwave Transistor Amplifier page 62
# s[0][0]=s11; s[0][1]=s12; s[1][0]=s21; s[1][1]=s22
# argument = 2x2 s-matrix parameter
# return = 2x2 y-matrix parameter
def s_to_y(s = [2, 2]):
    del6 = (1+s[0][0])*(1+s[1][1]) - s[0][1]*s[1][0]
    y_mtx = np.zeros([2, 2], dtype=complex)
    y_mtx[0][0] = ((1-s[0][0])*(1+s[1][1]) + s[0][1]*s[1][0])/del6  # y11
    y_mtx[0][1] = -2*s[0][1]/del6   # y12
    y_mtx[1][0] = -2*s[1][0]/del6   # y21
    y_mtx[1][1] = ((1+s[0][0])*(1-s[1][1]) + s[0][1]*s[1][0])/del6  # y22
    return y_mtx

# convert y-matrix parameter to s-matrix parameter
# Microwave Transistor Amplifier page 62
# argument = 2x2 y-matrix parameter
# return = 2x2 s-matrix parameter
def y_to_s(y = [2, 2]):
    del2 = (1+y[0][0])*(1+y[1][1]) - y[0][1]*y[1][0]
    s_mtx = np.zeros([2, 2], dtype=complex)
    s_mtx[0][0] = ((1-y[0][0])*(1+y[1][1]) + y[0][1]*y[1][0])/del2
    s_mtx[0][1] = -2*y[0][1]/del2
    s_mtx[1][0] = -2*y[1][0]/del2
    s_mtx[1][1] = ((1+y[0][0])*(1-y[1][1]) + y[0][1]*y[1][0])/del2
    return s_mtx

# convert common-emitter y-matrix parameter to common-base y-matrix parameter
# Microwave Transistor Amplifier page 63
# argument = 2x2 y-matrix parameter; common emitter
# return = 2x2 y-matrix parameter; common base
def y_e_to_y_b(y_e = [2, 2]):
    y_b_mtx = np.zeros([2, 2], dtype=complex)
    y_b_mtx[0][0] = y_e[0][0] + y_e[0][1] + y_e[1][0] + y_e[1][1]
    y_b_mtx[0][1] = -1*(y_e[0][1]+y_e[1][1])
    y_b_mtx[1][0] = -1*(y_e[1][0]+y_e[1][1])
    y_b_mtx[1][1] = y_e[1][1]
    return y_b_mtx

# convert common-emitter y-matrix parameter to common-collect y-matrix parameter
# Microwave Transistor Amplifier page 63
# argument = 2x2 y-matrix parameter; common emitter
# return = 2x2 y-matrix parameter; common collector
def y_e_to_y_c(y_e = [2, 2]):
    y_c_mtx = np.zeros([2, 2], dtype=complex)
    y_c_mtx[0][0] = y_e[0][0]
    y_c_mtx[0][1] = -1*(y_e[0][0]+y_e[0][1])
    y_c_mtx[1][0] = -1*(y_e[0][0]+y_e[1][0])
    y_c_mtx[1][1] = y_e[0][0] + y_e[0][1] + y_e[1][0] + y_e[1][1]
    return y_c_mtx