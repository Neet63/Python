# plt.arrow(x, y, dx, dy, kwargs)

import matplotlib.pyplot as plt
# Creating a line plot
plt.plot([0, 1], [0, 1])
# Adding an arrow
plt.arrow(0.2, 0.2, 0.4, 0.4, head_width=0.05, head_length=0.1, fc='red', ec='blue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Arrow created by using plt.arrow() function')
# show grid of the plot
plt.grid(True)
plt.show()





# Creating a plot
plt.plot([0, 1], [0, 1])
# Adding an arrow with annotation
plt.annotate('Arrow Annotation', xy=(0.5, 0.5), xytext=(0.2, 0.2), arrowprops=dict(facecolor='yellow',ec = 'red', arrowstyle='->'))
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Arrow Annotation Example')
# Displaying the grid
plt.grid(True)
plt.show()