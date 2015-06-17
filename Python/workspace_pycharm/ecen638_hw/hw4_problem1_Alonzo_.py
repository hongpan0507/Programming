
__author__ = 'Alonzo'
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integ

pi = np.pi
eta = 377
c = 3e8
f = 280e6
e0 = 8.854e-12
w = 2*np.pi*f
x = c/f
L = 0.5
j = complex(0, 1)
N = 51
M = N
seg = np.linspace(0, N, N)
delta_z = L/N
a = 1e-3
B = 2*np.pi/x
const = 1/(j*w*e0*4*pi)
Z_mn = []
theta_array = np.linspace(0, 2*pi, N)
# rmn values and Z values
def f_real(z_m, z_n_prime):
    r_mn = np.sqrt(a**2+(z_m-z_n_prime)**2)
    complex = const*(np.cos(B*r_mn)-j*np.sin(B*r_mn))*((1+j*B*r_mn)*(2*r_mn**2-3*a**2)+(B*r_mn*a)**2)/r_mn**5
    return complex.real

def f_imag(z_m, z_n_prime):
    r_mn = np.sqrt(a**2+(z_m-z_n_prime)**2)
    complex = const*(np.cos(B*r_mn)-j*np.sin(B*r_mn))*((1+j*B*r_mn)*(2*r_mn**2-3*a**2)+(B*r_mn*a)**2)/r_mn**5
    return complex.imag

for m in range(0, M):
    for n in range(0, N):
        F_real = integ.nquad(f_real, [[-L/2+m*delta_z, -L/2+(m-1)*delta_z], [-L/2+n*delta_z, -L/2+(n-1)*delta_z]])
        F_imag = integ.nquad(f_imag, [[-L/2+m*delta_z, -L/2+(m-1)*delta_z], [-L/2+n*delta_z, -L/2+(n-1)*delta_z]])
        Z = F_real[0]+j*F_imag[0]
        Z_mn.append(Z)

Z_mn = -1*np.matrix(Z_mn).reshape(M, N)

X = Z_mn.imag
R = Z_mn.real
D = np.linalg.inv(R)*X
e_val_n, J_n = np.linalg.eig(D)
#print(J_n)
#print(e_val_n)

# Normalize Eigencurrent
J_nn = np.zeros([N, N])
for i in range(N):
    J_nn[i, :] = np.transpose(J_n[:, i])/np.sqrt(np.inner(np.transpose(J_n[:, i]), np.transpose(R*J_n[:, i])))
J_nn = np.matrix(J_nn)
#print(J_nn)

#  Check for Orthonormal set
IP = np.zeros([N, N])
for i in range(N):
    for k in range(N):
        IP[i, k] = np.inner(J_nn[i], np.transpose(R*np.transpose(J_nn[k])))
IP = np.matrix(IP)
#print(IP)

# Characteristic Fields
#E_n = R*J_nn*(1+j*e_val_n)
#E_n = Z_mn*np.transpose(J_nn[N-2])
#E_n = R*J_n+j*X*J_n
#print(np.abs(E_n))

plt.figure(1)
ax1 = plt.subplot(111)
ax1.plot(seg, np.transpose(J_nn[N-1])/np.max(J_nn[N-1]), color='black')
ax1.plot(seg, np.transpose(J_nn[N-2]/np.max(J_nn[N-2])), color='red')
ax1.plot(seg, np.transpose(J_nn[N-3]/np.max(J_nn[N-3])), color='green')
ax1.plot(seg, np.transpose(J_nn[N-4]/np.max(J_nn[N-4])), color='blue')
ax1.set_title("Eigencurrents")

#plt.figure(2)
#plt.polar(theta_array, E_n, color='black')

plt.show()

