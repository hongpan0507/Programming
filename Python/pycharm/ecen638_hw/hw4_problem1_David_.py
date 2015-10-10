#David Grayson
#ECEN 638 HW3
#Problem 2

from scipy import integrate
from numpy import linalg as LA
import numpy as np
import cmath
import math
import matplotlib.pyplot as pyplot


N1 = 51 #51 #Number of segments
Z0 = 75 #Line Impedance
f0 = 280e6 #frequency
lam = 3e8/f0 #wavelength
a = 0.0005 #wire radius [m]
L = 0.5 #wire length [m]
dz1 = L/N1 #segment length

##Get center-points of each segment
zn1 = np.zeros(N1)
for i in range(N1):
    zn1[i] = -L/2 + dz1/2 + (i*dz1)

def r(z1,z2):
    return np.sqrt(a**2 + (z1-z2)**2)

k = 2*np.pi/lam

C = (-1j*120*lam)/(8*np.pi)

def f1i(z1,z2):
    return (C*cmath.exp(-1j*k*r(z1,z2))*(((1+1j*k*r(z1,z2))*(2*r(z1,z2)**2-3*a**2))+(k*a*r(z1,z2))**2)/(r(z1,z2)**5)).imag

#def f2i1(z2,z1):
#    return integrate.quad(f1i,z1-dz1/2,z1+dz1/2,args=(z2))[0]

def f1r(z1,z2):
    return (C*cmath.exp(-1j*k*r(z1,z2))*(((1+1j*k*r(z1,z2))*(2*r(z1,z2)**2-3*a**2))+(k*a*r(z1,z2))**2)/(r(z1,z2)**5)).real

#def f2r1(z2,z1):
#    return integrate.quad(f1r,z1-dz1/2,z1+dz1/2,args=(z2))[0]

Zmn1 = []

for i in range(N1):
    for p in range(N1):
        #progress = 'Computing Z '+repr(i+1)+' , '+repr(p+1)+' for N = '+repr(N1)+', f = '+repr(f[q])
        #print(progress)
        #Zi1 = integrate.quad(f2i1,zn1[i]-dz1/2,zn1[i]+dz1/2,args=(zn1[p]))[0]
        #Zr1 = integrate.quad(f2r1,zn1[i]-dz1/2,zn1[i]+dz1/2,args=(zn1[p]))[0]
        Zi1 = integrate.nquad(f1i,[[zn1[p]-dz1/2,zn1[p]+dz1/2],[zn1[i]-dz1/2,zn1[i]+dz1/2]])[0]
        Zr1 = integrate.nquad(f1r,[[zn1[p]-dz1/2,zn1[p]+dz1/2],[zn1[i]-dz1/2,zn1[i]+dz1/2]])[0]
        Z1 = Zr1 + 1j*Zi1
        Zmn1.append(Z1)

Zmn1 = np.matrix(Zmn1).reshape(N1,N1)

# np.savetxt("z_mn_real.csv",z_mn.real,delimiter=",")
# np.savetxt("z_mn_img.csv",z_mn.imag,delimiter=",")

V1 = np.zeros(N1)
V1 = np.matrix(V1).reshape(N1,1)

V1[(N1/2)-0.5,0] = 1

An1 = -LA.inv(Zmn1)*V1

# possibly missed this step somewhere above (corrects to have positive real power radiated)
Zmn1 = -Zmn1 #Zmn1

# compute eigencurrents
ln_bw, Jn_bw = LA.eig(LA.inv(Zmn1.real)*Zmn1.imag)


pyplot.figure(1)
pyplot.title('hw 4 prob 1; frequency = 280MHz; N = 101')
pyplot.xlabel('Segments')
pyplot.ylabel('Eigen Currents (Jn)')
pyplot.plot(zn1, Jn_bw[:,N1-1], color = 'red', label="J1")
pyplot.plot(zn1, Jn_bw[:,N1-2], color = 'blue', label="J2")
pyplot.plot(zn1, Jn_bw[:,N1-3], color = 'green', label="J3")
pyplot.plot(zn1, Jn_bw[:,N1-4], color = 'black', label="J4")
pyplot.legend(loc='upper right', shadow=True)

pyplot.show()


