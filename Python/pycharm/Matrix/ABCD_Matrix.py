import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = np.dot(A, B)
print("A * B")
print(C)

D = np.linalg.inv(A)
print("Inverse of A")
print(D)

E = np.dot(D, A)
print("Identity Matrix")
print(E)

F = np.dot(D, C)
print("Extract Matrix B")
print(F)
