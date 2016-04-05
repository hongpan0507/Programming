from numpy import sin
from math import pi
import numpy as np
from matplotlib import pyplot as plt

xs = np.linspace(-pi, pi, 30)
ys = sin(xs)
markers_on = [0, 17, 14, 29]

plt.figure(1)
plt.plot(xs, ys, 'g-')
plt.plot(xs[markers_on], ys[markers_on], 'rD')

plt.show()

# or using plt.scatter; look into lab6 for more info

