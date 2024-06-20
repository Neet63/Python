import numpy as np

# Sorting
# numpy.sort(a, axis, kind, order)
# a -> array,  axis -> along which axis to sort, 
# kind -> type of sorting by default quick,  order -> If the array contains fields, the order of fields to be sorted

a = np.array([[2,10,1],[5,4,2]])
print('Original Array : \n',a)
print('After Sort : \n', np.sort(a))

print('Sort along axis 0 :\n', np.sort(a,axis=0))

# Order Parameter in function
dt = np.dtype([('name','S10'), ('age',int)])
b = np.array([('Raju',15),('Shayam',30),('Aryan',25)], dtype=dt)

print('Original Array : \n',b)

print('Ordered by name :\n', np.sort(b,order='name'))
print('Ordered by age :\n', np.sort(b,order='age'))


# argsort() -> function returns the indices that would sort an array.
a = np.array([5,4,3,2,1])
print('Original Array : \n',a)
print("After argsort() this is indices of sorted order: \n", np.argsort(a))

y = np.argsort(a)
print('Sorted Array : \n', a[y])

# Reconstruct original array using loop
for i in y:
    print(a[i], end=(' '))

print()
# lexsort() -> sort by sequences key and last key is primary and second last after that and so on
#  for example -> below first it will sort by name and than by dv
name = ('raju','aman', 'jaimin','aarav','aarav')
dv = ('f.y', 's.y', 's.y', 's.y','f.y')
ind = np.lexsort((dv,name))  

print('After Lexsort() : ',ind)
print( 'Use this index to get sorted data:' )
print([name[i] + ", " + dv[i] for i in ind] )


# argmax() -> return index of maximum element respectively give along axis
# argmin() -> return index of minimum element respectively give along axis

a = np.array([[50,20,10],
              [90,40,30],
              [0,60,80]])

print('Index of Maximum element in a : ', np.argmax(a))
print('Index of Minimum element in a : ', np.argmin(a))


print('Index of Maximum element in a with axis 0: ', np.argmax(a, axis=0))
print('Index of Minimum element in a with axis 0: ', np.argmin(a, axis=0))

print('Index of Maximum element in a with axis 1: ', np.argmax(a, axis=1))
print('Index of Minimum element in a with axis 1: ', np.argmin(a, axis=1))


# nonzero() ->  Finds indices of non-zero elements.
x = np.array([[0,0,2],
              [5,0,0],
              [0,1,0,]])

print('Index of nozero element : ', np.nonzero(x))


# where() -> same as if-else but returns index
x = np.arange(9.).reshape(3,3)
print('Original Array : \n',x)

y = np.where(x>3)
print('Index of element > 3: ',y)

print('Printing those element : ', x[y])

# extrct() -> returns the elements satisfying any condition

# conditions:
c = np.mod(x,3)==0
print('Element wise value of condition : \n', c)

print('Extract those element : ', np.extract(c,x))