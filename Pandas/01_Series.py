import pandas as pd
import numpy as np
# series -> 1-D Labeled Array capable of holding data of any type
# pandas.Series( data, index, dtype, copy)  

s = pd.Series()
print('s series : ', s)

data = np.array(['a', 'b', 'c', 'd', 'f'])
s = pd.Series(data)
print('Series od data array :')
print(s)

# specifing index
s = pd.Series(data, index=[100,101,102,103,104])
print('After custom indexing')
print(s)


# Series from dict
data = {'a':1, 'b':2, 'c':3, 'd':4}
s = pd.Series(data)
print('Series from dict : ')
print(s)

# indexing
s = pd.Series(data, index=['d','c','a','b'])
print('After indexing : ')
print(s)

# Series from Scaler
s = pd.Series('Hello',index=[10,20,30,40])
print('Series from scaler : ')
print(s)

# Accessing data of series
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print('Accessing With index : ')
print('s[0] : ',s[0])
print('s[1] : ',s[1])
print('s[2] : ',s[2])

print('Access with label that define in series : ')
print('s[a] : ',s['a'])
print('s[c] : ',s['c'])
print('s[e] : ',s['e'])
print('List of elemnt of a,c,d : ')
print(s[['a','c','d']])
# slicing
print('After slice of [:3] : ')
print(s[:3])

print('last three element : ')
print(s[-3:])





