import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our data frame is:")
print(df)

# T -> Transposes rows and columns.
print('Transpose of df : ')
print(df.T)
print()
# axes -> Returns a list with the row axis labels and column axis labels as the only members.
print('Axes of df : ')
print(df.axes)
print()
# dtypes -> Returns the dtypes in this object.
print('Data type of df : ')
print(df.dtypes)
print()
# empty -> True if NDFrame is entirely empty [no items]; if any of the axes are of length 0.
print('Is Df Empty?  : ')
print(df.empty)
print()
# ndim -> Number of axes / array dimensions.
print('Ndim of df : ')
print(df.ndim)
print()
# shape ->Returns a tuple representing the dimensionality of the DataFrame.
print('Shape of df : ')
print(df.shape)
print()
# size -> Number of elements in the NDFrame.
print('Size of df : ')
print(df.size)
print()
# values -> Numpy representation of NDFrame.
print('Value of df : ')
print(df.values)
print()
# head() -> Returns the first n rows.
print('head of df : ')
print(df.head(n=3))
print()
# tail() -> Returns last n rows.
print('tail of df : ')
print(df.tail(n=2))
print()