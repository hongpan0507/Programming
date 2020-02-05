from math import pi
W = 1.186e-2
lambda0 = 3e-2
k0 = 2*pi/lambda0

h = 1.588e-3
G1 = W/(120*lambda0)*(1-1/24*(k0*h)**2)
#print(h/lambda0)

print("G1="+str(G1))

