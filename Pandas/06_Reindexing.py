
import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),  # D -> day, M->month, Y->Year
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})

print('Original df : ')
print(df)
print()
#reindex the DataFrame
df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])
print('reindexed df : ')
print(df_reindexed)
print()


# take an object and reindex its axes to be labeled the same as another object
print('Reindexing same as another data frame:')
df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])

df1 = df1.reindex_like(df2)
print(df1)
print()

# Filling
# pad/ffill −> Fill values forward
# bfill/backfill −> Fill values backward
# nearest −> Fill from the nearest index values

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print('Data Frame Without Fill : ')
print(df2.reindex_like(df1))
print()

# Now Fill the NAN's with preceding Values
print("Data Frame with Fill the NAN's with preceding Values:")
print(df2.reindex_like(df1,method='ffill'))

# limit = n -> setting limit of filling rows
print("Data Frame with Fill the NAN's with preceding Values for only 2 rows:")
print(df2.reindex_like(df1,method='ffill', limit=2))
print()
# fillna
df3 = df2.reindex_like(df1,method='ffill', limit=1)
print('Before filling NAN as 0')
print(df3)
print('Afore filling NAN as 0')

print(df3.fillna(0))


# Rename -> to relabel an axis based on some mapping
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print(df1)

print ("After renaming the rows and columns:")
print (df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
                  index = {0 : 'apple', 1 : 'banana', 2 : 'durian'}))



        

