# contour is an outline representing or bounding the shape or form of something.
# contour is used for shape analysis and object detection

# before finding contour apply thresold or canny edge detection
# cv.findContours(image, mode, method, contours)

# Contour retrival modes:
# 1. cv.RETR_EXTERNAL − Retrieves only the extreme outer contours.
# 2. cv.RETR_LIST − Retrieves all of the contours without establishing any hierarchical relationships.
# 3. cv.RETR_CCOMP − Retrieves all of the contours and organizes them into a twolevel hierarchy.
# 4. cv.RETR_TREE − Retrieves all of the contours and reconstructs a full hierarchy of nested contours.


# Contour approximation methods:
# 1. cv.CHAIN_APPROX_NONE − Stores absolutely all the contour points.
# 2. cv.CHAIN_APPROX_SIMPLE − Compresses horizontal, vertical, and diagonal segments and leaves only their end points.


# cv.drawContours(image, contours, contourIdx, color)
# To draw contour




import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')

plt.subplot(2,2,1)
plt.imshow(img)
plt.title('Original')
plt.axis(False)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 30, 200)

contours, hierarchy = cv2.findContours(canny,
                                       cv2.RETR_EXTERNAL, 
                                       cv2.CHAIN_APPROX_NONE)

print("Number of Contours = " ,len(contours))

plt.subplot(2,2,2)
plt.imshow(canny)
plt.title('Canny Edges')
plt.axis(False)

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)


plt.subplot(2,2,3)
plt.imshow(img)
plt.title('Contour')
plt.axis(False)

plt.show()
