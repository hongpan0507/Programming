from __future__ import division     # solve rounding to zero problem
from math import sqrt, pi, exp
from math import log as ln

z_0 = 50    # characteristic impedance
e_r = 30      # relative permittivity

e_r = input('relative permittivity = ')

A = z_0/60*sqrt((e_r+1)/2) + (e_r-1)/(e_r+1)*(0.23+0.11/e_r)
B = 377*pi/(2*z_0*sqrt(e_r))

W_h_ratio1 = 8*exp(A)/(exp(2*A)-2)  # if (W/h) <= 2
W_h_ratio2 = 2/pi*(B-1-ln(2*B-1)+(e_r-1)/(2*e_r)*(ln(B-1)+0.39-0.61/e_r))

if W_h_ratio1 <= 2:
    print 'W/h = %f3' % W_h_ratio1
    sub_h = input('Substrate Height = ')
    print 'W = %f3' % (W_h_ratio1*sub_h)

if W_h_ratio2 >= 2:
    print 'W/h = %f3' % W_h_ratio2
    sub_h = input('Substrate Height = ')
    print 'W = %f3' % (W_h_ratio2*sub_h)


