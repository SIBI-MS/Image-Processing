import cv2
import matplotlib.pyplot as plt

color_image = cv2.imread('baby.jpg')
negative_color_image = 255 - color_image

gray_image = cv2.imread('baby.jpg', cv2.IMREAD_GRAYSCALE)
negative_gray_image = 255 - gray_image
cv2.waitKey(0)
cv2.destroyAllWindows()

fig, axes = plt.subplots(2, 2, figsize=(6, 6))

# Plot the color image in the first subplot
axes[0, 0].imshow(cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB))
axes[0, 0].set_title('Color Image')

# Plot the negative color image in the second subplot
axes[0, 1].imshow(cv2.cvtColor(negative_color_image, cv2.COLOR_BGR2RGB))
axes[0, 1].set_title('Negative Color Image')

# Plot the grayscale image in the third subplot
axes[1, 0].imshow(gray_image, cmap='gray')
axes[1, 0].set_title('Grayscale Image')

# Plot the negative grayscale image in the fourth subplot
axes[1, 1].imshow(negative_gray_image, cmap='gray')
axes[1, 1].set_title('Negative Grayscale Image')

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()






