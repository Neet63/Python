import numpy as np
import pandas as pd

# Aggregation in pandas refers to the process of performing summary statistics on data, such as computing the mean, sum, count, or other aggregate values. 

df = pd.DataFrame(np.random.randint(1,10,(10, 4)),
                  index = pd.date_range('1/1/2000', periods=10),
                  columns = ['A', 'B', 'C', 'D'])

print('Original Data Frame : ')
print(df)
print()

r = df.rolling(window=3, min_periods=1)
print('After rolling:')
print(r)

# agg() and aggration() -> both same
s = r.aggregate(np.sum)
# s = r.agg(np.sum)
print('After aggrated sum : ')
print(s)

print()
print('Sum of column A : ')
print(r['A'].agg(np.sum))
print()

print('Sum of column A and B : ')
print(r[['A', 'B']].agg(np.sum))
print()

print('Sum and Mean of Column A : ')
print(r['A'].agg([np.sum,np.mean]))
print()

print('Sum of A and  Mean of  B : ')
print(r.agg({'A':np.sum, 'B':np.mean}))
print()
