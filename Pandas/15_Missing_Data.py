import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1,20,(5, 3)), 
                  index=['a', 'c', 'e', 'f','h'],
                  columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print('Original Data Frame with missing values: ')
print(df)
print()

print('Null Values : ')
print(df.isnull())
print()

print('Number of Null Values in each colums : ')
print(df.isnull().sum())
print()

print('Not null : ')
print(df['one'].notnull())
print()


# filling/cleaning missing value
print('Filling NAN with 0')
# df = df.fillna(0)
print(df.fillna(0))


# Fill NA Forward and backward

# i cell value to (i+1) if (i+1) is NAN
print('Forward Filling :')
print(df.fillna(method='pad'))
print()

# i cell value to (i-1) if (i-1) is NAN
print('Backward Filling : ')
print(df.fillna(method='bfill'))
print()

# drapna -> drop missing values rows
print('Dropping Missing value rows')
print(df.dropna())
print()

print('Dropping Missing value columns')
print(df.dropna(axis=1))
print()

# Replace Missing or Generic value 
df = pd.DataFrame({'one':[10,20,30,40,50,2000], 'two':[1000,0,30,40,50,60]})

print(df.replace({1000:10,2000:60}))

