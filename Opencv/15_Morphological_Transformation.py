# Simple operations on an image based on its shape are termed as morphological transformations
# two most common transformations are
# 1. erosion 
# 2. dilation


# Erosion -> gets rid of the boundaries of the foreground object
# The pixel in the original image is retained, if all the pixels under the kernel are 1. otherwise 0

# cv.erode(src, kernel, dst, anchor, iterations)


# Dialation ->  It is just the opposite of erosion
# Here, a pixel element is 1, if at least one pixel under the kernel is 1

# cv.dilate(src, kernel, dst, anchor, iterations)




import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('Image2.jpg',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)
dilation = cv.dilate(img,kernel,iterations = 1)


plt.subplot(2,2,1)
plt.imshow(img)
plt.title('Original')

plt.subplot(2,2,2)
plt.imshow(erosion)
plt.title('Eroison')

plt.subplot(2,2,3)
plt.imshow(dilation)
plt.title('Dialation')

plt.show()



