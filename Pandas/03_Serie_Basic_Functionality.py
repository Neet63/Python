import pandas as pd
import numpy as np

# Create series with 100 random element
s = pd.Series(np.random.rand(100))
print(s)
print()

# axes -> Returns a list of the row axis labels
print('The Axis are : ',s.axes)
print()

# dtype ->  Returns the dtype of the object.
print('Object Data Type : ', s.dtype)
print()

# empty -> Returns True if series is empty.
print('Is series Empty? : ', s.empty)
print()

# ndim -> Returns the number of dimensions of the underlying data
print('Number of Dimensions : ', s.ndim)
print()

# size -> Returns the number of elements in the underlying data.
print('Size of series : ', s.size)
print()

# values -> Returns the Series as ndarray.
print('Value os series : ', s.values)
print()

# head() -> Returns the first n rows. Bydeault n = 5
print('Head : ', s.head())
print('First 10 row : ', s.head(n=10))
print()

# tail() -> Returns the last n rows.
print('Tail : ', s.tail())
print()



