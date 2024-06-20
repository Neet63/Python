import numpy as np

# shape ->  returns a tuple consisting of array dimensions
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(a.shape)

#resize array with shape
b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.shape)
b.shape = (3,2)
print(b)
print(b.shape)

#resize using reshape
c = b.reshape(2,3)
print(c)

# ndim -> returns the number of array dimensions
d = np.arange(24)
print(d)
print('Dimension of d : ' ,d.ndim)
e = d.reshape(2,3,4)
print(e)
print('Dimension of e : ' ,e.ndim)


# itemsize -> returns the length of each element of array in bytes
print('Item size of e : ',e.itemsize)

# flags -> 
print('flags of e : ', e.flags)


