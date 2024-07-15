# Image filtering is a process of averaging the pixel values so as to alter the shade, brightness, contrast etc. of the original image.
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Image.jpg')

kernel = np.ones((3,3),np.float32)/10
dst = cv.filter2D(img,-1,kernel)
plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(1,2,2)
plt.imshow(dst)
plt.title('Convolved')
plt.xticks([])
plt.yticks([])
plt.show()