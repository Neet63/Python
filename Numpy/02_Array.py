# way to create nparray

# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# a = np.array([element1, element2,.....])


import numpy as np 
# 1D Array
a = np.array([1,2,3]) 
print(a)
print('a shape : ', a.shape)

# 2D Array
b = np.array([[1,2], [3,4]])
print(b)
print('b shape : ', b.shape)
#ndimn -> define dimension of array
c = np.array([1,2,3], ndmin=2)
print(c)
print('C Shape: ',c.shape)

#dtype -> define datatype of elements
d = np.array([1,2,3], dtype=float)
print(d)
print('d datatype : ',d.dtype)


