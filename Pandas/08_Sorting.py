import pandas as pd
import numpy as np

# Two type of sorting available
# 1) by label
# 2) by actual value

index_list = [0,2,5,8,3,6,9,1,4,7] 
col_list = ['col1','col2']
unsorted_df = pd.DataFrame(np.random.randint(10,100,(10,2)),index=index_list,columns =col_list)
print('Unsorted Data frame : ')
print(unsorted_df)
print()

# By Lable
sorted = unsorted_df.sort_index()
print('After sorting label in ascending : ')
print(sorted)
print()

sorted = unsorted_df.sort_index(ascending=False)
print('After sorting label in descending: ')
print(sorted)
print()

sorted = unsorted_df.sort_index(axis=1)
print('After sorting label with axis=1: ')
print(sorted)
print()

# Sort by values
sorted = unsorted_df.sort_values(by='col1')
print('After sorting by values of cols1 : ')
print(sorted)
print()


sorted = unsorted_df.sort_values(by=['col1', 'col2'])
print('After sorting by values of col1 and col2 both : ')
print(sorted)
print()

# kind -> define the sorting algo
sorted = unsorted_df.sort_values(by=['col1', 'col2'], kind = 'mergesort')
print('After sorting by values of col1 and col2 both : ')
print(sorted)
print()