__author__ = 'hpan'

from scipy.integrate import quad


#----------------intergration
def integrand(x, a, b):
   return a * x + b

a = 2
b = 1
I = quad(integrand, 0, 1, args=(a,b))
print(I)

import numpy as np
import matplotlib.pyplot as pyplot
import cmath
from custom_func import *
from scipy.integrate import quad
from scipy.integrate import nquad
from scipy.integrate import dblquad
from math import sin
from math import cos
from math import atan

pi = math.pi
mu_0 = 4*pi*1e-7    #permeability
epsilon_0 = 1e-9/(36*pi)    #permitivity
eta = 120*pi    #intrinsic impedance
dB_Np = 20/math.log(10,math.exp(1))     # 8.68 db per Np
#-----------------------------------------------------------


#------------------------np.linsapce
print("np.linspace")
resolution = 100
E_theta_r = np.zeros(resolution)
theta_array = np.linspace(0, pi, resolution)
print(theta_array[99])
i = 0
while i < np.size(E_theta_r):
    E_theta_r[i] = 1
    i+=1

#pyplot.polar(theta_array, E_theta_r)
#pyplot.show()

#-------print()
test = 111.1 - 22.2222j
print('original = %02f - %02fj' %(test.real, test.imag*-1))
print('real part = %f' %test.real)
print('imag part = %f' %test.imag)
print('magnitude = %f' %abs(test))

test2 = cmath.polar(test)
mag = abs(test)
pha = cmath.phase(test)
print('mag = %f' %mag)
print('phase = %f' %pha)
print('in polar form = ', test2)

test3 = cmath.exp(2*1j)
print('mag = %f' %abs(test3))
print('phase = %f' %cmath.phase(test3))

def test(x):
   return x**2


integrate = quad(test,1,2)
print('integrate = %f' %integrate[0])

test_array = np.arange(1,2,0.01)
i = 0
integrate2 = 0
while i < np.size(test_array):
    integrate2 = integrate2 + (test_array[i])**2 * 0.01
    i += 1
print('integrate2 = %f' %integrate2)

integrate3 = (2-1)*test((2+1)/2)
print('integrate3 = %f' %integrate3)

integrate4 = (2-1)*(test(1) + test(2))/2
print('integrate4 = %f' %integrate4)

i = 0
integrate5 = 0
while i < 100000:
    integrate5 = integrate5 + test(1+i*(2-1)/100000)
    i += 1

integrate5 = integrate5 + test(2)/2 + test(1)/2
integrate5 = integrate5*(2-1)/100000
print('integrate5 = %f' %integrate5)


test_array = ([1,4],[2,5],[3,6])
print(test_array[1][1])

test_array = np.zeros(5)
for num in range(0, np.size(test_array)):
    test_array[num] = 2

print(test_array)

test = lambda x: (sin(x))**2
integrate1 = quad(test,0,pi)
print('integrate1 = %f' %integrate[0])


test = lambda x: sin(x)
integrate2 = quad(test,0,pi)
result = (integrate2[0])**2
print('integrate2 = %f' %result)

test = 1/(2j)
print('real part = %f' %test.real)
print('imag part = %f' %test.imag)
print(abs(test))

#-------------------double integration
def test(y,x):
    return x*y
a = dblquad(test, 0,2, lambda y:0, lambda y:3)
print(a)

#--------------------n integration
print("nquad")
def test(x,y):
    return (x**2)*y
a = nquad(test, [[0,2],[0,3]])
print(a)

for i in range(0,5):
    print(i)

#-----------------------max in array
print("Max in array")
a = np.array([[1,4],[2,5],[3,6]])
print(a.max())
b = []
b.append(1)
b.append(2)
b.append(3)
b= np.reshape(b,(1,3))  #change from list to array
b = b/b.max()
print(b)

#----------------------add 2 arrays
from operator import add
print("Add two arrays")
test_array1 = np.array([[1,4],[2,5],[3,6]])
test_array2 = np.array([[1,4],[2,5],[3,6]])
test_array3 = test_array1 + test_array2
test_array4 = np.zeros([3,2])
test_array5 = test_array3+ test_array4
test_array5 = test_array5/2
print(test_array5)

#----------------------invert matrix
from numpy.linalg import inv
print("invert matrix")
test_array1 = np.array([[1,4,3],[2,5,3],[3,6,4]])
test_array2 = (test_array1)^-1
test_array3 = inv(test_array1)
print(test_array1)
print(test_array2)
print(test_array3)

#----------------------matrix multiplication
print("matrix multiplication")
test_array1 = np.array([1,4,3])
test_array2 = test_array1 * test_array1
test_array3 = test_array1.dot(test_array1)
print(test_array1)
print(test_array2)
print(test_array3)
a = np.size(test_array1)
print(a)

#---------------------- inverse tangent
print("inverse tangent")
tan = math.atan(1)*180/pi
print(tan)
