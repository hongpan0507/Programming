# Program function:
# 1. calculate Gamma
# 2. calculate Gain
# 3. calculate VSWR

# Stability condition
#   Unconditionally stable; p217
#       |gamma_s| < 1
#       |gamma_L| < 1
#       |gamma_IN| < 1
#       |gamma_OUT| < 1
#   else all potentially unstable

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
# @ 1GHz
# s11 = 0.770*exp(1j*-166*deg_rad)
# s12 = 0.029*exp(1j*35*deg_rad)
# s21 = 6.11*exp(1j*89*deg_rad)
# s22 = 0.365*exp(1j*-34*deg_rad)
# @ 2GHz
# s11 = 0.760*exp(1j*-174*deg_rad)
# s12 = 0.040*exp(1j*44*deg_rad)
# s21 = 3.06*exp(1j*74*deg_rad)
# s22 = 0.364*exp(1j*-43*deg_rad)
# @ 4GHz
# s11 = 0.756*exp(1j*-179*deg_rad)
# s12 = 0.064*exp(1j*48*deg_rad)
# s21 = 1.53*exp(1j*53*deg_rad)
# s22 = 0.423*exp(1j*-66*deg_rad)

# # book example 3.4.1; page 232; for testing only
# s11 = 0.73*exp(1j*175*deg_rad)
# s12 = 0
# s21 = 4.45*exp(1j*65*deg_rad)
# s22 = 0.21*exp(1j*-80*deg_rad)

# book example 3.4.1; page 232; for testing only
# s11 = 2.27*exp(1j*-120*deg_rad)
# s12 = 0
# s21 = 4*exp(1j*50*deg_rad)
# s22 = 0.6*exp(1j*-80*deg_rad)

# problem 3.7; page 284
# (a)
# s11 = 0.674*exp(1j*-152*deg_rad)
# s12 = 0.075*exp(1j*6.2*deg_rad)
# s21 = 1.74*exp(1j*36.4*deg_rad)
# s22 = 0.6*exp(1j*-92.6*deg_rad)
# (b)
# s11 = 0.385*exp(1j*-55*deg_rad)
# s12 = 0.045*exp(1j*90*deg_rad)
# s21 = 2.7*exp(1j*78*deg_rad)
# s22 = 0.89*exp(1j*-26.5*deg_rad)
# (c)
# s11 = 0.7*exp(1j*-50*deg_rad)
# s12 = 0.27*exp(1j*75*deg_rad)
# s21 = 5*exp(1j*120*deg_rad)
# s22 = 0.6*exp(1j*80*deg_rad)

# problem 3.16; page 287
# s11 = 0.706*exp(1j*-160*deg_rad)
# s12 = 0
# s21 = 5.01*exp(1j*85*deg_rad)
# s22 = 0.508*exp(1j*-20*deg_rad)

# problem 3.17; page 287
s11 = 2.3*exp(1j*-135*deg_rad)
s12 = 0
s21 = 4*exp(1j*60*deg_rad)
s22 = 0.8*exp(1j*-60*deg_rad)

# book example 4.3.1; page 302; for testing only
# s11 = 0.552*exp(1j*169*deg_rad)
# s12 = 0.049*exp(1j*23*deg_rad)
# s21 = 1.681*exp(1j*26*deg_rad)
# s22 = 0.839*exp(1j*-67*deg_rad)
# gamma_opt = 0.475*exp(1j*166*deg_rad)

# book example 4.3.2; page 307; for testing only
# s11 = 0.6*exp(1j*146*deg_rad)
# s12 = 0.085*exp(1j*62*deg_rad)
# s21 = 1.97*exp(1j*32*deg_rad)
# s22 = 0.52*exp(1j*-63*deg_rad)
# gamma_opt = 0.45*exp(1j*-150*deg_rad)
# gamma_s = gamma_opt     # optimal noise figure
# F_min_dB = 3.0   # dB scale
# r_n = 0.2   # given by the problem
# gamma_s = 0.53*exp(1j*-149*deg_rad)

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


# gamma_OUT = s22 + s12*s21*gamma_s/(1-s11*gamma_s)   # page 214; 3.2.6
# gamma_IN = s11 + s12*s21*gamma_L/(1-s22*gamma_L)    # page 214; 3.2.5
# print u'\u0393OUT' + " = %.3f" % abs(gamma_OUT) + " e^(j*%.1f" % (np.angle(gamma_OUT)/deg_rad) + ")"   # u'\u0393' = gamma in greek letter
# print u'\u0393IN' + " = %.3f" % abs(gamma_IN) + " e^(j*%.1f" % (np.angle(gamma_IN)/deg_rad) + ")"   # u'\u0393' = gamma in greek letter
# print "-----------------------------------------------------------------"
#
# M_s = (1 - abs(gamma_s)**2)*(1 - abs(gamma_IN)**2)/abs(1 - gamma_s*gamma_IN)**2  # source mismatch factor; p188; 2.7.17
# M_L = (1 - abs(gamma_L)**2)*(1 - abs(gamma_OUT)**2)/abs(1 - gamma_OUT*gamma_L)**2  # load mismatch factor; p190; 2.7.25
# print "M_s = %.4f" % M_s
# print "M_s(dB) = %.3f" % abs((10*log(M_s, 10)))      # default complex number, use abs() to turn it into normal one
# print "M_L = %.4f" % M_L
# print "M_L(dB) = %.3f" % abs((10*log(M_L, 10)))      # default complex number, use abs() to turn it into normal one
# print "-----------------------------------------------------------------"
#
# # G_T = (1-abs(gamma_s)**2)/abs(1-gamma_IN*gamma_s)**2 * abs(s21)**2 * (1-abs(gamma_L)**2)/abs(1-s22*gamma_L)**2     # p213; 3.2.1
# G_T = (1-abs(gamma_s)**2)/abs(1-s11*gamma_s)**2 * abs(s21)**2 * (1-abs(gamma_L)**2)/abs(1-gamma_OUT*gamma_L)**2     # p213; 3.2.2
# G_p = 1/(1-abs(gamma_IN)**2) * abs(s21)**2 * (1-abs(gamma_L)**2)/abs(1-s22*gamma_L)**2     # p213; 3.2.3
# G_A = (1-abs(gamma_s)**2)/abs(1-s11*gamma_s)**2 * abs(s21)**2 * 1/(1-abs(gamma_OUT)**2)     # p213; 3.2.4
# print "G_T = %.2f" % G_T
# print "G_T(dB) = %.2f" % np.real((10*log(G_T, 10)))      # default complex number
# print "G_p = %.2f" % G_p
# print "G_p(dB) = %.2f" % np.real((10*log(G_p, 10)))      # default complex number
# print "G_A = %.2f" % G_A
# print "G_A(dB) = %.2f" % np.real((10*log(G_A, 10)))      # default complex number
# print "-----------------------------------------------------------------"
#
# P_AVS = E_1**2/(8*np.real(Z_1))     # power available from the source
# P_IN = P_AVS * M_s  # p215; 3.2.7   # power input to the network
# P_L = G_T * P_AVS   # p213; p216; power delivered to the load
# P_AVN = G_A * P_AVS # p213; p216; power available from the network
# print "P_AVS(W) = %.4f" % np.real(P_AVS)
# print "P_IN(W) = %.4f" % np.real(P_IN)
# print "P_L(W) = %.4f" % np.real(P_L)
# print "P_AVN(W) = %.4f" % np.real(P_AVN)
# print "-----------------------------------------------------------------"
#
# gamma_a = abs((gamma_IN-conj(gamma_s))/(1-gamma_IN*gamma_s))    # p260; 3.8.2
# VSWR_in = (1+abs(gamma_a))/(1-abs(gamma_a))
# gamma_b = abs((gamma_OUT-conj(gamma_L))/(1-gamma_OUT*gamma_L))    # p260; 3.8.2
# VSWR_out = (1+abs(gamma_b))/(1-abs(gamma_b))
# print "VSWR_in = %.3f" % abs(VSWR_in)
# print "VSWR_out = %.3f" % abs(VSWR_out)


if s12 != 0:    # bilateral case
    print "Bilateral Case: "
    delta = s11*s22-s12*s21     # page 221
    k = (1-abs(s11)**2-abs(s22)**2+abs(delta)**2)/(2*abs(s12*s21))    # page 221
    print u'\u0394' + " = %.3f" % abs(delta) + " e^(j*%.1f" % (np.angle(delta)/deg_rad) + ")"   # u'\u0394' = delta
    print "k = %.3f" % k
    if k < 1 or abs(delta) > 1:     # potentially unstable
        if k < 1:
            print "(k < 1) --> potentially unstable"
        if abs(delta) > 1:
            print '(|' + u'\u0394' + '|' + " > 1) --> potentially unstable"   # u'\u0394' = delta
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
        print "center (CL) = %.3f" % abs(c_l) + " e^(j*%.1f" % (np.angle(c_l)/deg_rad) + ")"
        print "radius (rL) = %.3f" % r_l
        if abs(s11) > 1:
            print "|s11| > 1"
        elif abs(s11) < 1:
            print "|s11| < 1"
    else:        # unconditionally stable
        print '(k > 1) and (|' + u'\u0394' + '|' + " < 1) --> unconditionally stable"   # u'\u0394' = delta
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
        # print "G_T_max = %.3f" % G_T_max
        # print str(G_T_max)
        print "G_T_max(dB) = G_A_max(dB) = %.2f" % abs((10*log(G_T_max, 10)))     # default complex number, use abs() to turn it into normal one

        # print "Available Power-Gain Circle:"
        # g_a = (1 - abs(gamma_s)**2)/(1 - abs(s22)**2 + abs(gamma_s)**2*(abs(s11)**2-abs(delta)**2) - 2*np.real(gamma_s*C1))  # page 257, equation 3.7.13
        # C_a = g_a*np.conj(C1) / (1 + g_a*(abs(s11)**2-abs(delta)**2))   # equation 3.7.15
        # r_a = (1 - 2*k*abs(s12*s21)*g_a + abs(s12*s21)**2*g_a**2)**0.5 / (abs(1 + g_a*(abs(s11)**2 - abs(delta)**2)))    # equation 3.7.16
        # G_A = abs(s21)**2 * g_a
        # print "G_A(dB) = %.2f" % abs((10*log(G_A, 10)))     # default complex number, use abs() to turn it into normal one
        # print "Center (C_Fi) = %.3f" % abs(C_a) + " e^(j*%.1f" % (np.angle(C_a)/deg_rad) + ")"
        # print "radius (r_Fi) = %.3f" % abs(r_a)
else:   # unilateral case
    print "Unilateral Case: "
    if abs(s11) < 1:     # input stability; unconditionally stable
        print "(|s11| < 1) --> input unconditionally stable"
        print "Input Optimal termination: "
        print u'\u0393s' + " = %.3f" % abs(s11) + " e^(j*%.1f" % (np.angle(np.conj(s11))/deg_rad) + ")"   # u'\u0393' = gamma in greek letter
        G_s_max = 1/(1 - abs(s11)**2)   # p230
        print "G_s_max = %.3f" % G_s_max
        print "G_s_max(dB) = %.3f" % np.real((10*log(G_s_max, 10)))      # default complex number
        print "G_s_max Location = %.2f" % abs(s11) + " e^(j*%.1f" % (np.angle(np.conj(s11))/deg_rad) + ")"   # p232
        G_s_dB = input("G_s(dB) = ")
        G_s = 10**(float(G_s_dB)/10)
        print "G_s = %.3f" % G_s
        g_s = G_s*(1-abs(s11)**2)   # p231, 3.4.9
        print "g_s = %.3f" % g_s
        C_g_s = g_s*np.conj(s11)/(1 - abs(s11)**2*(1 - g_s))    # p231, 3.4.11
        r_g_s = sqrt(1-g_s)*(1-abs(s11)**2)/(1 - abs(s11)**2*(1-g_s))   # p231, 3.4.12
        print "constant input gain circle: "
        print "Center (C_g_s) = %.3f" % abs(C_g_s) + " e^(j*%.1f" % (np.angle(C_g_s)/deg_rad) + ")"
        print "radius (r_g_s) = %.3f" % abs(r_g_s)
    else:     # input stability; potentially unstable
        print "(|s11| > 1) --> input potentially unstable"
        print "To find input impedance, follow example 3.4.2 on page 237"
        gamma_s_c = 1/s11   # p234, 3.4.13
        print "Stability Boundary(" + u'\u0393s_c' + ") = %.2f" % abs(gamma_s_c) + " e^(j*%.1f" % (np.angle(gamma_s_c)/deg_rad) + ")"   # p232
        G_s_dB = input("G_s(dB) = ")
        G_s = 10**(float(G_s_dB)/10)
        G_s_max = G_s   # over-written to calculate G_TU_max
        print "G_s = %.3f" % G_s
        g_s = G_s*(1-abs(s11)**2)   # p231, 3.4.9
        print "g_s = %.3f" % g_s
        C_g_s = g_s*np.conj(s11)/(1 - abs(s11)**2*(1 - g_s))    # p231, 3.4.11
        r_g_s = sqrt(1-g_s)*(1-abs(s11)**2)/(1 - abs(s11)**2*(1-g_s))   # p231, 3.4.12
        print "constant input gain circle: "
        print "Center (C_g_s) = %.3f" % abs(C_g_s) + " e^(j*%.1f" % (np.angle(C_g_s)/deg_rad) + ")"
        print "radius (r_g_s) = %.3f" % abs(r_g_s)

    if abs(s22) < 1:     # output stability; unconditionally stable
        print "(|s22| < 1) --> output unconditionally stable"
        print "Output Optimal termination: "
        print u'\u0393L' + " = %.3f" % abs(s22) + " e^(j*%.1f" % (np.angle(np.conj(s22))/deg_rad) + ")"   # u'\u0393' = gamma in greek letter
        G_L_max = 1/(1 - abs(s22)**2)   # p230
        print "G_L_max = %.3f" % G_L_max
        print "G_L_max(dB) = %.3f" % np.real((10*log(G_L_max, 10)))      # default complex number
        print "G_L_max Location = %.2f" % abs(s22) + " e^(j*%.1f" % (np.angle(np.conj(s22))/deg_rad) + ")"   # p232
        G_L_dB = input("G_L(dB) = ")
        G_L = 10**(float(G_L_dB)/10)
        print "G_L = %.3f" % G_L
        g_L = G_L*(1-abs(s22)**2)   # p231, 3.4.9
        print "g_L = %.3f" % g_L
        C_g_L = g_L*np.conj(s22)/(1 - abs(s22)**2*(1 - g_L))    # p231, 3.4.11
        r_g_L = sqrt(1-g_L)*(1-abs(s22)**2)/(1 - abs(s22)**2*(1-g_L))   # p231, 3.4.12
        print "constant output gain circle: "
        print "Center (C_g_L) = %.3f" % abs(C_g_L) + " e^(j*%.1f" % (np.angle(C_g_L)/deg_rad) + ")"
        print "radius (r_g_L) = %.3f" % abs(r_g_L)
    else:     # output stability; potentially unstable
        print "(|s22| > 1) --> output potentially unstable"
        print "To find output impedance, follow example 3.4.2 on page 237"
        gamma_L_c = 1/s22   # p234, 3.4.13
        print "Stability Boundary(" + u'\u0393s_L' + ") = %.2f" % abs(gamma_L_c) + " e^(j*%.1f" % (np.angle(gamma_L_c)/deg_rad) + ")"   # p232
        G_L_dB = input("G_L(dB) = ")
        G_L = 10**(float(G_L_dB)/10)
        G_L_max = G_L   # over-written to calculate G_TU_max
        print "G_L = %.3f" % G_L
        g_L = G_L*(1-abs(s22)**2)   # p231, 3.4.9
        print "g_L = %.3f" % g_L
        C_g_L = g_L*np.conj(s22)/(1 - abs(s22)**2*(1 - g_L))    # p231, 3.4.11
        r_g_L = sqrt(1-g_L)*(1-abs(s22)**2)/(1 - abs(s22)**2*(1-g_L))   # p231, 3.4.12
        print "constant output gain circle: "
        print "Center (C_g_L) = %.3f" % abs(C_g_L) + " e^(j*%.1f" % (np.angle(C_g_L)/deg_rad) + ")"
        print "radius (r_g_L) = %.3f" % abs(r_g_L)

    # calculate G_TU_max; G_s_max and G_L_max is over-written by stable vale if potentially unstable
    G_o = abs(s21)**2
    print "G_o = %.3f" % G_o
    print "G_o(dB) = %.3f" % np.real((10*log(G_o, 10)))      # default complex number
    G_TU_max = G_s_max * G_o * G_L_max
    print "G_TU_max = %.3f" % G_TU_max
    print "G_TU_max(dB) = %.3f" % np.real((10*log(G_TU_max, 10)))      # default complex number

# # page 304; given a gamma_opt, find gamma_L for max power transfer
# print "minimum noise figure: "
# # gamma_s = gamma_opt     # optimal noise figure
# gamma_OUT = s22 + s12*s21*gamma_s/(1-s11*gamma_s)   # page 214
# gamma_L = conj(gamma_OUT)   # max power transfer
# gamma_IN = s11 + s12*s21*gamma_L/(1-s22*gamma_L)    # page 214
# print u'\u0393s' + " = %.3f" % abs(gamma_s) + " e^(j*%.1f" % (np.angle(gamma_s)/deg_rad) + ")"   # u'\u0393' = gamma in greek letter
# print u'\u0393OUT' + " = %.3f" % abs(gamma_OUT) + " e^(j*%.1f" % (np.angle(gamma_OUT)/deg_rad) + ")"   # u'\u0393' = gamma in greek letter
# print u'\u0393L' + " = %.3f" % abs(gamma_L) + " e^(j*%.1f" % (np.angle(gamma_L)/deg_rad) + ")"   # u'\u0393' = gamma in greek letter
# print u'\u0393IN' + " = %.3f" % abs(gamma_IN) + " e^(j*%.1f" % (np.angle(gamma_IN)/deg_rad) + ")"   # u'\u0393' = gamma in greek letter
#
# gamma_a = abs((gamma_IN-conj(gamma_s))/(1-gamma_IN*gamma_s))    # p260; 3.8.2
# VSWR_in = (1+abs(gamma_a))/(1-abs(gamma_a))
# gamma_a = abs((gamma_OUT-conj(gamma_L))/(1-gamma_OUT*gamma_L))    # p260; 3.8.2
# VSWR_out = (1+abs(gamma_a))/(1-abs(gamma_a))
# print "VSWR_in = %.3f" % abs(VSWR_in)
# print "VSWR_out = %.3f" % abs(VSWR_out)
#
# # G_T = G_A when output is conjugate matched
# G_T = (1-abs(gamma_s)**2)/abs(1-s11*gamma_s)**2 * abs(s21)**2 * (1-abs(gamma_L)**2)/abs(1-gamma_OUT*gamma_L)**2     # p213; 3.2.2
# G_p = 1/(1-abs(gamma_IN)**2) * abs(s21)**2 * (1-abs(gamma_L)**2)/abs(1-s22*gamma_L)**2     # p213; 3.2.3
# print "G_T(dB) = G_A(dB) = %.2f" % abs((10*log(G_T, 10)))      # default complex number, use abs() to turn it into normal one
# print "G_p(dB) = %.2f" % abs((10*log(G_p, 10)))      # default complex number, use abs() to turn it into normal one
# print "G_p(dB); book might have typo in the example or in the formula"
#
# # Noise figure; p299 (4.3.4)
# F_min = 10**(F_min_dB/10)  # convert from dB to linear scale
# F = F_min + 4*r_n*abs(gamma_s-gamma_opt)**2/((1-abs(gamma_s)**2)*abs(1+gamma_opt)**2)
# F = 10*log(F, 10)
# print "F(dB) = %.3f" % abs(F)      # default complex number, use abs() to turn it into linear
