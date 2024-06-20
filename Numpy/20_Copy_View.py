# When the contents are physically stored in another location, it is called Copy
# a different view of the same memory content is provided, we call it as View.

import numpy as np

a = np.arange(6)

print('Original Array : \n', a)
print('Id of a : ',id(a))

b=a
print('assigning a to a and bs id : ', id(b))

print('change the shape of b')
b.shape = (3,2)
print('It also change shape of a')
print('a shape : ', a)

# View or shallow copy
x = np.arange(6).reshape(3,2)

print('Array a : \n', x)

print('Create a view : ')
y = x.view()
print(y)
print('id of bothe array are diffrenet: ')
print('id of x : ', id(x))
print('id of y : ', id(y))

# changing shape of y doesnt change shape of x
y.shape = (2,3)
print('y : ',y)
print('x : ',x)

# slicing of array create a view
a = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
print('Original \n', a)

print('Create a slice : ')
s = a[:,:2]
print('sliced: \n', s)


# Deep Copy
# np.copy() create a deep copy
a = np.array([[10,20,30],
              [-20,-50,-70],
              [50,60,-80]])

print('Original Array : \n',a)
print('Id of a : ', id(a))

# Create deep copy of a
b = a.copy()
# b = np.copy(b)

print('Id of b : ', id(b))

b[0,0] = 2000
print(b)
print()
print(a)

