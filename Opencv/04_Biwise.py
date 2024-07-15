import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('images.png')
img2 = cv2.imread('image3.png')
h,w,d = img2.shape
img1 = cv2.resize(img1,(h,w))

dest1 = cv2.bitwise_and(img2, img1, mask=None)
dest2 = cv2.bitwise_or(img2, img1, mask=None)
dest3 = cv2.bitwise_xor(img1, img2, mask=None)
dest4 = cv2.bitwise_not(img1)
dest5 = cv2.bitwise_not(img2)

plt.imshow(img1)
plt.title('Image 1 ')
plt.show()

plt.imshow(img2)
plt.title('Image 2 ')
plt.show()

plt.imshow(dest1)
plt.title('Biwise AND ')
plt.show()

plt.imshow(dest2)
plt.title('Bitwise OR')
plt.show()

plt.imshow(dest4)
plt.title('Bitwise NOT img1')
plt.show()

plt.imshow(dest5)
plt.title('Bitwise NOT Image2')
plt.show()


