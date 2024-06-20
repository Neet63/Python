import numpy as np

a = np.arange(10)
print(a)

s = slice(2,7,2)
print(a[s])

b = a[2:7:2]
print(b)

print(a[5:])
print(a[2:6])

b = np.array([[1,2,3]
              ,[4,5,6]])
print(b)
print(b[1:])

a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 

print('Our array is:' )
print(a )
# this returns array of items in the second column 
print('The items in the second column are:'  )
print(a[...,1] )

# Now we will slice all items from the second row 
print('The items in the second row are:' )
print(a[1,...] )

# Now we will slice all items from column 1 onwards 
print('The items column 1 onwards are:' )
print(a[...,1:])