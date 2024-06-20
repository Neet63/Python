import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [4,5,6,7]
plt.plot(x,y)
plt.xlabel('X label font', fontsize = 20, fontfamily = 'sans-serif', fontstyle='italic')
plt.ylabel('Y label font', fontsize = 10, fontfamily = 'sans-serif')
plt.show()

# Global parameter
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 20

x = [1,2,3,4]
y = [4,5,6,7]
plt.plot(x,y)
plt.xlabel('X label font')
plt.ylabel('Y label font')
plt.show()




print('Controlling Font Properties : ')
# Creating a data
x = [i for i in range(10,40)]
y = [i for i in range(30,60)]

# Creating a plot
plt.scatter(x,y,color = 'blue')
plt.xlabel('X-axis cube values', fontsize = 10)
plt.ylabel('Y-axis cube values', fontsize = 12)
plt.title('plot with defined font size')
plt.show()




print('Second FOnt properties: ')
# Creating a data
x = [i for i in range(10,40)]
y = [i for i in range(30,60)]

# Creating a plot
plt.scatter(x,y,color = 'blue')
plt.xlabel('X-axis cube values', fontweight='bold')
plt.ylabel('Y-axis cube values', fontweight='bold')
plt.title('plot with defined font size',fontweight='bold')
plt.grid('on')
plt.show()