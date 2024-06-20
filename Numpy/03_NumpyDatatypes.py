# A dtype object is constructed using the following syntax −
# numpy.dtype(object, align, copy)

import numpy as np
dt = np.dtype(np.int32)
print(dt.name)    # print name of datatype
print(dt.kind)    # Character code of datatype
print(dt.itemsize)  # size of Datatype

#int8, int16, int32, int64 can be replaced by equivalent string 
# int8 -> i1
# int16 -> i2
# int32 -> i4

dt2 = np.dtype('i1')
print(dt2) 


# Endian Notation
dt3 = np.dtype('>i4')
print(dt3)

# first create structured data type
dt = np.dtype([('age',np.int8)]) 
print(dt)
#Now apply it to ndarray obj
a = np.array([10,20,30], dtype=dt)
print(a)
print(a.dtype)

# file name can be used to access content of age column 
print(a['age'])


student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
print(student)

a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print(a)
print(a.dtype)
print(a['marks'])

