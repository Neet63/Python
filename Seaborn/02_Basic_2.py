import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Loading Titanic Dataset
titanic = sns.load_dataset('titanic')
titanic.head()

sns.countplot(x='class',data=titanic)
plt.show()

# countplot -> to represent the occurrence(counts) of the observation present in the categorical variable

sns.countplot(data=titanic,x='survived')
plt.show()

# bar plot
sns.barplot(x='sex',y='survived',hue='class',data=titanic)
plt.show()

# correaltionship
correlation = titanic.corr()
plt.figure(figsize=(10,10))
sns.heatmap(correlation,cbar=True,square=True,fmt='.lf',annot=True,annot_kws={'size':8},cmap='Blues')
plt.show()
