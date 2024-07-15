import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load dataset and plot from that

# seaborn has some builtin datasets
# load the dataset
tips = sns.load_dataset('tips')
print(tips.head())

# To set theme of plot
sns.set_theme()

# Visulize the data with relationalship plot
sns.relplot(data = tips,x = "total_bill",y='tip',col='time',hue='smoker',style = 'smoker',size='size')
plt.show()
# relplot() -> relationship plot
# col -> create different plotbased on differnt value , here 2 plot dinner and lunch
# hue -> color the person based on specific property -> here smoker and non smoker
# style -> Differentiates the points' styles (e.g., markers) based on whether the customer is a smoker or not.
# size -> representing the size of the party.



#loading iris dataset
iris = sns.load_dataset('iris')
iris.head()

sns.scatterplot(x='sepal_length',y='petal_length',hue='species',data=iris)
plt.show()


sns.scatterplot(x='sepal_length',y='petal_width',hue='species',data=iris)
plt.show()
