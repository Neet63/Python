import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Create a figure and axis for the colorbar
fig, ax = plt.subplots(figsize=(6, 1), constrained_layout=True)

# Define a colormap and normalization for the colorbar
cmap = mpl.cm.cool
norm = mpl.colors.Normalize(vmin=5, vmax=10)

# Create a ScalarMappable without associated data using the defined cmap and norm
scalar_mappable = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)

# Add a horizontal colorbar to the figure 
colorbar = fig.colorbar(scalar_mappable, cax=ax, orientation='horizontal', label='Some Units')

# Set the title and display the plot
plt.title('Basic Colorbar')
plt.show()




# Generate sample data
data = np.random.random((100, 100))

# Create a plot with an image and a colorbar
fig, ax = plt.subplots(figsize=(7,4))
im = ax.imshow(data, cmap='viridis')

# Add a colorbar to the right of the image
cbar = plt.colorbar(im, ax=ax)

# Show the plot
plt.show()
print('Successfully drawn the colorbar...')