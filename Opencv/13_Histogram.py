# Histogram shows the intensity distribution in an image. 
# It plots the pixel values (0 to 255) on X axis and number of pixels on Y axis.

# cv.calcHist(images, channels, mask, histSize, ranges)

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('Image.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
   hist = cv.calcHist([img],[i],None,[256],[0,256])
   plt.plot(hist, color = col)
   plt.xlim([0,256])
plt.show()


