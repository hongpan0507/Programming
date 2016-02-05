# ecen641 hw1; problem 1.27
# Microwave Transistor Amplifier page 91

from cmath import exp
import numpy as np
import utilities as utl

pi = 3.14156
deg_rad = pi/180

# common-emitter S-parameter given in the problem
s11_e = 0.73*exp(1j*-128*deg_rad)
s21_e = 1.73*exp(1j*73*deg_rad)
s12_e = 0.045*exp(1j*114*deg_rad)
s22_e = 0.75*exp(1j*-52*deg_rad)

s_mtx_e = np.array([[s11_e, s12_e], [s21_e, s22_e]], dtype=complex)

# convert common-emitter S-parameter to common-emitter y-matrix parameter
# Microwave Transistor Amplifier page 62
y_matrix_e = utl.s_to_y(s_mtx_e)

# convert common-emitter y-matrix parameter to common-base y-matrix parameter
# Microwave Transistor Amplifier page 63
y_matrix_b = utl.y_e_to_y_b(y_matrix_e)

# convert common-emitter y-matrix parameter to common-collect y-matrix parameter
# Microwave Transistor Amplifier page 63
y_matrix_c = utl.y_e_to_y_c(y_matrix_e)

# convert common-base y-matrix parameter to common-base s-matrix parameter
# Microwave Transistor Amplifier page 62
s_matrix_b = utl.y_to_s(y_matrix_b)

# convert common-collector y-matrix parameter to common-collect s-matrix parameter
# Microwave Transistor Amplifier page 62
s_matrix_c = utl.y_to_s(y_matrix_c)

print ('s-parameter base: ')
print(s_matrix_b)
print ('s-parameter collector: ')
print(s_matrix_c)
