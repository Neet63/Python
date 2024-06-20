# # Create Array
# import array
# obj = array.array(typecode[, initializer])
#   typecode −> The typecode character used to create the array.
#   initializer −> array initialized from the optional value, which must be a list, a bytes-like object, or iterable over elements of the appropriate type.

import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])
print (type(a), a)

# creating an array with char type
a = arr.array('u', 'BAT')
print (type(a), a)

# creating an array with float type
a = arr.array('d', [1.1, 2.2, 3.3])
print (type(a), a)



# 'b': Signed char (1 byte)
# 'B': Unsigned char (1 byte)
# 'u': Unicode character (2 bytes in Python 2, 4 bytes in Python 3)
# 'h': Signed short (2 bytes)
# 'H': Unsigned short (2 bytes)
# 'i': Signed int (4 bytes)
# 'I': Unsigned int (4 bytes)
# 'l': Signed long (4 bytes)
# 'L': Unsigned long (4 bytes)
# 'q': Signed long long (8 bytes)
# 'Q': Unsigned long long (8 bytes)
# 'f': Float (4 bytes)
# 'd': Double (8 bytes)

#Traversal
from array import *
arr1 = array('i', [10,20,30,40,50])
# for x in arr1:
#     print(x)

print('arr1[0] : ', arr1[0])
print('arr1[1] : ', arr1[1])

#Insertion
arr1.insert(0,520)       # arr1.insert(index, value)
print(arr1)

#Deletion
# arr1.remove(40)     # arr1.remove(Value)
# arr1.pop(2)           # arr1.pop(index)
del arr1[5]
print(arr1)

#Searching
print('520 is at index number : ',arr1.index(520))    # arr1.index(value) -> return 1st index of value

#Update
arr1[0] = 0
print(arr1)

#Append
arr1.append(250)
print(arr1)

# Join 2 array
a = array('u', ['a','b','c','d','d'])
b = array('u', ['e','f','g','h'])
a.extend(b)
print(a)

#Copy array
a = array('i', [1,2,3,4,5])
b=a
print('before copy : a : ',id(a), ' b : ', id(b))
a[2] = 36
print(a)
print(b)
print('before copy : a : ',id(a), ' b : ', id(b))

#Making Deep Copy of Array
import copy
b = copy.deepcopy(a)
print('after copy : a : ',id(a), ' b : ', id(b))



#Create an empty array 
d = arr.array('i')
print(type(d),d)
