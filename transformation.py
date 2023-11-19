import cv2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

image = cv2.imread('flower2.jpeg')
resized_image = cv2.resize(image, (180, 180))
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
anti_rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
flipped_horizontal = cv2.flip(image, 1)
flipped_vertical = cv2.flip(image, 0)
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(image, (15, 15), 5)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.figure(figsize=(12, 8))

plt.subplot(241)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(242)
plt.title('Resized Image')
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(243)
plt.title('Rotated Image')
plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(244)
plt.title('Anti-Rotated Image')
plt.imshow(cv2.cvtColor(anti_rotated_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(245)
plt.title('Horizontally Flipped Image')
plt.imshow(cv2.cvtColor(flipped_horizontal, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(246)
plt.title('Vertically Flipped Image')
plt.imshow(cv2.cvtColor(flipped_vertical, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(247)
plt.title('Grayscale Image')
plt.imshow(grayscale_image, cmap='gray')
plt.axis('off')

plt.subplot(248)
plt.title('Blurred Image')
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.tight_layout
plt.show()