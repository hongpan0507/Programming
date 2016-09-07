# Program function:
# 1. calculate Gamma
# 2. calculate Gain
# 3. calculate VSWR


from cmath import exp, sqrt, log
from numpy import conj
import numpy as np


pi = 3.14156
deg_rad = pi/180

# book example 3.2.1; page 214; for testing only
# a. find G_T, G_A, G_p
s11 = 0.6*exp(1j*-160*deg_rad)
s12 = 0.045*exp(1j*16*deg_rad)
s21 = 2.5*exp(1j*30*deg_rad)
s22 = 0.5*exp(1j*-90*deg_rad)
gamma_s = 0.5*exp(1j*120*deg_rad)
gamma_L = 0.4*exp(1j*90*deg_rad)
# b. calculate P_AVS, P_IN, P_AVN, P_L
E_1 = 10*exp(1j*0*deg_rad)  # source voltage
Z_1 = 50    # source impedance
# c. caluclate VSWR_in VSWR_out

gamma_OUT = s22 + s12*s21*gamma_s/(1-s11*gamma_s)   # page 214; 3.2.6
gamma_IN = s11 + s12*s21*gamma_L/(1-s22*gamma_L)    # page 214; 3.2.5
print u'\u0393OUT' + " = %.3f" % abs(gamma_OUT) + " e^(j*%.1f" % (np.angle(gamma_OUT)/deg_rad) + ")"   # u'\u0393' = gamma in greek letter
print u'\u0393IN' + " = %.3f" % abs(gamma_IN) + " e^(j*%.1f" % (np.angle(gamma_IN)/deg_rad) + ")"   # u'\u0393' = gamma in greek letter
print "-----------------------------------------------------------------"

M_s = (1 - abs(gamma_s)**2)*(1 - abs(gamma_IN)**2)/abs(1 - gamma_s*gamma_IN)**2  # source mismatch factor; p188; 2.7.17
M_L = (1 - abs(gamma_L)**2)*(1 - abs(gamma_OUT)**2)/abs(1 - gamma_OUT*gamma_L)**2  # load mismatch factor; p190; 2.7.25
print "M_s = %.4f" % M_s
print "M_s(dB) = %.3f" % abs((10*log(M_s, 10)))      # default complex number, use abs() to turn it into normal one
print "M_L = %.4f" % M_L
print "M_L(dB) = %.3f" % abs((10*log(M_L, 10)))      # default complex number, use abs() to turn it into normal one
print "-----------------------------------------------------------------"

# G_T = (1-abs(gamma_s)**2)/abs(1-gamma_IN*gamma_s)**2 * abs(s21)**2 * (1-abs(gamma_L)**2)/abs(1-s22*gamma_L)**2     # p213; 3.2.1
G_T = (1-abs(gamma_s)**2)/abs(1-s11*gamma_s)**2 * abs(s21)**2 * (1-abs(gamma_L)**2)/abs(1-gamma_OUT*gamma_L)**2     # p213; 3.2.2
G_p = 1/(1-abs(gamma_IN)**2) * abs(s21)**2 * (1-abs(gamma_L)**2)/abs(1-s22*gamma_L)**2     # p213; 3.2.3
G_A = (1-abs(gamma_s)**2)/abs(1-s11*gamma_s)**2 * abs(s21)**2 * 1/(1-abs(gamma_OUT)**2)     # p213; 3.2.4
print "G_T = %.2f" % G_T
print "G_T(dB) = %.2f" % np.real((10*log(G_T, 10)))      # default complex number
print "G_p = %.2f" % G_p
print "G_p(dB) = %.2f" % np.real((10*log(G_p, 10)))      # default complex number
print "G_A = %.2f" % G_A
print "G_A(dB) = %.2f" % np.real((10*log(G_A, 10)))      # default complex number
print "-----------------------------------------------------------------"

P_AVS = E_1**2/(8*np.real(Z_1))     # power available from the source
P_IN = P_AVS * M_s  # p215; 3.2.7   # power input to the network
P_L = G_T * P_AVS   # p213; p216; power delivered to the load
P_AVN = G_A * P_AVS # p213; p216; power available from the network
print "P_AVS(W) = %.4f" % np.real(P_AVS)
print "P_IN(W) = %.4f" % np.real(P_IN)
print "P_L(W) = %.4f" % np.real(P_L)
print "P_AVN(W) = %.4f" % np.real(P_AVN)
print "-----------------------------------------------------------------"

gamma_a = abs((gamma_IN-conj(gamma_s))/(1-gamma_IN*gamma_s))    # p260; 3.8.2
VSWR_in = (1+abs(gamma_a))/(1-abs(gamma_a))
gamma_b = abs((gamma_OUT-conj(gamma_L))/(1-gamma_OUT*gamma_L))    # p260; 3.8.2
VSWR_out = (1+abs(gamma_b))/(1-abs(gamma_b))
print "VSWR_in = %.3f" % abs(VSWR_in)
print "VSWR_out = %.3f" % abs(VSWR_out)
