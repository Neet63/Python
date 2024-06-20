import numpy as np
# broadcasting refers to the ability of NumPy to treat arrays of different shapes during arithmetic operations

# operaton on same shape array
a = np.array([1,2,3,4])
b = np.array([1,2,3,4])

print('same size array : \n' ,(a*b))

# Different size aaray
a = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])

b = np.array([1,2,3])

print('Original arrays:')
print('a :\n',a)
print('b :\n',b)

print('Addition of different shaped aaray : \n', (a+b))