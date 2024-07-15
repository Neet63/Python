import matplotlib.pyplot as plt
import numpy as np


fig3 = plt.figure()
ax = plt.axes(projection = '3d')  #projection = '3d' ->plot graph in 3d
z = 20 * np.random.random(100)
x = np.sin(z)
y = np.cos(z)
ax.scatter(x,y,z, cmap='blue')   #cmap -> colormap
plt.show()