import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the low-contrast image
image = cv2.imread('flower.jpeg', cv2.IMREAD_GRAYSCALE)

# Perform contrast stretching
min_intensity = np.min(image)

max_intensity = np.max(image)
stretched_image = ((image - min_intensity) / (max_intensity - min_intensity) * 255).astype(np.uint8)

# Calculate the histogram of the original and stretched images
hist_original = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_stretched = cv2.calcHist([stretched_image], [0], None, [256], [0, 256])

# Perform histogram equalization
equalized_image = cv2.equalizeHist(image)

# Calculate the histogram of the equalized image
hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

# Display the original, stretched, and equalized images and their histograms
plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(232)
plt.title('Stretched Image')
plt.imshow(stretched_image, cmap='gray')
plt.axis('off')

plt.subplot(233)
plt.title('Equalized Image')
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')

plt.subplot(234)
plt.title('Histogram (Original)')
plt.plot(hist_original)
plt.xlim([0, 256])

plt.subplot(235)
plt.title('Histogram (Stretched)')
plt.plot(hist_stretched)
plt.xlim([0, 256])
plt.subplot(236)
plt.title('Histogram (Equalized)')
plt.plot(hist_equalized)
plt.xlim([0, 256])

plt.tight_layout()
plt.show()