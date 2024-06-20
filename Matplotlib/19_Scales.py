import numpy as np
import matplotlib.pyplot as plt

# scales refer to the mapping of data values to the physical dimensions of a plot
# Three type of scales:
# 1. Linear Scale
# 2. Logarithmic scale
# 3. Symmetrical Logarithmic Scale
# 4.Logit Scale

# Linear Scale
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Linear Scale')
plt.show()


# Logerithmic Scale
# Generating logarithmically spaced data
x = np.linspace(1, 10, 100)
y = np.log(x)

# Creating a plot with a logarithmic scale for the x-axis
plt.plot(x, y)
plt.xscale('log')  # Set logarithmic scale for the x-axis
plt.xlabel('X-axis (log scale)')
plt.ylabel('Y-axis')
plt.title('Logarithmic Scale')
plt.show()


# Symmetrical Logarithmic Scale
# Generating data for a sine wave with values around zero
x = np.linspace(-10, 10, 500)
y = np.sin(x)

# Creating a plot with a symmetrical logarithmic scale for the y-axis
plt.plot(x, y)

# Set symmetrical logarithmic scale for the y-axis
plt.yscale('symlog', linthresh=0.01)  
plt.xlabel('X-axis')
plt.ylabel('Y-axis (symlog scale)')
plt.title('Symmetrical Logarithmic Scale')
plt.show()






# All Scale in one plot
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')

# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')

# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.01)
plt.title('symlog')

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.show()