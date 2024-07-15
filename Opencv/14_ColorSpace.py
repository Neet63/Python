# color space is a mathematical model describing how colours can be represented

# cv.cvtColor(src, code, dst)


import cv2
import matplotlib.pyplot as plt
img = cv2.imread('Image.jpg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Displaying the image


plt.subplot(2,2,1)
plt.imshow(img)
plt.title('Original')
plt.subplot(2,2,2)
plt.imshow(img1)
plt.title('gray')
plt.subplot(2,2,3)
plt.imshow(img2)
plt.title('HSV')
plt.show()

