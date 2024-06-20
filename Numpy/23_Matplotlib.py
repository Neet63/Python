import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1,11)
y = 2*x + 5

plt.title('Matplotlib Demo')
plt.xlabel('X Axis')
plt.xlabel('Y Axis')
plt.plot(x,y,'ob')
plt.plot(x,y)
plt.show()

# sin wave
x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)
plt.title('Sine Wave and Cos Wave')

plt.plot(x,y,'b')
plt.plot(x,z,'r')
plt.show()


# Subplot()  ->  plot different things in the same figure
# plotting sin and cos same as above but different way

# plt.subplot(height, width, active subplot)
# Set up a subplot grid that has height 2 and width 1, 
# and set the first such subplot as active. 
plt.subplot(2, 1, 1)

# Make the first plot 
plt.plot(x, y) 
plt.title('Sine')

# Set the second subplot as active, and make the second plot. 
plt.subplot(2, 1, 2) 
plt.plot(x, z) 
plt.title('Cosine')

plt.show()


# Bar() -> generate bar graphs

x1 = np.array([1,3,5])
y1 = np.array([4,3,2])

x2 = np.array([2,4,6])
y2 = np.array([1,2,3])

plt.bar(x1,y1, align='center')
plt.bar(x2,y2,color='r',align='center')
plt.title('Bar Graph')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()





