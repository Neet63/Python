import numpy as np
import matplotlib.pyplot as plt

# Create a new Figure 
fig = plt.figure()

# add plot in figure
x = np.random.randint(1,20,(10,1))
y = x*2
plt.plot(x,y)
plt.show()

# Axes/ Subplots

# Creating a 2x2 grid of subplots
fig, axes = plt.subplots(nrows=2, ncols=2)

# Accessing individual axes (subplots)
axes[0, 0].plot([1, 2, 3], [4, 5, 6])  # Plot in the first subplot (top-left)
axes[0, 1].scatter([4,5,6], [4, 5, 6])  # Second subplot (top-right)
axes[1, 0].bar([4,5,6], [1,2,3])  # Third subplot (bottom-left)
axes[1, 1].hist([1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5])  # Fourth subplot (bottom-right)
plt.show()


# Axis
# Creating a plot
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])

# Customizing axis limits and labels
plt.xlim(0, 5)
plt.ylim(0, 35)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Artist -> components or entities that make up a plot such as figures, axes, lines, text, patches, shapes etc
# Create a figure and an axis (subplot)
fig, ax = plt.subplots()

# Plot a line (artist)
line = ax.plot([1, 2, 3], [4, 5, 6], label='Line')[0]

# Modify line properties
line.set_color('red')
line.set_linewidth(2.5)

# Add labels and title (text artists)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Artist Plot')
plt.legend()
plt.show() 
