import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps
import matplotlib as mpl
from matplotlib.colors import ListedColormap
# print(list(colormaps))

viridis = colormaps['viridis'].resampled(8)
print(viridis(0.37))

# Custom Colormap

# Creating a ListedColormap from color names
colormaps = [ListedColormap(['rosybrown', 'gold', "crimson", "linen"])]

# Plotting examples
np.random.seed(19680801)
data = np.random.randn(30, 30)
n = len(colormaps)

fig, axs = plt.subplots(1, n, figsize=(7, 3), layout='constrained', squeeze=False)
for [ax, cmap] in zip(axs.flat, colormaps):
   psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
   fig.colorbar(psm, ax=ax)

plt.show()