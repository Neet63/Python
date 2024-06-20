import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings','kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print("Original Data Frame : ")
print(df)
print()

# obj.groupby('key')
# obj.groupby(['key1','key2'])
# obj.groupby(key,axis=1)

print('Grouped by Teams : ')
print(df.groupby('Team'))
print(df.groupby('Team').groups)
print()


print('Grouped by Teams and Year : ')
print(df.groupby('Team'))
print(df.groupby(['Team','Year']).groups)
print()

print('Iterarating Over group : ')
grouped = df.groupby('Year')

for name,group in grouped:
    print(name)
    print(group)
print()

print('Select a Group : ')
print(grouped.get_group(2015))

print('Aggregration : ')
print(grouped['Points'].agg(np.mean))

print('Other Aggregration : ')
print(grouped['Points'].agg([np.mean, np.sum,np.std]))
print()


print('Transformation : ')
grouped2 = df.groupby('Team')
score = lambda x : (x - x.mean()) / x.std()*10
print(grouped2.transform(score))
print()


print('Filtering : ')
print(grouped2.filter(lambda x:len(x) >=3))
