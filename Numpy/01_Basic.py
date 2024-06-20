# Import numpy
import numpy as np

# Create Numpy array
a = np.array([1,2,3,4,5])   # 1D
b = np.array([[1,2,3,4], [4,5,6,7]])   #2D
c = np.array([i for i in range(10)])   #  loop

print(a.shape)
print(b.shape)
print(c.shape)

print(type(a))
print(type(b))
print(type(c))