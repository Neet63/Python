# LaTeX is a typesetting system widely used for producing scientific and technical documents

# Basic Latex in plot
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
x = np.linspace(-10, 10, 100)
y = np.exp(x)
plt.plot(x, y, color='red', label="$y=e^{x}$")   # latex
plt.legend(loc='upper right')
plt.show()


# Second Example
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
x = np.linspace(1, 10, 1000)
y = np.sin(x)
plt.plot(x, y, label=r'$\sin (x)$', c="red", lw=2)
plt.legend()
plt.show()



plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
x = np.linspace(1, 10, 1000)
y = np.sin(x)
plt.plot(x, y, label=r'$\sin (x)$', c="red", lw=2)
plt.legend(r'αiπ+1=0')
plt.show()


# Showing Equations
equation = r'$x = \frac{{-b \pm \sqrt{{b^2 - 4ac}}}}{{2a}}$'
plt.text(0.5, 0.5, equation, fontsize=12, ha='center')
plt.axis('off')
plt.show()


# Fractions
equation = r'The fraction is $\frac{3}{4}$'
plt.figure(figsize=(6, 3))
plt.text(0.5, 0.5, equation, fontsize=12, ha='center', va='center')
plt.axis('off')
plt.show()

# LaTeX code for the bold text
bold_text = r'$\sin(\theta), \log(x), \lim_{x \to \infty} f(x)$'

# Create a figure and display the bold text
plt.figure(figsize=(6, 3))
plt.text(0.5, 0.5, bold_text, fontsize=12, ha='center', va='center')
plt.axis('off')
plt.show()