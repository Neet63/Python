import pandas as pd
import numpy as np

# pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,left_index=False, right_index=False, sort=True)

import pandas as pd
left = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
   {'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})


print('Left DF : ')
print(left)
print('Right DF : ')
print(right)
print()

print('Merged Data Frame on id : ')
print(pd.merge(left,right,on='id'))
print()

print('Merge Data Frame on id and subject : ')
print(pd.merge(left,right,on=['id','subject_id']))


# Merge Method	     SQL Equivalent	              Description
# left	             LEFT OUTER JOIN	    Use keys from left object
# right	            RIGHT OUTER JOIN	    Use keys from right object
# outer	             FULL OUTER JOIN	    Use union of keys
# inner	               INNER JOIN	            Use intersection of keys