# ecen641 hw1; problem 1.27
# Microwave Transistor Amplifier page 91
# Hong Pan

from cmath import exp

pi = 3.14156
deg_rad = pi/180

# common-emitter S-parameter given in the problem
s11_e = 0.73*exp(1j*-128*deg_rad)
s21_e = 1.73*exp(1j*73*deg_rad)
s12_e = 0.045*exp(1j*114*deg_rad)
s22_e = 0.75*exp(1j*-52*deg_rad)

# convert common-emitter S-parameter to common-emitter y-matrix parameter
# Microwave Transistor Amplifier page 62
del6 = (1+s11_e)*(1+s22_e) - s12_e*s21_e
y11_e = ((1-s11_e)*(1+s22_e) + s12_e*s21_e)/del6
y12_e = -2*s12_e/del6
y21_e = -2*s21_e/del6
y22_e = ((1+s11_e)*(1-s22_e) + s12_e*s21_e)/del6

# convert to common-emitter y-matrix parameter to common-base y-matrix parameter
# Microwave Transistor Amplifier page 63
y11_b = y11_e + y12_e + y21_e + y22_e
y12_b = -1*(y12_e+y22_e)
y21_b = -1*(y21_e+y22_e)
y22_b = y22_e

# convert to common-emitter y-matrix parameter to common-collect y-matrix parameter
# Microwave Transistor Amplifier page 63
y11_c = y11_e
y12_c = -1*(y11_e+y12_e)
y21_c = -1*(y11_e+y21_e)
y22_c = y11_b

# convert to common-base y-matrix parameter to common-base s-matrix parameter
# Microwave Transistor Amplifier page 62
del2 = (1+y11_b)*(1+y22_b) - y12_b*y21_b
s11_b = ((1-y11_b)*(1+y22_b) + y12_b*y21_b)/del2
s12_b = -2*y12_b/del2
s21_b = -2*y21_b/del2
s22_b = ((1+y11_b)*(1-y22_b) + y12_b*y21_b)/del2

# convert to common-collector y-matrix parameter to common-collect s-matrix parameter
# Microwave Transistor Amplifier page 62
del2 = (1+y11_c)*(1+y22_c) - y12_c*y21_c
s11_c = ((1-y11_c)*(1+y22_c) + y12_c*y21_c)/del2
s12_c = -2*y12_c/del2
s21_c = -2*y21_c/del2
s22_c = ((1+y11_c)*(1-y22_c) + y12_c*y21_c)/del2

print ('s-parameter base: ')
print(s11_b)
print(s12_b)
print(s21_b)
print(s22_b)

print ('s-parameter collector: ')
print(s11_c)
print(s12_c)
print(s21_c)
print(s22_c)