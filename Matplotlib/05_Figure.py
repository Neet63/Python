# figure is the top-level container that holds all elements of a plot or visualization.

# plt.figure(figsize=(width, height), dpi=resolution)

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure
plt.figure(figsize=(8, 6), dpi=100)

# Add a line plot to the figure
plt.plot(x, y, label='Line Plot')
# add another plot on same graph
plt.scatter([1, 2, 3], [3, 5, 7], label='Points')
plt.legend()

# Customize the plot
plt.title('Figure with Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Display the figure
plt.show()

# legend
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