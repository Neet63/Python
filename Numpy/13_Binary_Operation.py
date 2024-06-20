import numpy as np
#Bitwise AND
a,b = 13,17
print('13 : ', bin(a))
print('17 : ', bin(b))

print('Bitwise and of a nad b : ', np.bitwise_and(a,b))

# Bitwise OR
a,b = 13,17
print('13 : ', bin(a))
print('17 : ', bin(b))

print('Bitwise or of a nad b : ', np.bitwise_or(a,b))

# Bitwise NOT
print('13 : ', bin(a))
print('Bitwise not of 13 : ', np.invert(a))
# uint
print('Botwise not of 13 in uint8')
x = np.array([13], dtype=np.uint8)
y = np.invert(x)
print('13s invert : ', y)

print('Binary of 13 : ', np.binary_repr(13,width=8))
print('Binary of 242 : ', np.binary_repr(242,width=8))


# Left Shift
print('Left shift of 10 by two positions:')
print(np.left_shift(10,2))

print('Binary representation of 10:')
print(np.binary_repr(10, width = 8))

print('Binary representation of 40:')
print(np.binary_repr(40, width = 8) )

#Right shiftt
print('Right shift of 40 by two positions:')
print(np.right_shift(40,2))

print('Binary representation of 40:')
print(np.binary_repr(40, width = 8))

print('Binary representation of 10:')
print(np.binary_repr(10, width = 8) )
