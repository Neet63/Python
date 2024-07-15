import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load an color image in grayscale and write that in other file
img = cv2.imread('Image.jpg',0)
# cv2.imshow('image',img)
plt.imshow(img)
plt.show()
cv2.imwrite("opencv_logo_GS.png", img)
