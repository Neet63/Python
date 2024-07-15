import cv2
import numpy as np
import matplotlib.pyplot as plt

# cv2.setMouseCallback(window, callbak_function)

# Callback function
def drawcircle(event,x,y,flag,params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
      cv2.circle(img,(x,y),20,(255,255,255),-1)

img = cv2.imread('Image.jpg')
cv2.imshow('Image',img)

plt.imshow(img)
cv2.setMouseCallback('Image', drawcircle)

plt.show()