
import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('/home/sibi/Desktop/dip/Images/parrot.jpg')
image_processing_functions = [
    ('Original Image', lambda img: img),
    ('Sepia Filter', lambda img: cv2.transform(img, np.array([[0.393, 0.769, 0.189],
                                                               [0.349, 0.686, 0.168],
                                                               [0.272, 0.534, 0.131]]))),
    ('Emboss Filter', lambda img: cv2.filter2D(img, -1, np.array([[0, -1, -1],
                                                                  [1,  0, -1],
                                                                  [1,  1,  0]]))),
    ('Enhanced Sharpening', lambda img: cv2.filter2D(img, -1, np.array([[0, -1, 0],
                                                                         [-1, 6, -1],
                                                                         [0, -1, 0]]))),
    ('Sobel Edge Detection', lambda img: cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=5)),
    ('Cartoonize', lambda img: cv2.stylization(img, sigma_s=150, sigma_r=0.25)),
    ('Sketch', lambda img: cv2.cvtColor(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2RGB)),
    ('Invert Colors', lambda img: cv2.bitwise_not(img)),
    ('Erosion', lambda img: cv2.erode(img, np.ones((5, 5), np.uint8), iterations=1)),
    ('Dilation', lambda img: cv2.dilate(img, np.ones((5, 5), np.uint8), iterations=1)),
    ('Bilateral Filter', lambda img: cv2.bilateralFilter(img, 9, 75, 75)),
    ('High-Pass Filter', lambda img: cv2.filter2D(img, -1, np.array([[-1, -1, -1],
                                                                    [-1,  8, -1],
                                                                    [-1, -1, -1]]))),
]
for i, (title, processing_function) in enumerate(image_processing_functions):
    processed_image = processing_function(image)
    plt.subplot(3, 4, i + 1)  # Adjust subplot layout based on the number of functions
    plt.imshow(processed_image)
    plt.title(title)
    plt.axis('off')  # Turn off axis labels
plt.show()
