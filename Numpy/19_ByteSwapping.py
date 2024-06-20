# numpy.ndarray.byteswap() -> function toggles between the two representations: bigendian and little-endian.
import numpy as np
a = np.array([1,256,8755],dtype=np.int16)

print('Array : \n',a)

print('Representation of data in memory in hexadecimal form:')  
print(map(hex,a))


# byteswap() function swaps in place by passing True parameter 

print('Applying byteswap() function:') 
print(a.byteswap(True)) 

print('In hexadecimal form:') 
print(map(hex,a) )
# We can see the bytes being swapped



