import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('Image.jpg')
img2 = cv2.imread('Image2.jpg')

addition = cv2.add(img1, img2)

plt.imshow(addition)
plt.show()

addition = cv2.addWeighted(img1,0.3, img2,0.7,0)
plt.imshow(addition)
plt.show()