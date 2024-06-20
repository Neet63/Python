import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0,math.pi*2,0.05)
y = np.sin(x)

plt.xlabel('angle')
plt.ylabel('Sine Value')
plt.title('Title')

plt.plot(x,y)
plt.show()