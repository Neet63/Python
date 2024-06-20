import numpy as np

# for matrix numpy has follow module
# numpy.matlib

# np.empty(shape, dtype, order)
a = np.empty((2,2))
print('empty : \n',a)

#  zeros
b = np.zeros((3,3))
print('zeors : \n',b)

# ones
c = np.ones((2,2))
print('ones : \n',c)

# np.eye()
d = np.eye(4)
print('eye : \n',d)

# np.identity()
e = np.identity(5,dtype=int)
print('Identity : \n', e)

# rand
f = np.random.rand(2,2)
print('Random : \n',f)

# randint
g = np.random.randint(1,10,(3,3))
print('Randint : \n',g)

