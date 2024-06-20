import pandas as pd
import numpy as np


s = pd.Series(["a","b","c","a"], dtype="category")
print(s)
print()

# to create categorical object 
# pandas.Categorical(values, categories, ordered)
print('Categorical Object : ')
cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print(cat)
print()

print('If element outsite category than it will represented as NAN : ')
cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
print(cat)
print()


print('describr() -> get similar output to a Series or DataFrame of the type string.')
cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
df = pd.DataFrame({"cat":cat, "s":["a", "c", "c", np.nan]})

print (df.describe())
print (df["cat"].describe())
print()


s = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print('Categories of Dataframe : ')
print(s.categories)
print()

print('Ordered Category : ', s.ordered)
print()


print('Reaming Categories : ')
s = pd.Series(["a","b","c","a"], dtype="category")
s.cat.rename_categories = ["Group %s" %g for g in s.cat.categories]
print (s.cat.rename_categories)
print()

print('Addidng Categories : ')
s = s.cat.add_categories([5,6])
print(s.cat.categories)
print()

print('Removing category : ')
s = s.cat.remove_categories(['a','c'])
print(s.cat.categories)
print()





