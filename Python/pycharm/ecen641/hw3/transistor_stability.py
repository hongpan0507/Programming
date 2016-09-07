from cmath import exp
from cmath import polar
import numpy as np


pi = 3.14156
deg_rad = pi/180

# book example 3.3.1; page 222; for testing only
# @ 500MHz
# s11 = 0.761*exp(1j*-151*deg_rad)
# s12 = 0.025*exp(1j*31*deg_rad)
# s21 = 11.84*exp(1j*102*deg_rad)
# s22 = 0.429*exp(1j*-35*deg_rad)

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

s11 = 0.75*exp(1j*-116*deg_rad)
s12 = 0.01*exp(1j*67*deg_rad)
s21 = 3.5*exp(1j*64*deg_rad)
s22 = 0.77*exp(1j*-65*deg_rad)

delta = s11*s22-s12*s21     # page 221
k = (1-abs(s11)**2-abs(s22)**2+abs(delta)**2)/(2*abs(s12*s21))    # page 221

print "delta = %.3f" % abs(delta) + " e^(j*%.1f" % (np.angle(delta)/deg_rad) + ")"

# print "delta = " + str(abs(delta)) + " e^(j*" + str(np.angle(delta)/deg_rad) + ")"


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


# problem 3.16 part b; page 287
s11 = 2.3*exp(1j*-135*deg_rad)
g_i = -10.8

# input G circle
c_g = g_i*np.conj(s11)/(1-abs(s11)**2*(1-g_i))
r_g = np.sqrt(1-g_i)*(1-abs(s11)**2)/(1-abs(s11)**2*(1-g_i))

print "Input G circle parameter:"
print "center (Cg) = %.3f" % abs(c_g) + " e^(j*%.1f" % (np.angle(c_g)/deg_rad) + ")"
print "radius (rg) = %.3f" % r_g
