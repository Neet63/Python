import numpy as np

# list
l1 = [1,2,3,4]
x = np.asarray(l1)
print(x)
print(type(x))

l2 = [4,5,6]
x = np.asarray(l1, dtype=np.float32)
print(x)
print(type(x))

# Set
s1 = (1,2,3)
y = np.asarray(s1)
print(y)

s2 = [(1,2,3),(4,5,6)]
z = np.asarray(s2)
print(z)

# np.frombuffer -> used to create a NumPy array from a buffer object
# numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
s = b'Hello World'
a = np.frombuffer(s, dtype='S1')
print(a)

# numpy.fromiter -> builds an ndarray object from any iterable object
# numpy.fromiter(iterable, dtype, count = -1)

list = range(9)
it = iter(list)

x = np.fromiter(it, dtype=int)
print(x)
x = x.reshape(3,3)
print(x)


