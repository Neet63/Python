# convert an image to a size different than its original.
# upsize or downsize the images

# Gaussian pyramid is used to down sample images
# Laplacian pyramid reconstructs an up sampled image from an image lower in the pyramid with less resolution.

import sys
import cv2 as cv
import matplotlib.pyplot as plt

filename = 'Image.jpg'

src = cv.imread(filename)

while 1:
   print ("press 'i' for zoom in 'o' for zoom out esc to stop")
   rows, cols, _channels = map(int, src.shape)
   plt.imshow(src)
   plt.title('Source')
   plt.show()
   k = cv.waitKey(0)   # cv2 not working

   if k == 27:
      break

   elif chr(k) == 'i':
      src = cv.pyrUp(src, dstsize=(2 * cols, 2 * rows))

   elif chr(k) == 'o':
      src = cv.pyrDown(src, dstsize=(cols // 2, rows // 2))
