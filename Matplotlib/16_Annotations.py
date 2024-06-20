import matplotlib.pyplot as plt
import numpy as np

# Plotting data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y, marker='o', linestyle='-', color='blue')

# Adding annotation
plt.annotate('Peak', xy=(3, 5), xytext=(4, 6), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Annotated Plot')
plt.grid(True)
plt.show()


# Multiple Annotations

# Create data points to be plotted
x = np.random.rand(30)
y = np.random.rand(30)

# Define the scatter plot using Matplotlib
fig, ax = plt.subplots()
ax.scatter(x, y)

# Add annotations to specific data points using text or arrow annotations
ax.annotate('Outlier', xy=(0.9, 0.9), xytext=(0.7, 0.7),arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Important point', xy=(0.5, 0.3), xytext=(0.3, 0.1),arrowprops=dict(facecolor='red', shrink=0.05))
ax.annotate('Cluster of points', xy=(0.2, 0.5), xytext=(0.05, 0.7),arrowprops=dict(facecolor='green', shrink=0.05))
   
# Adjust the annotation formatting as needed
plt.title('Annotated Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the scatter plot with annotations
plt.show()