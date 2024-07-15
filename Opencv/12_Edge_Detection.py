import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# cv2.Canny() function that identifies the edges of various objects

img = cv.imread('Image.jpg', 0)
edges = cv.Canny(img,100,200)

plt.subplot(1,2,1)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])

plt.subplot(1,2,2)
plt.imshow(edges,cmap = 'gray')
plt.title('Edges of original Image')
plt.xticks([])
plt.yticks([])

plt.show()