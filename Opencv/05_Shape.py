import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load a color image in grayscale
img = cv2.imread('Image.jpg')
# cv2.imshow('image',img)

# cv2.line(img,pt1,pt2,thickness)
cv2.line(img,(20,100),(200,500), (255,255,255),3)
cv2.rectangle(img,(400,200),(600,600), (0,0,255),5)

cv2.ellipse(img, (300,425), (80, 20), 5, 0, 360, (0,255,255), -1)
cv2.circle(img,(500,500),50, (255,255,0),-1)

plt.imshow(img)
plt.show()


# Adding Font
txt="Roronova Zoro"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,txt,(30,900), font, 5,(0,255,0),10,cv2.LINE_AA)
plt.imshow(img)
plt.show()

