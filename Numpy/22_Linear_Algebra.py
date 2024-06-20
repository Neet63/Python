import numpy as np 

# dot() -> give dot product of 2 array
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
print('a dot b :\n', np.dot(a,b))

#  vdot() -> returns the dot product of the two vectors. If the first argument is complex, then its conjugate is used for calculation. If the argument id is multi-dimensional array, it is flattened.
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
print('a vdot b :\n', np.vdot(a,b))

# inner
a = np.array([1,2,3])
b = np.array([4,5,6])

print('1d inner : \n',np.inner(a,b))

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])
print('nd inner : \n', np.inner(a,b))

# matmul() -> matrix multiplication
a = [[1,0],[0,1]] 
b = [[4,1],[2,2]] 
print('axb : \n',np.matmul(a,b))

#  Determinant
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print('Determinate : ', np.linalg.det(a))

# solve() function gives the solution of linear equations in the matrix form.


# inv -> multiplicative inverse
x = np.array([[1,2],[5,6]])
y = np.linalg.inv(x)
print('Inverse : \n',y)

print(np.dot(x,y))
