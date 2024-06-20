import pandas as pd
import numpy as np
#  pd.concat(objs,axis=0,join='outer',join_axes=None,ignore_index=False)

one = pd.DataFrame({
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5'],
   'Marks_scored':[98,90,87,69,78]},
   index=[1,2,3,4,5])

two = pd.DataFrame({
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5'],
   'Marks_scored':[89,80,79,97,88]},
   index=[1,2,3,4,5])

print('Original DF one :')
print(one)
print('Original DF two :')
print(two)
print()

print('COncatenated Data Frame : ')
print(pd.concat([one,two]))
print()

print('COncatenated with keys Data Frame : ')
print(pd.concat([one,two], keys=['x','y']))
print()

print('Follow own index     : ')
print(pd.concat([one,two], keys=['x','y'], ignore_index=True))
print()

print('Concatanating nre df as new columns: ')
print(pd.concat([one,two], axis=1))
print()

print()

# Time Series
print('Time Series : \n')
print(pd.Timestamp.now())
print('YYYY-MM-DD : ', pd.Timestamp('2002-01-17'))

print(pd.Timestamp(1587687255,unit='s'))

print (pd.date_range("11:00", "13:30", freq="30min").time)



