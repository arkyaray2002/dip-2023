import numpy as np
import cv2

def noisy(noise_typ, image):
    if noise_typ == "gauss":
        row, col, ch = image.shape
        mean = 0
        var = 0.1
        sigma = var**0.5
        gauss = np.random.normal(mean, sigma, (row, col, ch))
        gauss = gauss.reshape(row, col, ch)
        noisy = image + gauss
        return noisy

# Read the image from 'RGB2.jpg'
image = cv2.imread('rose.jpg')

# Apply the noisy function with Gaussian noise
noise = noisy('gauss', image)

# Display the noisy image and wait for a key press
cv2.imshow('Noise', noise)
cv2.waitKey(0)
