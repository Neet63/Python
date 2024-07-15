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