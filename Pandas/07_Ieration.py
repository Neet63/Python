# when we use iteration on pandas object than
# series iterate like array
# data frame iterate like dict

import numpy as np
import pandas as pd

N=20
df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
   })

print('df`s Column name :')
for col in df:
   print(col)

print()

# To ierate over df and iterator give only a view of object so we cant modify it
# iteritems() − to iterate over the (key,value) pairs
# iterrows() − iterate over the rows as (index,series) pairs
# itertuples() − iterate over the rows as namedtuples
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
print('Original Dataframe :')
print(df)
print()
# item()
print('item()')

for key,value in df.items():
   print(key,value)

print()
# iterrows()
print('Iter - row')
for row_index,row in df.iterrows():
   print(row_index,row)
print()

# itertuple()
print('Iter - Tuple')
for row in df.itertuples():
    print(row)


