# thresholding is a process of creating a binary image based on a threshold value of pixel intensity
# cv2 provide 3 type of thresholding
# 1.simple
# 2.Adeptive
# 3.Otsu

# cv2.threshold(src, thresh, maxval, type, dst)

import numpy as np
import cv2 
import matplotlib.pyplot as plt
# img = cv2.imread('gradient.jpeg')

# ret,img1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# plt.subplot(2,3,1)
# plt.imshow(img,vmin=0,vmax=0)
# plt.title('Original')
# plt.subplot(2,3,2)
# plt.imshow(img1,vmin=0,vmax=0)
# plt.title('OBinary Threshold')

# plt.show()


img = cv2.imread('Image.jpg')
img = cv2.medianBlur(img,5)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

titles = ['Original', 'Mean Thresholding', 'Gaussian Thresholding']
images = [img, th1, th2]

for i in range(3):
   plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
plt.show()
