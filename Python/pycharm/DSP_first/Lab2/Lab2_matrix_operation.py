# python 3.5
# 02/25/2017
# lab 2

import numpy as np
from matplotlib import pyplot

x = np.array([2, 3, 1, 0])  # row
y = np.array([[2], [3], [1], [0]])  # column

# debug
print("x =")
print(x)
print("y =")
print(y)

print("x dot y =")
print(np.dot(x, y))     # matrix multiplication
