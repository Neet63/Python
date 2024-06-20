import matplotlib.pyplot as plt
import numpy as np

# Example data
x = [1, 2, 3]
y1 = [2, 4, 6]
y2 = [1, 3, 5]
y3 = [3, 6, 9]

# Plotting the data
line1, = plt.plot(x, y1)
line2, = plt.plot(x, y2)
line3, = plt.plot(x, y3)

# calling legend with explicitly listed artists and labels
plt.legend([line1, line2, line3], ['Label 1', 'Label 2', 'Label 3'], loc = 'center')

# Show the plot
plt.show()
print('Successfully Placed a legend on the Axes...')


plt.rcParams["figure.figsize"] = [7, 3.50]
plt.rcParams["figure.autolayout"] = True

# Sample data
x = np.linspace(-2, 2, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Create the figure with subplots
f, axes = plt.subplots(3)

# plot the data on each subplot and add lagend
axes[0].plot(x, y1, c='r', label="sine")
axes[0].legend(loc='upper left')
axes[1].plot(x, y2, c='g', label="cosine")
axes[1].legend(loc='upper right')
axes[2].plot(x, y3, c='b', label="tan")
axes[2].legend(loc='upper center')

# Display the figure
plt.show()