import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


img = cv2.imread('color_image.jpeg', 0)
min_intensity = np.min(img)
max_intensity = np.max(img)
stretched_img = (((img-min_intensity)/(max_intensity-min_intensity))*255).astype(np.uint8)
equalized_img = cv2.equalizeHist(img)

hist_original = cv2.calcHist([img], [0], None, [256], [0, 255])
hist_stretched = cv2.calcHist([stretched_img], [0], None, [256], [0, 255])
hist_equalized = cv2.calcHist([equalized_img], [0], None, [256], [0, 255])


plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(232)
plt.title('Stretched Image')
plt.imshow(stretched_img, cmap='gray')
plt.axis('off')

plt.subplot(233)
plt.title('Equalized Image')
plt.imshow(equalized_img, cmap='gray')
plt.axis('off')

plt.subplot(234)
plt.title('Histogram-Original')
plt.plot(hist_original)
plt.xlim([0, 256])

plt.subplot(235)
plt.title('Histogram-Stretched')
plt.plot(hist_stretched)
plt.xlim([0, 256])

plt.subplot(236)
plt.title('Histogram-Equalized')
plt.plot(hist_equalized)
plt.xlim([0, 256])

plt.tight_layout()
plt.show()