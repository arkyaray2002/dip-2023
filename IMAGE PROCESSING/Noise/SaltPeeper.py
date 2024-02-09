import random
import cv2
import numpy as np

def add_noise(img):
    row, col = img.shape[:2]

    # Add random white pixels
    number_of_pixels = random.randint(300, 400)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        img[y_coord][x_coord] = 255

    # Add random black pixels
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        img[y_coord][x_coord] = 0

    return img

# Read the image from 'RGB2.jpg'
image = cv2.imread('apple.jpg', 0)

# Apply the add_noise function to create a noisy version
noisy_image = add_noise(image)

# Display the noisy image and wait for a key press
cv2.imshow('Noisy one', noisy_image)
cv2.waitKey(0)
