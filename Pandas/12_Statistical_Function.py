import pandas as pd
import numpy as np

# Percentage Change
s = pd.Series([1,2,16,8,0])
print('Orifinal Series : ')
print(s)

print('Percentage Change Series : ')
print(s.pct_change())

df = pd.DataFrame(np.random.rand(5,2))
print('Original Dataframe : ')
print(df)

print('Percentage change of df : ')
print(df.pct_change())
print()
print()

# Covariance
print('Covariance : ')
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([2,4,6,8,10])
print('COvariance of s1 and s2 : ', s1.cov(s2))

# in df computes cov between all the columns.
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print(frame['a'].cov(frame['b']))
print(frame.cov())
print()
print()

# Correlation
print('Cor-Relation ')
df = pd.DataFrame(  np.random.randn(10,5),
                  columns=['A','B','C','D','E'])

print('Original Dataframe : ')
print(df)
print()

print('Correlation of column A to B : ',  df['A'].corr(df['B']))

print('Correlation of column A to A : ',  df['A'].corr(df['A']))
print()
print()


# DataRanking -> produces ranking for each element in the array of elements. In case of ties, assigns the mean rank.

print('Data Ranking : ')

# Create a sample DataFrame with student names and scores
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve','Franklin'],
        'Score': [85, 92, 50, 78, 95,78]}
df = pd.DataFrame(data)
# Add a 'Rank' column with default ranking (ascending order)
print('Ascending Order : ')
df['Rank'] = df['Score'].rank()
print(df)


# Add a 'Rank' column with default ranking (descending order)
print('Descending Order : ')
df['Rank'] = df['Score'].rank(ascending=False)
print(df)


