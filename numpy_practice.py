# -*- coding: utf-8 -*-
"""numpy_practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1peVFNOT0S4rhLIswRejibPgN_YbfwayI
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
# %matplotlib inline

# How to create array A of size 15, with all zeros?
A = np.zeros(15)

# How to find memory size of array A?
A.size * a.itemsize

# How to create array B with values ranging from 20 to 60?
B = np.arange(20,61)

# How to create array C of reversed array of B?
C = B[::-1]

# How to create 4×4 array D with values from 0 to 15 (from top to bottom, left to right)?
D = np.arange(16).reshape(4,4)

# How to find the dimensions of array E [[3, 4, 5], [6, 7, 8]]?
E = np.array([[3, 4, 5], [6, 7, 8]])
E.shape

# How to find indices for non-zero elements from array F [0, 3, 0, 0, 4, 0]?
F = np.array([0, 3, 0, 0, 4, 0])
F.nonzero()

# How to create 3×3×3 array G with random values?
G = np.random.random((3,3,3))

# How to find maximum values in array H [1, 13, 0, 56, 71, 22]?
H = np.array([1, 13, 0, 56, 71, 22])
H.max()
H.min()
np.mean(H)
np.std(H)
np.median(H)

# How to transpose array D?
Dt = D.T

# How to append array [4, 5, 6] to array I [1, 2, 3]?
I = np.array([1,2,3])
I = np.concatenate((I,np.array([4,5,6])))

# How to member-wise add, subtract, multiply and divide two arrays J [1, 2, 3] and K [4, 5, 6]?
J = np.array([1,2,3])
K = np.array([4,5,6])
J + K
J - K
J * K
J / K

# How to find the total sum of elements of array I?
np.sum(I)

# How to find natural log of array I?
np.log(I)

# How to use build an array L with [8, 8, 8, 8, 8] using full/repeat function?
L = np.full(5,8)
L = np.repeat(8,5)

# How to sort array M [2, 5, 7, 3, 6]?
M = np.array([2, 5, 7, 3, 6])
np.sort(M)

# How to find the indices of the maximum values in array M?
M.argmax()

# How to find the indices of the minimum values in array M?
M.argmin()

# How to find the indices of elements in array M that will be sorted?
M.argsort()

# How to find the inverse of array N = [[6, 1, 1], [4, -2, 5], [2, 8, 7]] in numpy?
N = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
np.linalg.inv(N)

# How to find absolute value of array N?
np.abs(N)

# How to extract the third column (from all rows) of the array O [[11, 22, 33], [44, 55, 66], [77, 88, 99]]?
O = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
O[:,2]

# How to extract the sub-array consisting of the odd rows and even columns of P [[3, 6, 9, 12], [15,18, 21, 24], [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]]?
P = np.array([[3, 6, 9, 12], [15,18, 21, 24], [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])
P[::2,1::2]