from PIL import Image

def combine_images(left_image_path, right_image_path, output_image_path):
    # Open the images
    left_image = Image.open('image1.png')
    right_image = Image.open('image2.png')

    # Ensure both images are of the same size (256 x 256)
    if left_image.size != (256, 256) or right_image.size != (256, 256):
        print("Error: Images must be 256 x 256 pixels.")
        return

    # Create a new blank image (mode 'RGB')
    combined_image = Image.new('RGB', (256, 256))

    # Paste the left half of the first image onto the new image
    combined_image.paste(left_image.crop((0, 0, 128, 256)), (0, 0))

    # Paste the right half of the second image onto the new image
    combined_image.paste(right_image.crop((128, 0, 256, 256)), (128, 0))

    # Save and show the combined image
    combined_image.save(output_image_path)
    combined_image.show()

# Replace 'lena.bin' and 'peppers.bin' with your actual file paths
combine_images('image1.png', 'image2.png', 'output_image.png')
