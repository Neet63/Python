import numpy as np
import pandas as pd

# Table wise Function Application: pipe()
# Row or Column Wise Function Application: apply()
# Element wise Function Application: applymap()

# pipe()

def adder(n1,n2):
    return n1+n2


df = pd.DataFrame(np.random.randint(1,10,(5,3)),columns=['col1','col2','col3'])
print('Original df :')
print(df)

# adding 2 in whole table
df = df.pipe(adder,2)
print('after adder : ')
print(df)
print()

# apply()
print('Mean of df : ')
print(df.apply(np.mean))
print('Mean of df with axis=1 : ')
print(df.apply(np.mean,axis=1))

# applymap()

# custom function
df['col1'] = df['col1'].map(lambda x:x*100)
print(df)



