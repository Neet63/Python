# template matching is used to detect one 
# or more areas in an image that matches with a sample or template image.

# cv.matchTemplate(image, templ, method)

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Virat_and_dhoni.png',1)

plt.imshow(img)
plt.title('Original')
plt.show()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('virat.png',0)

plt.imshow(template)
plt.title('Template')
plt.show()

w,h = template.shape[0], template.shape[1]

matched = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
print(matched)
loc = np.where( matched >= threshold)

for pt in zip(*loc[::-1]):
   cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)


plt.imshow(img)
plt.title('Matched')

plt.show()