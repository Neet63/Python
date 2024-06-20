import matplotlib.pyplot as plt
import numpy as np

# Generating sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Creating subplots
fig, (ax1, ax2) = plt.subplots(1, 2)

# Plotting on the first subplot
ax1.plot(x, y1)
ax1.set_title('Sine Wave')

# Plotting on the second subplot
ax2.scatter(x, y2)
ax2.set_title('Cosine Wave')

# Displaying the subplots
plt.show()

