import numpy as np

# creates an uninitialized array of specified shape and dtype
# numpy.empty(shape, dtype = float, order = 'C')
x = np.empty([3,2], dtype = int)
print(x)
print(x.shape)

# Create array with all element with zero
# numpy.zeros(shape, dtype = float, order = 'C')
y = np.zeros([3,3],dtype=int)
print(y)
print(y.shape)
# Custom Type
x = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])
print(x)
print(x.shape)

# Create array with all element with one
# numpy.ones(shape, dtype = float, order = 'C')
z = np.ones([2,2],dtype=int)
print(z)
print(z.shape)

# Identity Matrix
w = np.eye(3)
print(w)
