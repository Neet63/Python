# Dataframe(df) -> two-dimensional data structure
# pandas.DataFrame( data, index, columns, dtype, copy)

import pandas as pd
import numpy as np

# Empty DataFrame
df = pd.DataFrame()
print('Empty Dataframe : ', df)

# list
data = [10,20,30,40]
df = pd.DataFrame(data)
print('List to df : ')
print(df)

data = [['alex',10],['Ben',30],['Charls',70],['Danny',60],['Earl',20]]
df = pd.DataFrame(data)
print('List to df : ')
print(df)

# give name to colums
df = pd.DataFrame(data, columns=['name','age'])
print('List to df after naming cols : ')
print(df)

# dict to df
data = {'Name' : ['alex', 'Benjimin', 'Choi','Dan'], 'Age':[10,30,50,20]}
df = pd.DataFrame(data)
print('Dict to Dataframe : ')
print(df)

# Indexing
df = pd.DataFrame(data, index=['a','b','c','d'])
print('Dict to Dataframe Indexing : ')
print(df)


# Df from list of dict
print('list of dict to df : ')
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)


data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df1)
print(df2)


# Column Selection
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df['one'])

# Adding a new column to an existing DataFrame object with column label by passing new series

print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)

print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']

print(df)

# column Deletion
# using del
del(df['one'])
print('After deleting one column')
print(df)

# pop
df.pop('two')
print('After deleting two column')
print(df)


# Row selection, addition and deletion
print('Row Selection')
df = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

print(df )
df = pd.DataFrame(d)
print(df.loc['b'])

print(df[2:4])

# ?Add row
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

print('Concated 2 df')
df = pd.concat([df, df2], ignore_index=True)
print(df)

df = df.drop(0)
print('Deleted First row')
print(df)

