# load() & save() -> handle numPy binary files (with npy extension)
# loadtxt() and savetxt() functions handle normal text files

import numpy as np

# saving np array
a = np.array([1,2,3,4])
np.save('array_a',a)

# loading np array
b = np.load('array_a.npy')
print(b)

# save np array as txt
a = np.array([10,20,30,40])
np.savetxt('a_texted.txt',a)

# load text data
b = np.loadtxt('a_texted.txt')
print(b)


