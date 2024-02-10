import cv2
import matplotlib.pyplot as plt

# Load the grayscale image
image_path = "taj.jpg"  # Replace with the path to your grayscale image
gray_image = cv2.imread(image_path, 0)

if gray_image is None:
    print("Error: Unable to load the image.")
else:
    # Calculate the histogram
    histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    # Plot the histogram
    plt.figure(figsize=(8, 6))
    plt.hist(gray_image.ravel(), 256, [0, 256])
    plt.title('Histogram of Grayscale Image')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.grid(True)

    # Show the original image
    cv2.imshow("Original Gray Image", gray_image)

    # Show the histogram
    plt.show()