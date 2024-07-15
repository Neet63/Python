import cv2
import numpy as np
import matplotlib.pyplot as plt


# Load a color image in grayscale
img = cv2.imread('Image.jpg',1)
# cv2.imshow('image',img)
newimg = cv2.resize(img,(100,100))
plt.imshow(img)
plt.show()
plt.imshow(newimg)
plt.show()


# Rotation
h,w = img.shape[0:2]
center = (w/2, h/2)
# Matrix
mat = cv2.getRotationMatrix2D(center, 90,1)
# Rotated Image
rotimg = cv2.warpAffine(img,mat,(h,w))

plt.imshow(rotimg)
plt.title('Rotated ')
plt.show()
