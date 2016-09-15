from cmath import exp, sqrt, log
from numpy import conj
import numpy as np


pi = 3.14156
deg_rad = pi/180

# book example 3.3.1; page 222; for testing only
# @ 500MHz
# s11 = 0.761*exp(1j*-151*deg_rad)
# s12 = 0.025*exp(1j*31*deg_rad)
# s21 = 11.84*exp(1j*102*deg_rad)
# s22 = 0.429*exp(1j*-35*deg_rad)

# book example 4.3.1; page 302; for testing only
# s11 = 0.552*exp(1j*169*deg_rad)
# s12 = 0.049*exp(1j*23*deg_rad)
# s21 = 1.681*exp(1j*26*deg_rad)
# s22 = 0.839*exp(1j*-67*deg_rad)
# gamma_opt = 0.475*exp(1j*166*deg_rad)
# gamma_s = gamma_opt     # optimal noise figure
# F_min_dB = 2.5  # minimum noise figure
# R_n = 3.5   # noise resistance
# z_0 = 50
# r_n = R_n/z_0     # normalized noise resistance; assume z_0 is 50 ohms

# book example 4.3.2; page 307; for testing only
s11 = 0.6*exp(1j*146*deg_rad)
s12 = 0.085*exp(1j*62*deg_rad)
s21 = 1.97*exp(1j*32*deg_rad)
s22 = 0.52*exp(1j*-63*deg_rad)
gamma_opt = 0.45*exp(1j*-150*deg_rad)
gamma_s = gamma_opt     # optimal noise figure
F_min_dB = 3.0   # dB scale
r_n = 0.2   # given by the problem

# problem 4.6; page 375
# s11 = 0.75*exp(1j*-116*deg_rad)
# s12 = 0.01*exp(1j*67*deg_rad)
# s21 = 3.5*exp(1j*64*deg_rad)
# s22 = 0.77*exp(1j*-65*deg_rad)
# gamma_opt = 0.65*exp(1j*120*deg_rad)    # from device datasheet or measurement data

# gamma_L = 0*exp(1j*0*deg_rad)
# gamma_s = 0*exp(1j*0*deg_rad)
# gamma_IN = s11 + s12*s21*gamma_L/(1-s22*gamma_L)    # page 214
# gamma_OUT = s22 + s12*s21*gamma_s/(1-s11*gamma_s)   # page 214

delta = s11*s22-s12*s21     # page 221
k = (1-abs(s11)**2-abs(s22)**2+abs(delta)**2)/(2*abs(s12*s21))    # page 221
print "delta = %.3f" % abs(delta) + " e^(j*%.1f" % (np.angle(delta)/deg_rad) + ")"
print "k = %.3f" % k

if k < 1 or abs(delta) > 1:
    print "potentially unstable"
    # input stability; page 218
    c_s = np.conj(s11-delta*np.conj(s22))/(abs(s11)**2-abs(delta)**2)
    r_s = abs(s12*s21/(abs(s11)**2-abs(delta)**2))
    # output stability
    c_l = np.conj(s22-delta*np.conj(s11))/(abs(s22)**2-abs(delta)**2)
    r_l = abs(s12*s21/(abs(s22)**2-abs(delta)**2))
    print "input stability circle: "
    print "center (Cs) = %.3f" % abs(c_s) + " e^(j*%.1f" % (np.angle(c_s)/deg_rad) + ")"
    print "radius (rs) = %.3f" % r_s
    if abs(s22) > 1:
        print "|s22| > 1"
    elif abs(s22) < 1:
        print "|s22| < 1"
    print "output stability circle: "
    print "center (Cl) = %.3f" % abs(c_l) + " e^(j*%.1f" % (np.angle(c_l)/deg_rad) + ")"
    print "radius (rl) = %.3f" % r_l
    if abs(s11) > 1:
        print "|s11| > 1"
    elif abs(s11) < 1:
        print "|s11| < 1"
else:
    print "unconditionally stable"
    print "maximum power transfer for bilateral case: "
    # Simultaneous conj match; p240
    # "unconditionally stable" is a necessary condition to have "Simultaneous conj match"; p241
    B1 = 1 + abs(s11)**2 - abs(s22)**2 - abs(delta)**2
    B2 = 1 + abs(s22)**2 - abs(s11)**2 - abs(delta)**2
    C1 = s11 - delta*conj(s22)
    C2 = s22 - delta*conj(s11)
    gamma_Ms = (B1 - sqrt(B1**2-4*abs(C1)**2))/(2*C1)
    gamma_ML = (B2 - sqrt(B2**2-4*abs(C2)**2))/(2*C2)
    print u'\u0393Ms' + " = %.3f" % abs(gamma_Ms) + " e^(j*%.1f" % (np.angle(gamma_Ms)/deg_rad) + ")"   # u'\u0393' = gamma in greek letter
    print u'\u0393ML' + " = %.3f" % abs(gamma_ML) + " e^(j*%.1f" % (np.angle(gamma_ML)/deg_rad) + ")"   # u'\u0393' = gamma in greek letter

    G_T_max = 1/(1-abs(gamma_Ms)**2) * abs(s21)**2 * (1-abs(gamma_ML)**2)/abs(1-s22*gamma_ML)**2
    # G_T = G_p = G_A under simultaneous conj match condition; p242
    print "G_T_max(dB) = G_A_max(dB) = %.2f" % abs((10*log(G_T_max, 10)))     # default complex number, use abs() to turn it into normal one

    print "Available Power-Gain Circle:"
    g_a = (1 - abs(gamma_s)**2)/(1 - abs(s22)**2 + abs(gamma_s)**2*(abs(s11)**2-abs(delta)**2) - 2*np.real(gamma_s*C1))  # page 257, equation 3.7.13
    C_a = g_a*np.conj(C1) / (1 + g_a*(abs(s11)**2-abs(delta)**2))   # equation 3.7.15
    r_a = (1 - 2*k*abs(s12*s21)*g_a + abs(s12*s21)**2*g_a**2)**0.5 / (abs(1 + g_a*(abs(s11)**2 - abs(delta)**2)))    # equation 3.7.16
    G_A = abs(s21)**2 * g_a     # equation 3.7.12
    print "G_A(dB) = %.2f" % abs((10*log(G_A, 10)))     # default complex number, use abs() to turn it into normal one
    print "Center (C_g_a) = %.3f" % abs(C_a) + " e^(j*%.1f" % (np.angle(C_a)/deg_rad) + ")"
    print "radius (r_g_a) = %.3f" % abs(r_a)

# page 304; given a gamma_opt, find gamma_L for max power transfer
print "Constant Noise Circle: "
F_i_dB = input("F_i(dB) = ")    # user input
F_i = 10**(float(F_i_dB)/10)    # convert from dB scale to normal scale
F_min = 10**(F_min_dB/10)   # convert from dB to normal; F_min_dB is given
N_i = (F_i - F_min)/(4*r_n)*abs(1+gamma_opt)**2     # noise parameter; equation 4.3.6 on page 299
C_F_i = gamma_opt/(1+N_i)   # center of constant noise circle; equation 4.3.7 on page 300
r_F_i = 1/(1+N_i)*sqrt(N_i**2 + N_i*(1-abs(gamma_opt)**2))
print "Noise parameter Ni = %.4f" % N_i
print "Center (C_Fi) = %.3f" % abs(C_F_i) + " e^(j*%.1f" % (np.angle(C_F_i)/deg_rad) + ")"
print "radius (r_Fi) = %.3f" % abs(r_F_i)

print "assume optimal noise figure or change gammas to obtain F"
gamma_s = gamma_opt     # optimal noise figure
# gamma_s = 0.53*exp(1j*-149*deg_rad)   # uncomment to calculate Noise figure based on gamma_s
gamma_OUT = s22 + s12*s21*gamma_s/(1-s11*gamma_s)   # page 214
gamma_L = conj(gamma_OUT)   # max power transfer
gamma_IN = s11 + s12*s21*gamma_L/(1-s22*gamma_L)    # page 214
print u'\u0393s' + " = %.3f" % abs(gamma_s) + " e^(j*%.1f" % (np.angle(gamma_s)/deg_rad) + ")"   # u'\u0393' = gamma in greek letter
print u'\u0393OUT' + " = %.3f" % abs(gamma_OUT) + " e^(j*%.1f" % (np.angle(gamma_OUT)/deg_rad) + ")"   # u'\u0393' = gamma in greek letter
print u'\u0393L' + " = %.3f" % abs(gamma_L) + " e^(j*%.1f" % (np.angle(gamma_L)/deg_rad) + ")"   # u'\u0393' = gamma in greek letter
print u'\u0393IN' + " = %.3f" % abs(gamma_IN) + " e^(j*%.1f" % (np.angle(gamma_IN)/deg_rad) + ")"   # u'\u0393' = gamma in greek letter

gamma_a = abs((gamma_IN-conj(gamma_s))/(1-gamma_IN*gamma_s))    # p260; 3.8.2
VSWR_in = (1+abs(gamma_a))/(1-abs(gamma_a))
gamma_a = abs((gamma_OUT-conj(gamma_L))/(1-gamma_OUT*gamma_L))    # p260; 3.8.2
VSWR_out = (1+abs(gamma_a))/(1-abs(gamma_a))
print "VSWR_in = %.3f" % abs(VSWR_in)
print "VSWR_out = %.3f" % abs(VSWR_out)

# G_T = G_A when output is conjugate matched
G_T = (1-abs(gamma_s)**2)/abs(1-s11*gamma_s)**2 * abs(s21)**2 * (1-abs(gamma_L)**2)/abs(1-gamma_OUT*gamma_L)**2     # p213; 3.2.2
G_p = 1/(1-abs(gamma_IN)**2) * abs(s21)**2 * (1-abs(gamma_L)**2)/abs(1-s22*gamma_L)**2     # p213; 3.2.3
print "G_T(dB) = G_A(dB) = %.2f" % abs((10*log(G_T, 10)))      # default complex number, use abs() to turn it into normal one
print "G_p(dB) = %.2f" % abs((10*log(G_p, 10)))      # default complex number, use abs() to turn it into normal one
print "G_p(dB); book might have typo in the example or in the formula"

# Noise figure; p299 (4.3.4)
F_min = 10**(F_min/10)  # convert from dB to linear scale
F = F_min + 4*r_n*abs(gamma_s-gamma_opt)**2/((1-abs(gamma_s)**2)*abs(1+gamma_opt)**2)
F = 10*log(F, 10)
print "F(dB) = %.3f" % abs(F)      # default complex number, use abs() to turn it into linear
