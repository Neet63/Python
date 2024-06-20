import matplotlib.pyplot as plt
import numpy as np

# Create a sample image (random pixels)
image = np.random.rand(100, 100)

# Create a mask to hide certain parts of the image
mask = np.zeros_like(image)
mask[30:70, 30:70] = 1  # Masking a square region

# Apply the mask to the image
masked_image = np.ma.masked_array(image, mask=mask)

# Display the original and masked images
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(masked_image, cmap='gray')
plt.title('Masked Image')
plt.axis('off')
plt.show()