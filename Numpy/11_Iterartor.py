import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)

print('Original array is:')
print(a)

print('Modified array is:')
for x in np.nditer(a):
   print(x, '  ',end='')
print()    

# Transpose
a = np.arange(0,60,5)
a = a.reshape(3,4)
b = a.T
print(b)


print('Sorted in C-style order:')
c = b.copy(order = 'C')
# or use below
print(c)
for x in np.nditer(c):
   print (x,'  ',end='')

print('\n')

print('Sorted in F-style order:')
c = b.copy(order = 'F')
print(c)
for x in np.nditer(c):
   print(x,' ' ,end='')

print()

# Other Way using nditer
print ('Sorted in C-style order:')
for x in np.nditer(a, order = 'C'): 
   print (x, end=' ')
print()

print ('Sorted in F-style order:' )
for x in np.nditer(a, order = 'F'): 
   print (x,end=' ')

# Modify Array Value
# op_flags. Its default value is read-only, but can be set to read-write or write-only mode. 
# This will enable modifying array elements using this iterator.
print()
for x in np.nditer(a, op_flags=['readwrite']):
   x[...] = 2*x

print('Mofidied array : \n', a)
