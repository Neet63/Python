import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load a color image in grayscale
img = cv2.imread('Image.jpg')
plt.imshow(img)
plt.show()

print('Shape of Image : ',img.shape)
# shape give tuple -> (heights, width, number of channel)

print('Size of image : ', img.size)

img2 = img

# Modifying the property
# making some part as black or other color
for i in range(1000):
   for j in range(1000):
      img[i,j]=[250,0,0]      # color code
      
plt.imshow(img)
plt.show()


# Image can be split in invidual planes by split()

b,g,r = cv2.split(img2)
img2[:,:,0] = [0,255,0]
plt.imshow(img2)
plt.show()