import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

# Load the image
img = mpimg.imread('Image.jpg')  # Load image file

# Display the image
plt.imshow(img)
plt.axis('off')  # Turn off axis labels and ticks (optional)
plt.show()


# Colormap
# Load the image
img = mpimg.imread('Image.jpg')  # Load image file

# Display the image
plt.imshow(img , cmap='gray')
plt.colorbar()
plt.axis('on')  # Turn off axis labels and ticks (optional)
plt.show()


# Cropping Image
plt.imshow(img[300:800, 500:1200])
plt.show()

# Resized image
resized_img = cv2.resize(img, (200,200))
plt.imshow(img)
plt.show()
