import pandas as pd
import numpy as np

# DataFrame − “index” (axis=0, default), “columns” (axis=1)

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

#Create a DataFrame
df = pd.DataFrame(d)
print('Original Data frame :')
print(df)

# select_dtype() -> select columns that has dtype that mention in include list
num_df = df.select_dtypes(include=[np.number])
print('Data frame that contain only numbers : ')
print(num_df)

# Sum() -> sum all values column wise
print('Sum of cols : ')
print(df.sum())

print(num_df.sum(1))

# mean() -> give average
print('Mean od columns : ')
print(num_df.mean())

# Standard Deviation
print('Standarad deviation of df : ')
print(num_df.std())

# median() 
print('Median od df : ')
print(num_df.median())

# Mode
print('Mode of df : ')
print(num_df.mode())

# count() -> Number of non-null observations
print('Count of df : ')
print(df.count())

# min() & max()
print('Min and max of df : ')
print(df.min())
print(df.max())

# abs() -> absolute value

# prod() -> product of value
print('Product of value :')
print(num_df.prod())

# cumsum() -> Cumulative Sum
print('Cumilative sum of df : ')
print(df.cumsum())

# cumprod() -> cumilative prod()
print('Cumilative product : ')
print(num_df.cumprod())

# Summarize the data
# describe() -> computes a summary of statistics
#            -> function excludes the character columns and given summary about numeric columns 

print(df.describe())

# includ -> argument which is used to pass necessary information regarding what columns need to be considered for summarizing

print(df.describe(include=['object']))
print(df.describe(include='all'))

