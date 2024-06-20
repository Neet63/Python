import matplotlib as mpl
from matplotlib.colors import Normalize
import numpy as np
from matplotlib import colors,cm
import matplotlib.pyplot as plt

# Matplotlib's linear normalization process using the Normalize()
print('Matplotlibs linear normalization process using the Normalize')
# Creates a Normalize object with a specified range
norm = Normalize(vmin=-1, vmax=1)

# Normalizing a value
normalized_value = norm(0)

# Display the normalized value
print('Normalized Value', normalized_value)

# Sample Data
X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(7,4), layout='constrained')

# Logarithmic Normalization 
pc = ax[0].imshow(Z**2 * 100, cmap='plasma',
   norm=colors.LogNorm(vmin=0.01, vmax=100))
fig.colorbar(pc, ax=ax[0], extend='both')
ax[0].set_title('Logarithmic Normalization')

# Linear Normalization
pc = ax[1].imshow(Z**2 * 100, cmap='plasma',
   norm=colors.Normalize(vmin=0.01, vmax=100))
fig.colorbar(pc, ax=ax[1], extend='both')
ax[1].set_title('Linear Normalization')
plt.show()




# CenteredNorm()

# select a divergent colormap
cmap = cm.coolwarm 

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(7,4), layout='constrained')

# Default Linear Normalization
pc = ax[0].pcolormesh(Z, cmap=cmap)
fig.colorbar(pc, ax=ax[0])
ax[0].set_title('Normalize')

# Centered Normalization
pc = ax[1].pcolormesh(Z, norm=colors.CenteredNorm(), cmap=cmap)
fig.colorbar(pc, ax=ax[1])
ax[1].set_title('CenteredNorm()')

plt.show()