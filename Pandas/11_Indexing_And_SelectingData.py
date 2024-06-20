import pandas as pd
import numpy as np

# 1).loc()  -> Label based
# 2).iloc() -> Integer based
# 3).ix()   -> Both Label and Integer based -> deprecate dafter 0.20.0 version


df = pd.DataFrame(np.random.randint(1,20,(8, 4)),
                  index = ['a','b','c','d','e','f','g','h'], 
                  columns = ['A', 'B', 'C', 'D'])

print('Original loc df : ')
print(df)
print()

# loc()
print('all rows of a specific column:')
print(df.loc[:,'A'])

print('all rows of a specific multiple columns : ')
print(df.loc[:,['A','D']])

print('specific rows of specific columns : ')
print(df.loc[['a','c','e','g'], ['A','D']])

print('all colums for specific rows : ')
print(df.loc['a':'d'])

print('for getting value with a boolean array of some condition: ')
print('Is number gretter than 10 : ')
print(df.loc['a']>10)   # here condition is -> value > 10
print()
print()



# iloc()
df = pd.DataFrame(np.random.randint(1,20,(8, 4)),
                  columns = ['A', 'B', 'C', 'D'])

print('Original iloc df : ')
print(df)

print('All columns of specified rows : ')
print(df.iloc[:4])    

print('Slicing : ')
print(df.iloc[1:4, 1:3])

print('Slicing throudh list of indexes : ')
print(df.iloc[[0,1,2],[2,3]])   # will amke pair like (0,2),(0,3),(1,2),(1,3) etc

print('slice like [1:3] row and all cols : ')
print(df.iloc[1:3, :])
print()
print()

