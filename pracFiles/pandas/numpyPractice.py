# this is a practice file to get familiar with Numpy implementation into pandas

import numpy as np

# single dimensional array
print("Singledimensional array: ")
d = np.array([1, 2, 3, 4, 5])
print(type(d))
print(d)

# multidimensional array
print()
print("-------------")
print("Multidimensional array: ")
dd = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(type(dd))
print()
print(dd)

# print out the shape of the array, and the data type of the "dd" array
print()
print("The shape of both single and multidimensional arrays in that specific order: ")
print("-------------")
print(d.shape)
print(dd.shape)
print(dd.dtype)

# Return a sample (or samples) from the “standard normal” distribution.
print()
print("-------------")
print("Returning a sample from the 'standard normal' distribution: ")
rn = np.random.randn(3, 3)
print(rn)
