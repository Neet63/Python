import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]]) 
y = x[[0,1,2], [0,1,0]]    
# take pair like (0,0)  ,  (1,1)   and (2,0) as index
print(y)

x = np.array([[0,1,2], 
              [3,4,5],
              [6,7,8],
              [9,10,11]])
print('Original : \n', x)

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[rows, cols]
print('Corner element : \n',y)


z= x[1:4,1:3]
print('After slicing : \n',z)

#  using advanced index for column 
y = x[1:4,[1,2]]
# y = x[1:4,[0,2]]
print('After slicing with advanced indexing : \n',y)


# Boolean Array Indexing
# This type of advanced indexing is used when the resultant object is meant to be the result of Boolean operations, such as comparison operators.

# we will print number greater than 5
b = x[x>5]
print('Numberb >5 in a : \n', b)

c = x[x<4]
print('Number <4 in a : \n', c)



a = np.array([np.nan, 1,2,np.nan,3,4,5]) 
print(a[~np.isnan(a)])


#Filtering COmplex number
a = np.array([[1,2,3+4j],
              [5+10j,6,7],
              [8,9+18j,2]])

b = a[np.iscomplex(a)]
print('Filtering COmplex Number \n',b)


