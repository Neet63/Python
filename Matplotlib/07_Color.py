import matplotlib.pyplot as plt
import numpy as np

# sample data
t = np.linspace(0.0, 2.0, 201)
s = np.sin(2 * np.pi * t)

# RGB tuple for specifying facecolor
fig, ax = plt.subplots(figsize=(7,4), facecolor=(.18, .31, .0   ))

# Plotting the data
plt.plot(t, s)
plt.title('RGB Tuple')

# Show the plot
plt.show()
print('successfully used the RGB tuple for specifying colors..')

# Hex string for specifying axis facecolor
fig, ax = plt.subplots(figsize=(7,4))
ax.set_facecolor('#eafff5')
plt.title('Hex sTRING')

# Plotting the data
plt.plot(t, s)

# Show the plot
plt.show()
print('successfully used the Hex string for specifying colors..')


# create a plot
fig, ax = plt.subplots(figsize=(7,4))

# Plotting the data
plt.plot(t, s)
# using the Gray level string for specifying title color
ax.set_title('Voltage vs. time chart', color='0.7')

# Show the plot
plt.show()
print('successfully used the Gray level string for specifying colors..')


# create a plot
fig, ax = plt.subplots(figsize=(7,4))

# Cn notation for plot
ax.plot(t, .7*s, color='C1', linestyle='--')
plt.title('CN color')
# Show the plot
plt.show()
print('successfully used the Cn notation for specifying colors..')



